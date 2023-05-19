#calculator 1/2 - Create a simple calculator include defensive programming

while True:
    try:
        #User input of equation
        input_1 = float(input('Please enter the first number: '))
        input_2 = float(input('Please enter the second number: '))
        operator = input('Please input the operation you would like to perform on the numbers (+, -, *, /): ')

        #perform calculation
        if operator == '+':
            result = input_1 + input_2
        elif operator == '-':
            result = input_1 - input_2
        elif operator == '*':
            result = input_1 * input_2
        elif operator == '/':
            if input_2 == 0:
                print('Division by zero is not allowed.')
                continue #jump back to operator input if division by zero
            else:
                result = input_1 / input_2
        else:
            print('The operator you entered is invalid.')
            continue #jump back to operator input if invalid operator

        #display result
        print(f'The result of {input_1} {operator} {input_2} is {result}.')

        #write equation to a text file if operator is valid
        with open('equation.txt', 'a') as f:
            f.write(f'{input_1} {operator} {input_2} = {result} \n')     #\n to add new line

        #ask if user wants to continue
        while True:
            continue_calculation = input('Do you want to continue? (Yes/No): ').lower()
            if continue_calculation == 'yes':
                break
            elif continue_calculation == 'no':
                print('Thank you for using the calculator. Bye Bye!')
                exit()
            else:
                print('Invalid input. Please enter Yes or No.')
    except ValueError:
        print('Please enter valid input.')
        continue #jump back to first input if invalid input
