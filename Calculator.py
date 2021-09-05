import tkinter as tk
from tkinter.constants import PROJECTING
import algorithm

#히스토리 값 (화면 상단)
historyValue = ''
#이전 히스토리 값
lastValue = ''

#현재 입력된 값
inputValue = 0
#현재 작동
actionStatus = 0
isDecimalPoint = 0


#버튼 클릭 시 작동
def clickFunc(value):
    if value.isdigit():
        enterNumber(value)
    else:
        enterCommand(value)

#숫자 입력 시 작동 함수


def enterNumber(value):
    global inputValue, actionStatus, isDecimalPoint
    # 현재 무슨 동작을 하고 있냐(actionStatus)를 받아와서
    # 연산자 다음으로 입력되는 숫자일 경우 인풋 창 지우고 새로 입력
    if actionStatus == 1:
        inputValue = int(value)
        inputVisibleValue.set(str(value))
        actionStatus = 0
    # 식 종료 다음으로 입력되는 숫자일 경우 전부 지우고 새로 입력
    elif actionStatus == 2:
        clearCommand()
        inputValue = int(value)
        inputVisibleValue.set(str(value))
        actionStatus = 0
    # 숫자를 처음 or 연속으로 입력할 경우 기존 숫자에 다음에 추가
    else:
        print(isDecimalPoint)
        if isDecimalPoint != 0:
            for i in range(isDecimalPoint):
                value = float(value) / 10
            inputValue = inputValue + float(value)
            inputVisibleValue.set(str(inputValue))
            isDecimalPoint += 1
        else:
            inputValue = (inputValue*10) + int(value)
            inputVisibleValue.set(str(inputValue))

#커멘드 입력 시 작동 함수


def enterCommand(Command):
    global historyValue, lastValue, inputValue, actionStatus, isDecimalPoint
    isDecimalPoint = 0
    #사칙연산 커멘드일 경우
    calculationCommentList = ['+', '-', '*', '/']
    if Command in calculationCommentList:
        #결과값을 얻고 그 다음 동작시에 기존 정보들 초기화.
        if actionStatus == 2:
            beforeResult = inputValue
            clearCommand()
            historyValue = str(beforeResult) + " " + Command
            historyVisibleValue.set(str(historyValue))
            inputVisibleValue.set(str(0))
        #커멘드를 연속으로 입력할 경우 예외처리 (기존 입력 커멘드 제거하고 새 입력 커멘드로 변경)
        elif actionStatus == 1:
            historyValue = lastValue + " " + str(inputValue) + " " + Command
            historyVisibleValue.set(str(historyValue))
        else:
            lastValue = historyValue
            historyValue = historyValue + " " + str(inputValue) + " " + Command
            historyVisibleValue.set(str(historyValue))
            inputVisibleValue.set(str(0))
        actionStatus = 1
    #소숫점( . ) 커멘드일 경우
    elif Command == '.':
        if isDecimalPoint == 0 or inputValue == 0 or inputValue == '':
            value = str(inputValue) + "."
            inputVisibleValue.set(str(value))
            isDecimalPoint = 1
    #연산( = ) 커멘드일 경우
    elif Command == '=':
        historyValue = historyValue + " " + str(inputValue)
        historyVisibleValue.set(historyValue + " " + Command)
        # print(historyValue)
        inputValue = algorithm.processing(historyValue)
        # print(inputValue)
        inputVisibleValue.set(inputValue)
        actionStatus = 2
    #초기화 커멘드일 경우
    elif Command == 'C':
        clearCommand()
    #delete 커멘드일 경우
    elif Command == '<-':
        deleteCommand()

#초기화 함수


def clearCommand():
    global historyValue, lastValue, inputValue, actionStatus
    historyValue = ''
    lastValue = ''
    inputValue = 0
    actionStatus = 0
    historyVisibleValue.set(str(''))
    inputVisibleValue.set(str(inputValue))

#지우기 함수


def deleteCommand():
    global inputValue
    try:
        inputValue = int(str(inputValue)[:-1])
    except:
        inputValue = 0
    inputVisibleValue.set(str(inputValue))


#GUI layout 그리기 시작
layout = tk.Tk()
layout.title('계산기')
layout.resizable(False, False)

#보여질 히스토리 값과 인풋값 value 셋팅
historyVisibleValue = tk.StringVar()
historyVisibleValue.set(str(historyValue))
inputVisibleValue = tk.StringVar()
inputVisibleValue.set(str(inputValue))

#인풋 영역 레이아웃 그리기 시작.
histroyArea = tk.Entry(
    layout, textvariable=historyVisibleValue, state="disable", justify="right")
histroyArea.grid(column=0, row=0, columnspan=4, ipadx=80,  ipady=10)
inputArea = tk.Entry(layout, textvariable=inputVisibleValue, justify="right")
inputArea.grid(column=0, row=1, columnspan=4, ipadx=80, ipady=30)

#버튼 영역 레이아웃 그리기 시작
layoutIndex = [
    ["", "", "", "<-"],
    ["C", "CE", "( )", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["", "0", ".", "="]
]
for i, layerDetail in enumerate(layoutIndex):
    for k, value in enumerate(layerDetail):
        button = tk.Button(layout,
                           text=value,
                           width=10,
                           height=3,
                           bg='white',
                           fg='black',
                           command=lambda
                           val=value: clickFunc(val)
                           )
        button.grid(column=k, row=(i + 2))
layout.mainloop()
