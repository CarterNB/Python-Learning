# EX 1
# print('hello world!')
# EX 2
# var1 = 15.2
# var2 = 11.3

# sum = var1+ var2

# print('sum of {0} and {1} is {2}'. format(var1, var2, sum))
# EX 3
# num = float(input('Enter a number to find the square root of it'))

# numSq = num **0.5
# print('The square root of %0.2f is %0.2f'%(num,numSq))

# EX 4
'''
a = 5
b = 6
c = 9
s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print('The area of the triangle is %0.3f' % (area))
'''

# EX 5
'''
import cmath
a = 4
b = 6.2
c = 1
d=b*b-4*a*c
sol1 = (-b+cmath.sqrt(d))/(2*a)
sol2 = (-b-cmath.sqrt(d))/(2*a)

print('The two solutions are {0} and {1}'.format(sol1,sol2))
'''

# EX 6
'''
x=5
y=6

print('the values of x and y are currently {0} and {1}'.format(x,y))

temp = x
x=y
y=temp

print('the values of x and y are now {0} and {0}'.format(x,y))
'''

# EX 7
'''
import random

print(random.randint(0,100))
'''

# EX 8
'''
cFactor=1.609
kilo=float(input('Enter the distance in kilometers'))

mile=kilo*cFactor

print('The distance of %0.3f km is equivalent to %0.3f miles'%(kilo,mile))
'''

# EX 9
'''
cel=float(input('Insert temperature in celsius to convert to fahrenheit: '))

far = cel * 1.8 + 32

print('%0.3f Celsius is equivalent to %0.3f fahrenheit'%(cel,far))

'''

# EX 10
'''
num=float(input('Enter a number to check if it is positive, negative or 0: '))

if num > 0:
    print('num is a positive number')
if num < 0:
    print('num is a negative number')
if num ==0:
    print('num is zero')


if num>=0:
    if num==0:
        print('num is zero')
    else:
        print('num is positive')
else:
    print('num is negative')
'''

# EX 11
'''
num=int(input('Enter a number to find out if it is odd or even: '))

check=num % 2

if check==0:
    print('number is even')
else:
    print('number is odd')
'''

# EX 12
'''
year = int(input('Enter a year to find out if it is a leap year: '))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print('{0} is not a leap year'.format(year))
'''

# EX 13
'''
num1 = 9
num2 = 7
num3 = 2

if num1>num2 and num1>num3:
    print("number 1 {0} is the largest number".format(num1))
elif num2>num1 and num2>num3:
    print("number 2 of {0} is the largest number".format(num2))
else:
    print("number 3 of {0} is the largest number".format(num3))
'''

# EX 14
'''
num=int(input('Input number to find out if it is prime: '))

flag = 0
if num == 1:
    print(num,'is not a prime number')
elif num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            flag = 1
            break

    if flag:
        print(num, 'is not a prime number')
    else:
        print(num, 'is a prime number')
'''

# EX 15
'''
lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are: ")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
'''

# EX 16
'''
num=int(input('Enter a number to see value of the factorial: '))
sol=1
if num < 0:
    print("negative numbers cannot have factorials")
elif num ==0:
    print("The factorial of zero is 1")
else:
    for i in range(1,num+1):
        sol = sol*i
    print('The factorial of {0} is {1}'.format(num, sol))
'''

# EX 17
'''
num=int(input("Enter a number to see the multiplication table for that number: "))

for i in range(1, num+1):
    mul=i*num
    print(num, 'x',i,'=',mul)
'''

# EX 18
'''
nterms=100
n1=0
n2=1
count=0
while count<nterms:
    print(n1)
    nth=n1+n2
    n2=n1
    n1=nth
    count+=1
'''

# EX 19
'''
num=407

order=len(str(num))
sum=0;

temp=num

while temp > 0:
    digit = temp % 10
    sum +=digit ** order
    print(digit)
    temp//=10

if num ==sum:
    print(num, "is an Armstrong number")
else:
    print(num, 'is not an Armstrong number')
'''
# EX 20
'''
upper = 20000
lower = 100

for num in range(lower, upper+1):
    temp=num
    order=len(str(num))

    sum = 0
    while temp>0:
        digit=temp % 10
        sum = sum + (digit ** order)
        temp//=10
    if(num==sum):
        print(num, ' is an Armstrong number')
'''
# EX 21
'''
num=int(input("Enter a number to find the sum of all natural numbers below it: "))

sum=0
for i in range(1,num+1):
    sum+=i
print("The sum is {0}".format(sum))
'''

