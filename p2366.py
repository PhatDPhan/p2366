# Phat Phan
# La Salle University, CSC366, Spring 2018
# Infix to Postfix
# https://www.python.org/downloads/
# The project is written on Python 3 version

import sys
import string
# re class is the regex class that help dealing with variables that contain 2 or more letter for example a1, a2, or omg
import re

# The advantage of python 3 is that when it breaks the in put into token. each token will automatically seperate by blank space.
# for example A1 + 6 will give A1 6 +

# The diadvantage is when users input without anyspace. there will be error. For example, a+5, a+ 5 because when
# it splits the input, it will see a+5 or a+ as a whole token

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
    
    #create a stack to hole the left parentthesis and all operations +-*/%^ 
    operation = Stack()
	
    #create the array that holds postfix output
    postfixList = []
    
    #array to hold breaking down input as tokens
    tokenList = userInput.split()

    # loop throught each token
    # check if each token is a variable, number, letter, or left-right parentthesis
    # when it sees a  right parentthesis meaning the end of a expression(it may a small expression inside a bigger epression)
    # it will pop  everything in the operation stack to the postfixList
    for token in tokenList:
        if re.search('[a-zA-Z]', token) or token in str(list(range(10000))):
            postfixList.append(token)
        elif token == '(':
            operation.push(token)
        elif token == ')':
            topToken = operation.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = operation.pop()
        else:
            while (not operation.isEmpty()) and \
               (prec[operation.peek()] >= prec[token]):
                  postfixList.append(operation.pop())
            operation.push(token)

    while not operation.isEmpty():
        postfixList.append(operation.pop())
    return " ".join(postfixList)

# Postfix evaluation method, if the expressions contain just number
# it will calculate output
def postfixEval(postfixExpr):
    # create stack to hold all arimitic operations
    operandStack = Stack()
    # postfixExpr is the result of inFixtoPostfix method
    tokenList = postfixExpr.split()

    # Loop through the list
    for token in tokenList:
        if token in str(list(range(19998))):
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
