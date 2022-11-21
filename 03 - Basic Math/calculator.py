firstNum = float(input('Enter the first number: '))

operator = input('Addition (+), Subtraction(-), Multiplication (*), Division (/)')

secondNum = float(input('Enter the second number: '))

output = f'{str(firstNum)} {operator} {secondNum} = '

if operator == '+':
    print(output + str(firstNum + secondNum))
elif operator == '-':
    print(output + str(firstNum - secondNum))
elif operator == '*':
    print(output + str(firstNum * secondNum))
elif operator == '/':
    print(output + str(firstNum / secondNum))