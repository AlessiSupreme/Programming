#This program simulates a Magic 8 Ball.

import random

def createResponsesFile():

    #Create file
    responses = [
        "Yes, of course!",

        "Without a doubt, yes.",

        "You can count on it.",

        "For sure!",

        "Ask me later!",

        "I'm not sure.",

        "I can't tell you right now.",

        "I'll tell you after my nap.",

        "No way!",

        "I don't think so.",

        "Without a doubt, no.",

        "The answer is clearly NO!"
    ]

    with open('8ball_responses.txt', 'w') as file:

        for response in responses:

            file.write(response + '\n')


def readResponsesFile():

    #Read responses
    responses = []

    with open('8ball_responses.txt', 'r') as file:

        for line in file:

            responses.append(line.strip())

    return responses


def getRandomResponse(responses):

    #Return a random response
    return random.choice(responses)


def main():

    #Main
    createResponsesFile()

    responses = readResponsesFile()

    while True:

        input("Ask a yes or no type question (press Enter to quit): ")

        if input("Ask a yes or no type question (press Enter to quit): ").strip() == "":

            break

        else:

            response = getRandomResponse(responses)

            print("Magic 8 Ball says:", response)


#Main
if __name__ == "__main__":
    main()