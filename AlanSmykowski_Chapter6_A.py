#This program validates the format of the user's input prompt

import re


#Function to validate phone numbers
def validatePhone(phone):

    #Phone Number: (123) 456-7890 or 123-456-7890
    pattern = r'^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$'

    return re.match(pattern, phone) is not None


#Function to validate social security numbers
def validateSsn(ssn):

    #SSN: 123-45-6789
    pattern = r'^\d{3}-\d{2}-\d{4}$'

    return re.match(pattern, ssn) is not None


#Function to validate zip codes
def validateZip(zipCode):

    #Zip Code: 12345 or 12345-6789
    pattern = r'^\d{5}(-\d{4})?$'

    return re.match(pattern, zipCode) is not None


#Function to determine the type of input
def determineInputType(userInput):

    if validatePhone(userInput):
        return "Phone Number"

    elif validateSsn(userInput):
        return "Social Security Number"

    elif validateZip(userInput):
        return "Zip Code"

    else:
        return "invalid"


#Re-execute the program
def reDo(answer):

    if answer == "y":
        print("Continuing instance.\n\n")
        main()

    else:
        print("Program exit.")

    return


#Main function for user input
def main():

    #Choose user input method
    print("This program will validate the following upon input: Phone Number, SSN, Zip Code.\n")
    print("Choose your input method:")
    print("1. All three, One by one - Input all three, each after another as prompted.")
    print("2. One, Detect and validate - Input either one of the three and it will be validated automatically.")

    userInput = int(input("\nInput Method (1 or 2): "))

    #Use input method one
    if userInput == 1:
        print("\nOne by one.")
        Phone = input("\nPhone Number: ")
        SSN = input("Social Security Number: ")
        Zip = input("Zip Code: ")

        #Display results
        if validatePhone(Phone):
            print("\nPhone Number valid.\n")
        else:
            print("\nPhone Number invalid!")
            print("Ensure your Phone Number is in this format: (123) 456-7890 or 123-456-7890\n")

        if validateSsn(SSN):
            print("SSN valid.\n")
        else:
            print("SSN invalid!")
            print("Ensure your SSN is in this format: 123-45-6789\n")

        if validateZip(Zip):
            print("Zip Code valid.")
        else:
            print("Zip Code invalid!")
            print("Ensure your Zip Code is in this format: 12345 or 12345-6789")

    #Use input method two
    else:
        print("\nDetection and validation.")
        userInput = input("Enter either a Phone Number, Social Security Number, or Zip Code: ")

        inputType = determineInputType(userInput)

        #Display results
        if inputType == "invalid":
            print("\nThe input is not a valid Phone Number, Social Security Number, or Zip Code.")
            print("\nFor proper formatting, refer to this guide:")
            print("Phone Number format: (123) 456-7890 or 123-456-7890")
            print("SSN format: 123-45-6789")
            print("Zip Code format: 12345 or 12345-6789")

        else:
            print(f"\nThe input is a valid {inputType}.")

    reDo(input("\nWould you like to validate another? (y or n): "))


#Main call
if __name__ == "__main__":
    main()
