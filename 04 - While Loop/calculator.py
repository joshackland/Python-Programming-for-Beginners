while True:
    print('Type "exit" to quit the program')

    firstNum = input('Enter the first number: ')
    if firstNum == 'exit':
        break
    firstNum = int(firstNum)

    operator = input('Addition (+), Subtraction(-), Multiplication (*), Division (/)')
    if operator == 'exit':
        break

    secondNum = input('Enter the second number: ')
    if secondNum == 'exit':
        break
    secondNum = int(secondNum)

    output = f'{str(firstNum)} {operator} {secondNum} = '

    if operator == '+':
        print(output + str(firstNum + secondNum))
    elif operator == '-':
        print(output + str(firstNum - secondNum))
    elif operator == '*':
        print(output + str(firstNum * secondNum))
    elif operator == '/':
        print(output + str(firstNum / secondNum))