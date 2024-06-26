#This program allows you to enter student grades and store them in grades.csv

import csv
import os


#Write student grades to a CSV file
def writeGradesToFile():

    clearNow = 0

    try:

        studentCount = int(input("Enter the number of students: "))

        clearGradesFile(2)

        with open('grades.csv', 'w', newline='') as file:

            writer = csv.writer(file)

            writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

            for _ in range(studentCount):

                try:

                    firstName = input("First name: ")

                    lastName = input("Last name: ")

                    exam1 = int(input("Grade for Exam 1: "))

                    exam2 = int(input("Grade for Exam 2: "))

                    exam3 = int(input("Grade for Exam 3: "))

                    writer.writerow([firstName, lastName, exam1, exam2, exam3])

                    print("Grades have been written to grades.csv.")

                except:

                    clearNow = 1

                    print("Invalid input. The file will be cleared.")

    except:
        print("You were supposed to enter a number. No changes were made.")

    if clearNow == 1:

        clearGradesFile(2)


#Read and display the contents of the CSV file
def readGradesFromFile():

    print("")

    with open('grades.csv', 'r') as file:

        reader = csv.reader(file)

        for row in reader:

            print('\t'.join(row))


#Clear the contents of the CSV file
def clearGradesFile(clearType):

    with open('grades.csv', 'w'):
        pass

    if clearType == 1:
        print("The contents of grades.csv have been cleared.")


#Re-execute the program
def reDo(answer):

    if answer == "y":

        print("Continuing instance.\n")

        main()

    else:
        print("Program exit.")

    return


#Main
def main():

    print("You'll be entering student grades in this program session.")

    if os.path.exists('grades.csv'):

        if os.path.getsize('grades.csv') == 0:

            print("Detected an empty grades.csv file. You will write to this file.\n")

            writeGradesToFile()

            readGradesFromFile()

        else:

            print("\nDetected existing grades.csv file.")
            print("What would you like to do?")
            print("\n1. Overwrite file.")
            print("2. Display contents of the file.")
            print("3. Clear the file.")

            action = int(input("\nSelect an action: "))

            if action == 1:

                writeGradesToFile()

            elif action == 2:

                readGradesFromFile()

            elif action == 3:

                clearGradesFile(1)

            else:
                print("Invalid selection.")

    else:

        writeGradesToFile()

        readGradesFromFile()

    reDo(input("\nWould you like to redo the grading session? (y or n): "))


#Main call
if __name__ == "__main__":
    main()
