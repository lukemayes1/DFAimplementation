# ------------------------------------------------------------------ #
# Luke Mayes                                                         # 
# April 28, 2022                                                     #
#                                                                    #
# DFA Implementaion - Determines if a input string is accepted or    #
# rejected by a DFA. The DFA is defined in a .txt file that is       #
# provided by the user.                                              #
# ------------------------------------------------------------------ #


def readFileData():
    # Variables
    contents = []
    i = 0

    # Prompt user for file name and open file
    fileInput = input("Input file: ")

    # Open file and calculate line count
    file = open(fileInput, "r")
    lineCount = len(open(fileInput, "r").readlines(  ))
    
    # Read and process lines
    while i < lineCount:
        line = file.readline().partition(';')[0].strip("\t").replace(" ", "")
        contents.append(line)
        i = i + 1
    
    return contents

def nextState(state, charcter, contents, alphabet):
    # Find next state based off currState and currChar
    if charcter == alphabet[0]: # a
        next = int(contents[state][0])
    elif charcter == alphabet[1]: # b
        next = int(contents[state][1])
    return next


# Variables
contents = readFileData()
alphabet = contents.pop(0)
numStates = contents.pop(0)
acceptState = int(contents.pop(-1))
numCharsRead = 0

# Prompt user for input
inputStr = input("Input a string: ")

# Loop through input string
while numCharsRead != len(inputStr):
    currState = 0

    # Display information about DFA from file
    print("\nDFA Information")
    print("------------------------")
    print("The alphabet is " + alphabet)
    print("There are " + numStates + " states")
    print("The accept state is q" + str(acceptState))

    # Process input string
    print("\nDFA Steps Taken")
    print("--------------------------------------------")
    for i in range(len(inputStr)):
        print("Current state = " + str(currState) + " Current input char = " + inputStr[i])
        currState = nextState(currState, inputStr[i], contents, alphabet)
        numCharsRead = numCharsRead + 1

    # Determine if string is accepted or rejected
    if currState == acceptState:
        print("Current state = " + str(currState) + " String " + inputStr + " is accepted")
    else:
        print("Current state = " + str(currState) + " String " + inputStr + " is rejected")

    # Reset and ask user for another input 
    numCharsRead = 0
    inputStr = input("\n-----------------------------------------"\
                      "----------------------------------------"\
                      "-----------------\n\nInput another string: ")
    