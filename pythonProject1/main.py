
import random as rand



def get_title(titleFilePath):
    try:
        with open(titleFilePath, "r") as f:
            line = f.read()
            print(line)
    except FileNotFoundError:
        print("File could not be found.\n")
        


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

def load_hangman_drawings(hangmanDrawingsFilePath,num):
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
            print(array[num])
    except FileNotFoundError:
        print("File could not be found.\n")


def get_guess():
    guess = ""
    guess = input("Guess a letter: ")
    while not guess.isalnum():
        guess = input("Please enter only letters of the alphabet: ")
    return guess


def startGame():
    mistakes = 0
    letters_mistakes = []
    get_title("hangmanWord.txt")
    word = get_random_word("ListOfWords.txt")
    correct_list = ["_" for i in range(len(word)-1)]
    while mistakes != 7:
        load_hangman_drawings("hangmanDrawings2.txt", mistakes)
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
            if mistakes < 8:
                mistakes += 1
                print("Letter not in the word.")
                letters_mistakes.append(guess)
                print(set(letters_mistakes))
        if mistakes == 7:
            print("Game over! You lost\n\nThank you for playing!")


startGame()

