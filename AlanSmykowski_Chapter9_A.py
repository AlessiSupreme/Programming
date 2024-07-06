#Program for managing a bank account with a test function

#BankAcct class
class BankAcct:
    def __init__(self, name, accountNumber, amount, interestRate):
        self.name = name
        self.accountNumber = accountNumber
        self.amount = amount
        self.interestRate = interestRate

    #Adjusting the interest rate
    def adjustInterestRate(self, newRate):
        self.interestRate = newRate

    #Withdrawing money
    def withdraw(self, amount):
        if amount > self.amount:
            print("Insufficient funds.")
        else:
            self.amount -= amount

    #Depositing money
    def deposit(self, amount):
        self.amount += amount

    #Getting the balance
    def getBalance(self):
        return self.amount

    #Calculateing interest
    def calculateInterest(self, days):
        interest = self.amount * (self.interestRate / 100) * (days / 365)
        return interest

    #String representation of the account
    def __str__(self):
        return f"\nAccount holder: {self.name}, Balance: ${self.amount:.2f}, Interest rate: {self.interestRate}%"


#Test function
def testBankAcct():
    #Creating a bank account
    acct = BankAcct("John Doe", "123456789", 1000, 5)

    #Displaying initial account info
    print(f"\nAccount information\n___________________{acct}")
    print("_______________________________________________________________")

    #Test for deposit method
    acct.deposit(500)
    print(f"\nAfter depositing $500\n_____________________{acct}")
    print("_______________________________________________________________")

    #Test for withdraw method
    acct.withdraw(300)
    print(f"\nAfter withdrawing $300\n______________________________{acct}")
    print("_______________________________________________________________")

    #Test for getting balance method
    balance = acct.getBalance()
    print(f"\nCurrent balance: ${balance:.2f}")

    #Test for adjusting the interest rate
    acct.adjustInterestRate(6)
    print(f"\nAfter adjusting interest rate to 6%\n_________________________{acct}")
    print("_______________________________________________________________")

    #Test for calculating interest
    interest = acct.calculateInterest(30)
    print(f"\nInterest for 30 days: ${interest:.2f}")

    #Display for final info
    print(f"\nFinal account information\n_________________________{acct}")
    print("_______________________________________________________________")


#Main
def main():
    testBankAcct()


#Main call
if __name__ == "__main__":
    main()
