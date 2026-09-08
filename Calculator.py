import math

def add (num1, num2):
    sum= num1 + num2
    print (sum)

def subtraction (num1, num2):
    sub= num1 - num2
    print (sub)

def multiplication (num1, num2):
    multiple = num1 + num2
    print (multiple)

def division (num1, num2):
    divide = num1/num2
    print (divide)

def exponent (num1, num2):
    power = num1**num2
    print (power)

loop = True

while loop:


    num1 = int(input())
    action = input()
    num2 = int(input())

    if action == '+':
        add (num1, num2)

    if action == '-':
        subtraction (num1, num2)
    print (subtraction)

    if action == '*':
        multiplication (num1, num2)

    if action == '/':
        division (num1, num2)

    if action == '**':
        exponent (num1, num2)