# EX 22
'''
terms = 10

result = list(map(lambda x: 2**x, range(terms)))

print("The total terms are: ", terms)
for i in range(terms):
    print("2 raised to power",i,"is",result[i])
'''

# EX 23
'''
my_list = [12, 65, 54, 39, 102, 339, 221]

result = (list(filter(lambda x: (x % 13 == 0), my_list)))

print(result, "are divisible by 13")
'''

# EX 24
'''
dec = 344

print("The decimal value of",dec,"is: ")
print(bin(dec), "in binary.")
print(hex(dec),"in hexadecimal")
print(oct(dec),"in octal")
'''

# EX 25
'''
val = int(1222)

print("The ASCII value of '",val,"'is", chr(val))

for i in range(1000,1100+1):
    print("The ASCII character for ",i,"is",chr(i))
'''

# EX 26
'''
def computeHCF(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if ((x %i==0) and (y%i==0)):
            hcf = i
    return hcf

num1=628
num2=932

print("The HCF is ", computeHCF(num1,num2))
'''

# EX 27
'''
def computeHCF(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if ((x %i==0) and (y%i==0)):
            hcf = i
    return hcf

def computeLCM(x,y):
    LCM=(abs(x*y))/computeHCF(x,y)
    return LCM

num1=54
num2=24

print("The lowest common multiple of ",num1,"and",num2,"is",computeLCM(num1,num2))
'''

# EX 28
'''
def print_factors(x):
    for i in range(1,x+1):
     if x%i==0:
         print(i)
num=320

print_factors(num)
'''

# EX 29
'''
def add(x,y):
    sol=x+y
    return sol

def subtract(x,y):
    sol=x-y
    return sol

def divide(x,y):
    sol=x/y
    return sol

def multiply(x,y):
    sol=x*y
    return sol

print("Select Desired Operation.")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")

while True:
    choice = input("Enter Choice (1,2,3,4)")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
        except ValueError:
            print("Invalid Input. PLease Enter a Number.")
            continue
        if choice == '1':
            print(add(num1, num2))
        elif choice == '2':
            print(subtract(num1, num2))
        elif choice == '3':
            print(divide(num1, num2))
        elif choice == '4':
            print(multiply(num1, num2))

    more = input("Would you like to do another calculation? (yes/no): ")
    if more == 'no':
        break
else:
    print("Invalid Input")
'''

# EX 30
'''
import itertools, random

deck=list(itertools.product(range(1,14),['Spade','Heart','Club','Diamond']))

random.shuffle(deck)

print("You got: ")
for i in range(2):
    print(deck[i][0], "of", deck[i][1])
'''

# EX 31
'''
import calendar

yy=2023
mm=1

print(calendar.month(yy,mm))
'''

# EX 32
'''
def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))

nterms=15

if nterms<=0:
    print("please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(fibo(i))
'''

# EX 33

'''
def recur_add(n):
    if n<=1:
        return n
    else:
        return(n+recur_add(n-1))

num = 16

if num<0:
    print("Enter a positive number")
else:
    print("The sum is",recur_add(num))
'''

# EX 34
'''
def recur_fac(n):
    if n==1:
        return(n)
    else:
        return(n*recur_fac(n-1))

num=7

if num<0:
    print("A factorial must be a positive integer")
elif num==0:
    print("The factorial of zero is one")
else:
    print("The factorial of",num,"is",recur_fac(num))
'''

# EX 35
'''
def convertToBinary(n):
    if n>1:
        convertToBinary(n//2)
    print(n%2,end='')

dec=34

convertToBinary(dec)
print()
'''

# EX 36
'''
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(X)):
    for j in range(len(Y)):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)
'''

# EX 37
'''
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)
'''

# EX 38
'''

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)
'''

# EX 39
'''
my_str = 'aIbohPhoBiA'

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")
'''

# EX 40
'''
# define punctuation
punctuations = "!()-[]{};:""\,<>./?@#$%^&*_~"

my_str = "Hello!!!, he said---- and went."

no_punct=""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

print(no_punct)
'''

