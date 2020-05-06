"""
CTEC 121
<Garrett>
<Mod 3 Lab 2>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    try:
        print(4/0)
    except ZeroDivisionError:
        print("\nThere was a divide by zero error. Exiting program.\n")
        exit
    except:
        print("Unknown Exception")
        exit

main()    