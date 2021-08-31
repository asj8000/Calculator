import tkinter as tk

historyValue = ''
lastValue = ''
inputValue = 0
calculatedValue = 0
actionStatus = 0

def clickFunc(value):
    if value.isdigit():
        enterNumber(value)
    else:
        enterCommand(value)

def enterNumber(value):
    global inputValue, actionStatus
    if actionStatus == 1 :
        print('z')
        inputValue = int(value)
        inputVisibleValue.set(str(value))
    else:
        print('a')
        inputValue = (inputValue*10) + int(value)
        inputVisibleValue.set(str(inputValue))
    actionStatus = 0

def enterCommand(Command):
    global historyValue, lastValue, inputValue, calculatedValue, actionStatus

    calculationCommentList = ['+','-','x','/','=']
    if Command in calculationCommentList:
        if actionStatus == 1:
            inputValue = calculation(Command)
            historyValue = lastValue + " " + str(inputValue) + " " + Command
            historyVisibleValue.set(str(historyValue))
            inputVisibleValue.set(inputValue)
        else:
            inputValue = calculation(Command)
            lastValue = historyValue
            historyValue = historyValue + " " + str(inputValue) + " " + Command
            historyVisibleValue.set(str(historyValue))
            inputVisibleValue.set(inputValue)
        actionStatus = 1

def calculation(Command):
    global historyValue, lastValue, inputValue, calculatedValue, actionStatus
    
    if calculatedValue == 0:
        result = inputValue
    elif Command == "+":
        result = calculatedValue + inputValue
    elif Command == "-":
        result = calculatedValue - inputValue
    elif Command == "x":
        result = calculatedValue * inputValue
    elif Command == "/":
        result = calculatedValue / inputValue
    else:
        result = '???'

    return result

#GUI 그리기 시작
layout = tk.Tk()
layout.title('계산기')
layout.resizable(False,False)

historyVisibleValue = tk.StringVar()
historyVisibleValue.set(str(historyValue))
histroyArea = tk.Entry(layout, textvariable=historyVisibleValue, state="disable", justify="right")
histroyArea.grid( column=0, row=0, columnspan = 4, ipadx=80,  ipady = 10)

inputVisibleValue = tk.StringVar()
inputVisibleValue.set(str(inputValue))
inputArea = tk.Entry(layout, textvariable=inputVisibleValue, justify="right")
inputArea.grid(column=0, row=1, columnspan=4, ipadx=80, ipady=30)

layoutIndex = [
    ["","","","<-"],
    ["C","CE","( )","/"],
    ["7","8","9","x"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["+/-","0",".","="]
]

for i, layerDetail in enumerate(layoutIndex):
    for k, value in enumerate(layerDetail):
        button = tk.Button(layout, 
            text = value, 
            width = 10,      
            height = 3,
            bg = 'white',   
            fg = 'black',
            command = lambda 
            val = value: clickFunc(val)
        )
        button.grid(column = k, row = (i + 2))
layout.mainloop()