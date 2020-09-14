# Problem Set 2, hangman.py
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def list_of_words():
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    split_secret_word = list(secret_word)
    global guesses_remaining
    global my_word

    for (index, letter) in enumerate(secret_word):
        if letter in letters_guessed:
            word_so_far.insert(index, letter)
        elif letter not in letters_guessed:
            word_so_far.insert(index, '_ ' )

    if split_secret_word == word_so_far:
        total_score = guesses_remaining * unique(secret_word)
        print("Good Guess: ", word_so_far)
        print("Congratulations")
        print("Total Score: ", total_score)
        exit()

    elif guesses_remaining == 0:
        print("You ran out of guesses")
        print("The word is", secret_word)
        exit()

    else:
        print("Guess: ", word_so_far)
        my_word_list = word_so_far[:]
        my_word = ''.join(my_word_list)
        word_so_far.clear()
        print("\n------")
        return

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    alphabet = list(string.ascii_lowercase)
    alphabet_copy = alphabet[:]

    for letter in alphabet_copy:
        if letter in letters_guessed:
            alphabet.remove(letter)

    alphabet = ''.join(alphabet)
    print("Available Letters: ", alphabet)
    return alphabet

def unique(secret_word):
    '''
    Purpose for total score calculation
    Create a unique list. If secret word letters are unique add it to unique list
    '''

    split_secret_word=list(secret_word)
    unique_list = []

    for i in split_secret_word:
        if i not in unique_list:
           unique_list.append(i)

    return len(unique_list)

def user_input(letter):

    global guesses_remaining
    global warnings_remaining

    consonants = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    #generate list for consonants
    for i in string.ascii_lowercase:
        if i not in vowels:
            consonants.append(i)
    ##end generate list for consonants

    if letter in vowels:
        if letter in letters_guessed:
            print("Oops! You've already guessed that letter.")
            if warnings_remaining > 0:
                warnings_remaining = warnings_remaining - 1
                print("You have %d warnings remaining" % (warnings_remaining))
                return

            elif guesses_remaining > 0:
                guesses_remaining = guesses_remaining - 1
                print("You have no warnings left")
                print("You have %d guesses remaining" % guesses_remaining)
                return

        elif letter not in letters_guessed:
            letters_guessed.append(letter)
            if letter in secret_word:
                return
            elif letter not in secret_word:
                print("Oops! That letter is not in my word")
                guesses_remaining = guesses_remaining - 2
                # print("You have %d guesses remaining" % guesses_remaining)
                return

    elif letter in consonants:
        if letter in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining = warnings_remaining - 1
                print("You have %d warnings remaining" % (warnings_remaining))
                return

            elif guesses_remaining > 0:
                guesses_remaining = guesses_remaining - 1
                print("You have no warnings left")
                print("You have %d guesses remaining" % guesses_remaining)
                return

        elif letter not in letters_guessed:
            letters_guessed.append(letter)
            if letter in secret_word:
                return
            elif letter not in secret_word:
                print("Oops! That letter is not in my word")
                guesses_remaining = guesses_remaining - 1
                # print("You have %d guesses remaining" % guesses_remaining)
                return

def illegal_characters(letter):
    '''
    Check if the letter is in alphabet
    If it is not in alphabet subtract warnings then subtract list
    '''

    global warnings_remaining
    global guesses_remaining

    if str(letter) not in string.ascii_lowercase:
        if str(letter) == "*":
            pass
            return

        else:
            print ("You can only input an alphabet")

            if warnings_remaining >0:
                warnings_remaining = warnings_remaining - 1
                print("You have %d warnings remaining" % warnings_remaining)
                return

            elif guesses_remaining > 0:
                guesses_remaining = guesses_remaining-1
                print("You have no warnings left")
                print("You have %d guesses remaining" % guesses_remaining)
                return
    else:
        return

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''

    my_word = my_word.replace("_ ", "_")

    if len(my_word) != len(other_word):
        return False

    elif len(my_word) == len(other_word):
        for (index, letter) in enumerate(other_word):
            if letter in my_word[index]:
                continue
            elif letter not in my_word[index]:
                if "_" in my_word[index]:
                    pass
                else:
                    return False
        return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''

    for other_word in list_of_words():
        if match_with_gaps(my_word, other_word):
            possible_matches.append(other_word)
            continue
        else:
            continue

    if not possible_matches:
        print("No Matches")
    else:
        print(possible_matches)



secret_word = choose_word(wordlist)
num_of_letters_in_secret_word = len(secret_word)
guesses_remaining = 6
warnings_remaining = 3
letters_guessed = []
word_so_far = []
check_full_word = []
my_word_list = []
possible_matches = []
my_word = ""


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    '''

    # Initial Statement
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long" % (num_of_letters_in_secret_word))
    print("You have %d warnings left" % warnings_remaining)
    print("-----\nYou have %d guesses left" % guesses_remaining)

    while True:

        letter = str(input("Please guess a letter (use * for help): "))

        if letter == "*":
            show_possible_matches(my_word)

        letter = letter.lower()
        illegal_characters(letter)
        user_input(letter)
        get_guessed_word(secret_word, letters_guessed)
        print("You have %d guesses left" % guesses_remaining)
        get_available_letters(letters_guessed)


hangman_with_hints(secret_word)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    '''

    # Initial Statement

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long" % num_of_letters_in_secret_word)
    print("You have %d warnings left" % warnings_remaining)
    print("-----\nYou have %d guesses left" % guesses_remaining)

    while True:
        letter = str(input("Please guess a letter: "))
        letter = letter.lower()
        illegal_characters(letter)
        user_input(letter)
        get_guessed_word(secret_word, letters_guessed)
        print("You have %d guesses left" % guesses_remaining)
        get_available_letters(letters_guessed)
        continue


# hangman(secret_word)



