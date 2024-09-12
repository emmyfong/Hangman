# Hangman Game
# Date: 2024.8.22
# Author: Emmy Fong
# \

#Imports
import random
from words import wordList

#Functions
def getWord():
    randomWord = random.choice(wordList)
    #convert to uppercase to make it easier for comparison
    randomWord = randomWord.upper()
    #return the word
    return randomWord

def drawHangman(tries):
    #draw the hangman
    hangmanStages = [
    '''
    ------
    |    |
    |
    |
    |
    |
    -----------
    ''',

    '''
    ------
    |    |
    |    O
    |
    |
    |
    -----------
    ''',

    '''
    ------
    |    |
    |    O
    |    |
    |
    |
    -----------
    ''',

    '''
    ------
    |    |
    |    O
    |  / |
    |
    | 
    -----------
    ''',
    
    '''
    ------
    |    |
    |    O
    |  / | \\
    |
    | 
    -----------
    ''',

    '''
    ------
    |    |
    |    O
    |  / | \\
    |    |
    | 
    -----------
    ''',

    '''
    ------
    |    |
    |    O
    |  / | \\
    |    |
    |   / 
    -----------
    ''',

    '''
    ------
    |    |
    |    O
    |  / | \\
    |    |
    |   / \\
    -----------
    '''
    ]
    print(hangmanStages[tries])

def main(word):
    lenOfWord = len(word)
    displayWord = '_ ' * lenOfWord
    guessedWords = []
    guessedLetters = []
    maxTries = 7
    correct = False
    incorrectGuesses = 0
    correctGuesses = 0

    drawHangman(incorrectGuesses)
    print(displayWord)

    #start playing loop
    # Stopping Conditions:
    #   The word has been guessed correctly
    #   The hangman has been fully drawn
    #  \
    while(((correct != True) and (correctGuesses != lenOfWord)) and (incorrectGuesses < maxTries)):
        #FOR TESTING PURPOSES
        #print(word)
        
        userInput = input("\nPlease guess a letter or word: ")

        #convert to uppercase
        userInput = userInput.upper()

        #check if it's a letter
        if (len(userInput) == 1) and userInput.isalpha():
            #it is a letter

            #check if it's been guessed already
            if(userInput in guessedLetters):
                print("This letter has been guessed already\n")
                continue
            
            else:
                guessedLetters.append(userInput)
                #checker boolean
                isInWord = False
                
                #check if the letter is in the word
                letterIndex = 0
                for element in word:
                    if(element == userInput):
                        isInWord = True
                        correctGuesses += 1
                        displayWord = displayWord[:letterIndex] + userInput + displayWord[letterIndex + 1:]
                    letterIndex += 2

                if (isInWord == True):
                    print(userInput + " is in the word!")
                else:
                    print(userInput + " is not in the word!")
                    incorrectGuesses += 1

        elif (len(userInput) <= lenOfWord) and userInput.isalpha():
            #it's a word
            #Check if its been guessed
            if(userInput in guessedWords):
                print("This word has been guessed already\n")
            
            else:
                guessedWords.append(userInput)

                if(userInput == word):
                    #the guess is correct
                    print(userInput + " is the word!!!")
                    displayWord = userInput
                    correct = True
                if(len(userInput) <= lenOfWord):
                    #Checker for any letters
                    anyLetters = False

                    #Check to see if any letters are in the word
                    #split the string into characters
                    splitInput = [*userInput]
                    splitWord = [*word]
                    displayWordList = list(displayWord)
                    for i in splitInput:
                        for index, j in enumerate(splitWord):
                            if(i == j):
                                anyLetters = True
                                correctGuesses += 1
                                displayWordList[2 * index] = i  # Update the correct position in the list
                            if anyLetters:
                                print(i + " is in the word!")
                            else:
                                print(userInput + " is not in the word!")
                                incorrectGuesses += 1
                    
                    #Combine with current displayWord
                    displayWord = ''.join(displayWordList)


        else:
            #not valid
            print("Not a valid input")

        drawHangman(incorrectGuesses)
        print(displayWord)
        if correctGuesses == lenOfWord:
            correct = True

    if(correct or (correctGuesses == lenOfWord)):
        print("Congratulations! You guessed the correct word: " + word)
        print("You had " + str(incorrectGuesses) + " incorrect guesses!")
    
    if(incorrectGuesses >= maxTries):
        print("You lost T^T")
        print("The word was " + word)

#Run the game
print("Let's play hangman!!\n")
playing = True

while(playing == True):
    randomWord = getWord()
    main(randomWord)
    print("\n")
    while(playing):
        playAgain = input("Would you like to play again? (Y/N): ")
        playAgain = playAgain.upper()
        if(playAgain == 'Y'):
            break
        elif(playAgain == 'N'):
            playing = False
            quit()
        else:
            print("That was not a valid input")
            