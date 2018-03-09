# Phat Phan
# La Salle University, CSC366, Spring 2018
# Infix to Postfix
#https://www.python.org/downloads/release/python-364/

#Define class stack that has 6 methods. we will use push and pop
#Their others 4 are used for checking
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
def infixToPostfix(infixexpr):
    prec = {}
    prec["^"] = 3
    prec["%"] = 2
    prec["*"] = 2
    prec["/"] = 2
    prec["+"] = 1
    prec["-"] = 1
    prec["("] = 0
    
	#create a stack name 
    lexeme = Stack()
	
	#create the array that like the lexeme array 
    postfixList = []
	#array to hold breaking down input as tokens
    tokenList = infixexpr.split()

	# if the token is 
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            lexeme.push(token)
        elif token == ')':
            topToken = lexeme.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = lexeme.pop()
        else:
            while (not lexeme.isEmpty()) and \
               (prec[lexeme.peek()] >= prec[token]):
                  postfixList.append(lexeme.pop())
            lexeme.push(token)

    while not lexeme.isEmpty():
        postfixList.append(lexeme.pop())
    return " ".join(postfixList)





def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

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










#read user input. Then break it into single chracter in tokenList
expression = input('Please enter your expression!\n')
print(infixToPostfix("( A + D * F ) ^ 2 + C - ( O - P )"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


print(infixToPostfix(expression))


c=True
check = expression.split()
for char in check:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        c=False


if c:
    print(postfixEval(infixToPostfix(expression)))
else:
    print(infixToPostfix(expression))