# EX 41
'''
my_str = "Hello this Is an Example With cased letters"

words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are: ")
for word in words:
    print(word)
'''

# EX 42
'''
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};

print("Union of E and N is",E|N)

print("Intersection of E and N is", E&N)

print("Difference of E and N is",E-N)

print("Symmetric difference of E and N is",E^N)
'''

# EX 43
'''
vowels = 'aeiou'
ip_str = 'Hello, have you tried our tutorial section yet?'

ip_str = ip_str.casefold()

count={}.fromkeys(vowels,0)

for char in ip_str:
    if char in count:
        count[char] += 1
print(count)
'''

# EX 44

# EX 45
'''
def jpeg_res(task_4_measurements):
    with open(task_4_measurements,'rb') as img_file:
        img_file.seek(163)

        a = img_file.read(2)

        height = (a[0] << 8) + a[1]

        a = img_file.read(2)

        width = (a[0] << 8) + a[1]

    print("The resolution of the image is", width,"x",height)
jpeg_res("task_4_measurements.jpg")
'''

# EX 46

# EX 47
'''
count=0
rows = 5
for i in range(rows):
    count = count+1
    for j in range(count):
        print('* ',end="")
    print('\n')

count = rows
for i in range(rows):
    count += -1
    for j in range(count):
        print('* ',end="")
    print('\n')

rows = 6
count=0
for i in range(rows):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")
'''
'''
rows = 5
ascii_val=65

for i in range(rows):

    for j in range(i+1):
        alpha=chr(ascii_val)
        print(alpha,end=" ")
    ascii_val += 1
    print('\n')
'''

# EX 48
'''
dic_1 = {1: 'a', 2: 'b'}
dic_2 = {2: 'c', 4: 'd'}

print(dic_1|dic_2)
'''

# EX 49

# EX 50
'''
my_list = [21, 44, 54, 32, 11]

for index, val in enumerate(my_list, start=1):
    print(index,val)
'''

# EX 51
'''
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)
'''
# EX 52
'''
my_list = [1, 2, 3, 4, 5]

print(my_list[1:4:2])
'''

# EX 53
'''
dict = {'a':'juice','b':'grill','c':'corn'}

for key in dict.items():
    print(key,value)

for key in dict:
    print(key, dict[key])
'''

# EX 54
'''
dt = {5:4, 1:6, 6:3}

sorted_dict = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}

print(sorted_dict)
'''

# EX 55
'''
import random

val = (random.randint(0, 1))

if val ==1:
    my_list=[1]
else:
    my_list=[]

if not my_list:
    print("The list is empty")
else:
    print("THe list is not empty")
'''

# EX 56
'''
string = input()

try:
    num = int(input())
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)
'''

# EX 57

# EX 58
'''
list_1 = [1,'a','b']
list_2 = [3,4,7,1]

list_con = list_1 + list_2
print(list_con)
'''
'''
list_1 = [1,'a','b']
list_2 = [3,4,7,1]

list_con = [*list_1, *list_2]
print(list_con)
'''

# EX 59
'''
my_dict = {1: 'a', 2: 'b', 3: 'c'}

if 4 in my_dict:
    print("present")
else:
    print("absent")
'''

# EX 60
'''
def split(list_a, chunk_size):

    for  i in range (0, len(list_a), chunk_size):
        yield list_a[i:i+chunk_size]

chunk_size = 4
my_list = [1,2,3,4,5,6,7,8,9,0]
print(list(split(my_list,chunk_size)))
'''

# EX 61
'''
balance_str = "1500"
balance_int = (balance_str)

print(type(balance_int))

print(balance_int)
'''

# EX 62
'''
print('\033[38;2;5;243;2m' + 'This text is colourful' + '\033[0m')
#\033 is code used to call a function
#38;2;r;g;b is used to call the rgb colour code of the text
#m is the function name
'''

# EX 63
'''
from datetime import datetime

my_date_str = 'Mar 13 2023 6:11PM'

datetime_obj = datetime.strptime(my_date_str, '%b %d %Y %I:%M%p')

print(type(datetime_obj))
print(datetime_obj)
'''

# EX 64
'''
#Get second last obj from a list
my_list = ['a','b','c','d','e']

print(my_list[-2])
'''

# EX 65
'''
my_str = 'I love python.'

print(my_str[2:6])

print(my_str[7:])

print(my_str[:-1])
'''

