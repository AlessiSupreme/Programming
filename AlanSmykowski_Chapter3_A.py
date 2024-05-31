#This program asks the user for expenses and their types and outputs the sum, max and min
#This one was really educational and fun to make, so I added a bunch of useful features

import functools


#Add function for the reduce method
def addFunc(a, b):
    return a + b


#Calculations
def calculateTotal(fullList, inputType, expenseType):

    #Sum of expenses
    sumItem = functools.reduce(addFunc, fullList)

    #Smallest expense
    minItem = min(fullList)
    minIndex = min(range(len(fullList)), key=fullList.__getitem__)

    #Biggest expense
    maxItem = max(fullList)
    maxIndex = max(range(len(fullList)), key=fullList.__getitem__)

    #Output types
    if inputType == 1:
        print("\n\n\nType of expense: " + expenseType)

    else:
        print("\nTypes of expenses present:")
        print(', '.join(expenseType))

    #Output sum
    print("\nThe sum of your expenses is $" + str(sumItem))

    #Output highest and type
    print("\nThe highest of your expenses is $" + str(maxItem))

    if inputType == 2:
        print("Of the type " + str(expenseType[maxIndex]))

    #Output lowest and type
    print("\nThe lowest of your expenses is $" + str(minItem))

    if inputType == 2:
        print("Of the type " + str(expenseType[minIndex]))

    return


#Items are separated by a comma
def commaType():

    #User type string
    print("\nWhat is the type of your expenses?")
    typeStr = str(input("(Enter a string):"))

    # User input string
    print("\nInput your list below.")
    inStr = str(input("(Enter a string):"))

    #Setup
    expensesLength = int(len(inStr)) - 1
    charIndex = 0

    expenseItem = ""
    lastChar = ""
    expensesListed = []

    #Convert input string to a list
    while charIndex <= expensesLength:

        #Add string to list
        if inStr[charIndex] == ',' or inStr[charIndex] == ' ':

            #Flexibility for a comma and space in input
            if lastChar != ',':
                expenseItem = float(expenseItem)
                expensesListed.append(expenseItem)
                expenseItem = ""

        #This will ignore any dollar signs and list brackets
        elif inStr[charIndex] == '$' or inStr[charIndex] == '[' or inStr[charIndex] == ']':
            i = 0

        #Add character to string
        else:
            expenseItem += str(inStr[charIndex])

        lastChar = str(inStr[charIndex])
        charIndex += 1

    #Adds last item to list
    if expenseItem != "":
        expenseItem = float(expenseItem)
        expensesListed.append(expenseItem)
        expenseItem = ""

    return expensesListed, typeStr


#Items are given one by one
def oneByOneType():

    #User input
    print("\nHow many expenses will you input?")
    print("(0 for any amount up to 1000.")
    print("You can enter 'end' at any time in the Expense field to end prompt sequence.")

    #Setup
    expensesAmount = int(input("(Enter a number): "))
    itemIndex = 1

    expensesListed = []
    typesListed = []

    if expensesAmount == 0:
        expensesAmount = 1000

    print("\nFor the following, input both Type and Expense as a string or a float.")

    #Convert input string to a list
    while itemIndex <= expensesAmount:

        typesListed.append(str(input("\nType of expense " + str(itemIndex) + ": ")))

        inStr = str(input("Expense " + str(itemIndex) + ": "))

        if inStr == "end":
            print("List end.")
            return expensesListed

        else:
            #Piece of code to remove any dollar signs
            expenseLength = int(len(inStr)) - 1
            charIndex = 0
            expenseItem = ""

            while charIndex <= expenseLength:

                if inStr[charIndex] == '$':
                  i = 0

                else:
                    expenseItem += str(inStr[charIndex])

                charIndex += 1

            expenseItem = float(expenseItem)
            expensesListed.append(expenseItem)
            expenseItem = ""

            itemIndex += 1

    return expensesListed, typesListed


#Redo the code
def reDo(answer):

    if answer == "y":
        print("Continuing instance.\n\n")
        main()

    else:
        print("Program exit.")

    return


#Main
def main():

    #Ask user for method of input
    print("\nWhich input method will you use?")

    print("\n1. All expenses at once, separated by a comma, a space, or both.")
    print("Choose this if all expenses are of the same type.")
    print("- Example: 50, 60 70, 80$ $90, 100.")
    print("Punctuation and dollar signs are ignored.")

    print("\n2. One by one. Simply press enter after each expense.")
    print("The prompt will repeat for each item.")

    listType = int(input("\n(Enter a number):"))

    #Call for list input
    if listType == 1:
        expenseList, typeList = commaType()
        inputType = 1

    else:
        typeList = []
        expenseList, typeList = oneByOneType()
        inputType = 2

    #Call for calculation
    calculateTotal(expenseList, inputType, typeList)

    #Call for redo
    reDo(input("\nWould you like to redo the process? (y/n): "))

    return


#Main call
if __name__ == "__main__":
    main()