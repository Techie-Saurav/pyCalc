#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#imports
import sys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#variables
expression = ""
prompt = ""
temp = None                         #no fixed use, i'll use it multiple times

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#define functions
def checkCorrectness():
    global expression

    if expression[:1].isdigit() == False or expression[-1:].isdigit() == False:
        sys.exit("The expression starts or ends with an invalid character.")

    if "=" in expression:

        print()
        print("'=' detected in the expression.")
        print("I can skip the RHS, and evaluate the LHS. In this case, input 1. I'll do this by default.")
        print("Alternatively, I can ignore the '='(in case of a typo), and evaluate the string as is. In this case, input 2.")
        print()

        prompt = input("What is your answer? ").strip()
        
        if prompt.strip() == "2":
            expression = expression.replace("=","")
        else:
            expression = expression.split("=")[0]

def solve():
    global expression
    expression = eval(expression)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#da schtuff de actual
expression = input("Enter the expression that is to be evaluated: ")

checkCorrectness()
solve()
print(expression)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~