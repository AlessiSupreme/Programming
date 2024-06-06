#This program checks user prompted text to determine likelihood of spam and times it

import time

#Constants
SPAMKEYWORDS = [
    "act", "amazing", "buy", "cash", "cheap", "claim",
    "click", "congratulations", "credit", "deal", "discount",

    "earn", "exclusive", "free", "guarantee", "link",
    "limited", "miracle", "money", "cost", "offer",

    "opportunity", "prize", "participant", "refund", "reward",
    "save", "selected", "trial", "win", "worth"
]


#Timer
def make_timer(startTime):

    elapsedTime = time.time() - startTime

    print(f"Elapsed time: {elapsedTime:.2f} seconds.\n")


#Score
def getScore(message):

    spamScore = 0

    matchedKeywords = []

    #Scan for keywords
    for keyword in SPAMKEYWORDS:
        keywordCount = message.lower().count(keyword.lower())

        if keywordCount > 0:
            spamScore += keywordCount

            matchedKeywords.append(keyword)

    return spamScore, matchedKeywords


#Likelihood based on score
def getLikelihood(score):

    if score == 30:
        likelihood = "Highest possible"

    elif score >= 20:
        likelihood = "Very High"

    elif score >= 15:
        likelihood = "High"

    elif score >= 10:
        likelihood = "Moderate"

    elif score >= 5:
        likelihood = "Low"

    else:
        likelihood = "Very Low"

    return likelihood


#Percentage based on score
def getPercentage(score):

    percentage = (100 / 30) * score

    return int(percentage)


#Redo program
def reDo(answer):

    if answer == "y":
        print("Continuing instance.\n")
        main()

    else:
        print("Program exit.")

    return


#Main
def main():

    #Start timer
    startTime = time.time()

    #User prompt
    emailMessage = input("Enter the email message to be evaluated: ")

    #Call to get score and keywords
    spamScore, matchedKeywords = getScore(emailMessage)

    #Call to get likelihood
    likelihood = getLikelihood(spamScore)

    #Call to get percentage
    percentage = getPercentage(spamScore)

    #Results
    print("\nSpam score:", spamScore)

    print("Likelihood of spam: " + str(likelihood) + " (" + str(percentage) + "% of words detected)")

    if matchedKeywords:
        print("Common spam keywords detected:", ", ".join(matchedKeywords), "\n")

    else:
        print("No spam keywords found.\n")

    #Display elapsed time
    make_timer(startTime)

    reDo(input("Check another message? (y/n): "))


#Main call
if __name__ == "__main__":
    main()
