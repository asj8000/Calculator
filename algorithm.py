def isInteger(value):
    if value[0] == ('-', '+'):
        return value[1:].isdigit()
    else:
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
        expressionArray = []
        number = 0
        isNumber = False

        expression = expression.replace(" ","")
        
        for value in expression:
            try:
                value = int(value)
                Number = Number * 10 + int(value)
                isNumber = True
            except:
                if isNumber:
                    expressionArray.append(number)
                    number = 0
                isNumber = False
                expressionArray.append(value)        
        return expressionArray

    def infixToPostfix(self,expression):
        stack = Stack()
        expressionArray = []
        prec = { '*' : 3, '/' : 3, '+' : 2, '-' : 2, '(' : 1 }
        
        for value in expression:
            try:
                #숫자일 경우 입력
                value = int(value)
                expressionArray.append(value)
            except:
                #시작 괄호일 경우 입력
                if value == '(':
                    stack.push(value)
                #종료 괄호일 경우 입력
                elif value == ')':
                    while stack.peek() != '(':
                        expressionArray.append(stack.pop())
                    stack.pop()
                else:
                    if stack.isEmpty():
                        stack.push(value)
                    else:
                        while stack.size() > 0:
                            if prec[stack.peek()] >= prec[value]:
                                expressionArray.append(stack.pop())
                            else:
                                break
                        stack.push(value)
        while not stack.isEmpty():
            expressionArray.append(stack.pop())
        return expressionArray

    def CalculationPostfix(self,expressionArray):
        stack = Stack()
        
        for value in expressionArray:
            try:
                #숫자일 경우 스택에 push
                value = int(value)
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
    tokens = Cal.splitExpression(expression)#계산식 array로 분리
    postfix = Cal.infixToPostfix(tokens) #계산식을 후위표현식으로 변경
    val = Cal.CalculationPostfix(postfix)# 후위표현식 계산
    return val
