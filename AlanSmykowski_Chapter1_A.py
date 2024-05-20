#Initialize constants and accumulators
TOTALTICKETS = 20

ticketsSold = 0

buyerCount = 0

#Main
while ticketsSold < TOTALTICKETS:

    #Prompt user
    ticketsPurchased = int(input("Enter the number of tickets you want to buy (up to 4): "))

    #Check validity
    if 1 <= ticketsPurchased <= 4 and ticketsSold + ticketsPurchased <= TOTALTICKETS:

        #Update accumulators
        ticketsSold += ticketsPurchased

        buyerCount += 1

        #Calculate remaining tickets
        remainingTickets = TOTALTICKETS - ticketsSold

        #Display remaining tickets
        print(f"You've purchased {ticketsPurchased} tickets. Remaining tickets: {remainingTickets}")

    else:

        print(

            "Invalid number of tickets.")


#Display total
print(f"Total number of buyers: {buyerCount}")
