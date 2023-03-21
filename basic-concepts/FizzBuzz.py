num=int(input("Enter your number: "))
def fizzbuzz(num):
    if num%3 ==0:
        if num%5==0:
            return 'FizzBuzz'
        return 'Fizz'
    elif num%5 == 0:
        return 'Buzz'
    else:
        return num

print(fizzbuzz(num))
