def isInt(value):
    return value.isdigit()

#계산식을 스택으로 관리
class Stack:
    def __init__(self):
        self.data = [] 
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return self.size() == 0
    def push(self, item):
        self.data.append(item)
    def pop(self):
        return self.data.pop()
    def peek(self):
        return self.data[-1]

class Calculation:
    def splitExpression(self,expression):
        expressionList = []
        number = 0
        isNumber = False
        isDecimalPoint = 0

        expression = expression.replace(" ","")
        
        for value in expression:
            if isInt(value):
                value = int(value)
                if isDecimalPoint != 0:
                    for i in range(isDecimalPoint):
                        value = value / 10
                    number = number + value
                    isDecimalPoint += 1
                else:
                    number = number * 10 + int(value)
                isNumber = True
            elif value == ".":
                isDecimalPoint = 1
            else:
                if isNumber:
                    expressionList.append(number)
                    number = 0
                isNumber = False
                isDecimalPoint = 0
                expressionList.append(value)
        if isNumber == True:
            expressionList.append(number)
        return expressionList

    def infixToPostfix(self,expression):
        stack = Stack()
        expressionList = []
        prec = { '*' : 3, '/' : 3, '+' : 2, '-' : 2, '(' : 1 }
        
        for value in expression:
            try:
                value = float(value)
                expressionList.append(value)
            except:
                if value == '(':
                    stack.push(value)
                elif value == ')':
                    while stack.peek() != '(':
                        expressionList.append(stack.pop())
                    stack.pop()
                else:
                    if stack.isEmpty():
                        stack.push(value)
                    else:
                        while stack.size() > 0:
                            if prec[stack.peek()] >= prec[value]:
                                expressionList.append(stack.pop())
                            else:
                                break
                        stack.push(value)
        while not stack.isEmpty():
            expressionList.append(stack.pop())
        return expressionList

    def CalculationPostfix(self,expressionList):
        stack = Stack()
        
        for value in expressionList:
            try:
                #숫자일 경우 스택에 push
                value = float(value)
                stack.push(value)
            except:
                # 그 외 연산자 처리
                if value == '+':
                    number1 = stack.pop()
                    number2 = stack.pop()
                    stack.push(number2+number1)
                elif value == '-':
                    number1 = stack.pop()
                    number2 = stack.pop()
                    stack.push(number2-number1)
                elif value == '*':
                    number1 = stack.pop()
                    number2 = stack.pop()
                    stack.push(number2*number1)
                elif value == '/':
                    number1 = stack.pop()
                    number2 = stack.pop()
                    stack.push(int(number2/number1))
        return stack.pop()


def processing(expression):
    Cal = Calculation()
    infix = Cal.splitExpression(expression)#계산식 array로 분리
    postfix = Cal.infixToPostfix(infix) #계산식을 후위표현식으로 변경
    result = Cal.CalculationPostfix(postfix)# 후위표현식 계산
    result = ("%g" % result)
    return result