
import random as rand


'''
The function get_title gets the title of the game from the file that the user chooses as parameter "titleFilePath".
It then tries to find the file path from the parameter and opens and reads from it displaying the content which is the title
If the file path isnt correct or the file is missing or mispelled the code with throw an error and quit the application nicely
'''
def get_title(titleFilePath):
    try:
        with open(titleFilePath, "r") as f:
            line = f.read()
            print(line)
    except FileNotFoundError:
        print("File could not be found.\n")
        exit()

'''
This function get_random_word return a random word from the list selected by the user from the parameter.
It opens and reads each one of the words in the text file and chooses a random from that list.
If the file wasnt found or the path is incorrect, the program will throw an error and will use the backup words instead which are stored in the backup_words list. 
'''
def get_random_word(randomWordList):
    backup_words = ["kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz"]
    try:
        with open(randomWordList, "r") as w:
            words = w.readlines()
            random_word = rand.choice(words)
            return random_word
    except FileNotFoundError:
        print("File could not be found. Using back up words instead..\n")
        random_backup_word = rand.choice(backup_words)
        return random_backup_word

"""
In this function the hangman drawing will be displayed and will change everytime the user gets the letter wrong until the user loses
First of all the file from the parameter that the user chooses to uses will load.
These drawings from the text file will be looped and the "\n" will be removed to seperate each drawing.
Once thats done the we are store the actual drawing in the "array" and create the drawings, tempArray will be cleaned.
To access the drawings a parameter "num" is created and will will use that parameter to give different indexes for the drawing
"""
def load_hangman_drawings(hangmanDrawingsFilePath):
    try:
        array = []
        with open(hangmanDrawingsFilePath, 'r') as f:
            drawings = f.readlines()
            tempArray = []
            for line in drawings:
                if not line == "\n":
                    tempArray.append(line)
                else:
                    array.append("".join(tempArray))
                    tempArray = []
            return array
    except FileNotFoundError:
        print("File could not be found.\n")

"""
This small function is only used to ask the user repedetly to input a guess and to input a letter and not a symbol or number.
Basically any letter from the alphabet.
Script will run until the user inputs a letter and will be triggered when the user inputs a non alphabetical letter
"""
def get_guess():
    guess = ""
    guess = input("Guess a letter: ")
    while not guess.isalnum():
        guess = input("Please enter only letters of the alphabet: ")
    return guess

"""
In the final function which is the main function that connects everything together we initialise a "mistakes" variable and the letters that the user mistakes storing them in a list.
First of all we call the function get_title to display the title giving it the file path as parameter.
We get a random word from the get_random_word function and store it in a variable.
Once we get the random word we make the correct_list which is the list that displays the hidden word and will reveal the hidden word everytime we input a correct letter.
When the user inputs a letter it will be saved in the mistake letters list or if correct it will be added in the correct list
For every letter that is not in the word an error will be displayed and it will loop the guess question until the user runs out of lives and the game will output a good bye message.
"""
def startGame():
    mistakes = 0
    letters_mistakes = []
    get_title("hangmanWord.txt")
    word = get_random_word("ListOfWords.txt")
    correct_list = ["_" for i in range(len(word)-1)]
    hangmanMistakesMax = load_hangman_drawings("hangmanDrawings2.txt")
    while mistakes != len(hangmanMistakesMax) :
        print(hangmanMistakesMax[mistakes])
        print("".join(correct_list))
        guess = get_guess()
        if len(guess) != 1:
            multiple_enters = list(guess)
            print(multiple_enters)
            for i in multiple_enters:
                if i in word:
                    index_letter = word.index(guess)
                    correct_list[index_letter] = guess
                else:
                    mistakes += 1
                    print("Letter not in the word.")
                    letters_mistakes.append(guess)
                    print(set(letters_mistakes))
        if guess in word:
            index_letter = word.index(guess)
            correct_list[index_letter] = guess
        else:
            if mistakes < len(hangmanMistakesMax):
                mistakes += 1
                print("Letter not in the word.")
                letters_mistakes.append(guess)
                print(set(letters_mistakes))
        if mistakes == len(hangmanMistakesMax):
            print("Game over! You lost\n\nThank you for playing!")


startGame()

