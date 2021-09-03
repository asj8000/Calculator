def splitExpression(expression):
    expressionArray = []
    number = 0
    isNumber = False
    #공백 제거
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

print(splitExpression("2+3"))



'''
'''