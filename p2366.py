# Phat Phan, Kenvin Sie
# La Salle University, CSC366, Spring 2018
# Project 2: Infix to Postfix
# Dowload link: https://www.python.org/downloads/
# The project is written on Python 3 version

import sys
import string

# re class is the regex class that help dealing with variables that contain 2 or more letter for example a1, a2, 9562 or omg
import re
# Kevin provided a buid in ethod of python that can handle better then regex. they are isalnum() and isdigit()
# However, in the loop to ask users if they want to do another expression, it's simplier with regex

# The advantage of python 3 is that when it breaks the in put into tokens. each token will automatically seperate by blank space.
# for example A1 + 6 will give A1 6 +

# The diadvantage is when users input without anyspace. there will be error. For example, a+5, a+ 5 because when
# it splits the input, it will see a+5 or a+ as a whole token
# Kevin provided fix_space method to handle tokens with or without space

# Define class stack that has 5 methods. we will use push and pop and peak to work on each token
# Their others 4 are used for checking
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    # go back 1 position in the stack
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
       
# method to convert infix to postfix    
def infixToPostfix(userInput):
    prec = {}
    prec["^"] = 3
    prec["%"] = 2
    prec["*"] = 2
    prec["/"] = 2
    prec["+"] = 1
    prec["-"] = 1
    prec["("] = 0
    
    #create a stack to hold the left parentthesis and all operations +-*/%^ and variables
    operation = Stack()
	
    #create the array that holds postfix output
    postfixList = []
    
    #array to hold breaking down input as tokens
    tokenList = fix_spaces(userInput).split()

    # loop throught each token
    # check if each token is a variable, number, letter, or left-right parentthesis
    # when it sees a  right parentthesis meaning the end of an expression(it may a small expression inside a bigger epression)
    # it will pop  everything in the operation stack to the postfixList
    for token in tokenList:
        if token.isalnum():
            postfixList.append(token)
        elif token == '(':
            operation.push(token)
        elif token == ')':
            topToken = operation.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = operation.pop()
        else:
            while (not operation.isEmpty()) and (prec[operation.peek()] >= prec[token]):
                postfixList.append(operation.pop())
            operation.push(token)
    #pop out everything in the operation stack
    while not operation.isEmpty():
        postfixList.append(operation.pop())
    return " ".join(postfixList)

# Postfix evaluation method, if the expressions contain just number
# it will calculate output
def postfixEval(postfixExpr):
    # create stack to hold all arimitic operations and number
    operandStack = Stack()
    # postfixExpr is the result of inFixtoPostfix method
    tokenList = postfixExpr.split()

    # Loop through the list
    # it checks 3 tokens from left to right at a time
    # for example 6 3 + 6 - meaning 6 + 3 = 9 then 9 - 6 = 3
    for token in tokenList:
        if token.isdigit():
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

# method to calculate the posfix
def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "%":
        return op1 % op2
    elif op == "^":
        return op1 ** op2
    else:
        return op1 - op2


# Kenvin gave a great method: strip spaces out and replace them with ones we want
def fix_spaces(string):
    precedence = ["^", "%", "*", "/", "+", "-", "(", ")"]

    temp = string.replace(" ", "")

    for tok in temp:
        if tok in precedence:
            temp = temp.replace(tok, " " + tok + " ")
    return temp


# This is the main method that will call other method
def main():
    # A loop to ask user if they want to continue or not
    while True:
# Read user input
        expression = input('Please enter your expression!\n')

# Check if input contain just characters, number, or both
# If input contain just characters or both characters and number,
# then use infixtoposstfix method without evaluation
# If the input contain just number then evaluate it.

        c=True
        check = expression.split()
        for char in check:
            if re.search('[a-zA-Z]', char):
                c=False

        if c:
            print("This is the Postfix:")
            print(infixToPostfix(expression))
            print("This is the evaluation result:")
            print(postfixEval(infixToPostfix(expression)))
        else:
            print("This is the Postfix:")
            print(infixToPostfix(expression))

# Ask user if they want to continue        
        again = input("\nDo you want to continue?  Y/N\n").lower()
        if again == "y":
            continue
        else:
            break 
    sys.exit()

if  __name__ =='__main__':
    main()
