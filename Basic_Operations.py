flag=1

while flag != 0:
    num1=int(input('input first number: '))
    num2=int(input('input second number: '))
    op=input("Input operation (+,-,*,/): ")

    if op == '+':
        sum = num1 + num2
        print('sum of',num1,'and',num2,'is',sum)
    elif op == '-':
        diff = num1 - num2
        print('differnce of',num1,'and',num2,'is',diff)
    elif op =='*':
        prod = num1 * num2
        print('product of',num1,'and',num2,'is',prod)
    elif op == '/':
        quot = num1/num2
        print('quotient of',num1, 'and',num2,'is',quot)

    flag=input('Enter 1 if you would like to do another operation if not, enter 0 to end.')
