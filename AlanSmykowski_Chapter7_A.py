#This program counts the number of sentences and prints them

import re


#Function to find sentences
def findSentences(text):

    #Include numbers at the start of a sentence
    pattern = r'[\dA-Z].*?[.!?](?= [\dA-Z]|$)'

    sentences = re.findall(pattern, text, flags=re.DOTALL | re.MULTILINE)

    return sentences


#Main
def main():

    #Example text including sentences starting with numbers
    #Modify this as if it was a user input field
    text = '''See the U.S.A. today. It's right here, not
    a world away. Average temp. is 66.5. 2 people were there.
    The meeting is on 5th Ave. What time is it? 4.5 million people attended.'''

    #Find and count sentences
    sentences = findSentences(text)
    sentenceCount = len(sentences)

    #Display the sentences and the count
    for sentence in sentences:
        print(f"-> {sentence}")

    print(f"\nNumber of sentences: {sentenceCount}\n")


#Main call
if __name__ == "__main__":
    main()