# EX 66
'''
print("Python")

print("is easy to learn.")

print()

print("Python", end=" ")
print("is easy to learn")
'''

# EX 68
'''
import random

my_list = [1, 'a', 32, 'c','d',555]
print(random.choice(my_list))
'''

# EX 69
'''
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
print(isfloat('s12'))
print(isfloat("1.123"))
print(isfloat('10'))
'''

# EX 70
'''
this_list = ['a',1,'a',4,3,2,'a'].count('a')
print(this_list)
'''

# EX 72
'''
my_dict = {31: 'a', 21: 'b', 13: 'c'}

del my_dict[31]
print(my_dict.pop(21)) #Prints value of dictionary that is popped
print(my_dict)
'''

# EX 73

'''
my_str='''
# This is a way
# to print multi line
# code in python
'''
my_str = ("This is a way \n"
"to print multi line\n"
"code in python.")

print(my_str)
'''

# EX 75
'''
import time

start = time.time()
i=100000
for x in range(i):
    print(x*x*x)


end = time.time()
print(end-start,"seconds")
'''

# EX 76
'''
class Vehicle:
    def name(self,name):
        return name
v = Vehicle()
print(v.__class__.__name__)
'''

# EX 77

'''
index = [1,2,3]
languages = ['python','c','java']
dictionary =dict(zip(index,languages))
print(dictionary)
'''

# EX 79
'''
my_str = "   python   "
print(my_str)
print(my_str.strip())
'''

# EX 81
'''
from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3

print(Day.MONDAY)
print(Day.MONDAY.name)
print(Day.MONDAY.value)
'''

# EX 82
'''
def name():
    return "JOHN","ARMIN"

print(name())

name1,name2=name()
print(name1,name2)
'''
'''

def name():
    n1="JOHN"
    n2="ARMIN"
    return {1:n1,2:n2}
names=(name())
print(names)
'''

# EX 86
'''
import pathlib

print(pathlib.Path("test.py").parent.absolute())

print(pathlib.Path().absolute())
'''

# EX 87
'''
list1=[1,2,3,4]
list2=['a','b','c','d']

for i,j in zip(list1,list2):
    print(i,j)
'''

# EX 89
'''
num=5551234
reversed_num=0

while num!=0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num//=10

print("reversed number: " + str(reversed_num))
'''

# EX 90
'''
base = 4
exponent = 4

result = 1

while exponent !=0:
    result *= base
    exponent-=1

print("Answer = " + str(result))
'''

# EX 91
'''
number = 56127
count =0

while number != 0:
    number//=10
    count+=1

print("number of digits is", count)
'''

# EX 92
'''
str1 = "Race"
str2 = "Care"

str1_l=str1.lower()
str2_l=str2.lower()

if len(str1_l)==len(str2_l):
    sort_s1=sorted(str1_l)
    sort_s2=sorted(str2_l)

    if sort_s1==sort_s2:
        print(str1 +" and "+ str2 + " are anagrams")
    else:
        print(str1 +" and "+ str2 + " are not anagrams")
else:
    print(str1 +" and "+ str2 + " are not anagrams")
'''

# EX 93
'''
str1="this is a string"

str2=str1[0].upper() +str1[1:]

print(str2)
'''

# EX 94
'''
def get_permutations(string, i=0):
    if i == len(string):
        print("".join(string))
    for j in range(i, len(string)):
        words = [c for c in string]
        words[i], words[j] = words[j], words[i]

        get_permutations(words, i + 1)


print(get_permutations("pog"))
'''

# EX 95
'''
import time


def countdown(time_s):
    while time_s:
        mins, secs = divmod(time_s, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_s -= 1

    print("stop")


countdown(5)
'''

# EX 96
'''
count = 0
countt = 0
str1 = "StringusPingus"
char1 = "u"

i = 0

for x in range(i, len(str1)):
    if char1 == str1[x]:
        count += 1

for i in str1:
    if i == char1:
        countt += 1

print(countt)
'''

# EX 97
'''
list1 = [1, 5, 3, 5, 7, 5, 2, 9]

print((list(set(list1))))

# Sets cannot contain duplicate entries so turning a list into a set is a good way to remove duplicates
'''

# EX 98

print(b'Easy \xE2\x9C\x85'.decode("utf-8"))
