import string

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    split_secret_word = list(secret_word)
    word_so_far = []
    global guesses_remaining

    for (index, letter) in enumerate(secret_word):
        if letter in letters_guessed:
            word_so_far.insert(index, letter)
        elif letter not in letters_guessed:
            word_so_far.insert(index, '_ ' )

    if split_secret_word == word_so_far:
        total_score = guesses_remaining * unique(secret_word)
        print("Congratulations")
        print("Total Score: ", total_score)
        print("Good Guess: ", word_so_far)
        exit()

    elif guesses_remaining == 0:
        print("You ran out of guesses")
        print("The word is", secret_word)
        exit()

    else:
        print("Good Guess: ", word_so_far)
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

secret_word = "else"
num_of_letters_in_secret_word = len(secret_word)
guesses_remaining = 6
warnings_remaining = 3
letters_guessed= []
word_so_far = []
check_full_word = []

# Initial Statement
print("Welcome to the game Hangman!")
print("I am thinking of a word that is %d letters long" % (num_of_letters_in_secret_word))
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

'''
Starts up an interactive game of Hangman.

* At the start of the game, let the user know how many 
  letters the secret_word contains and how many guesses s/he starts with.

* The user should start with 6 guesses

* Before each round, you should display to the user how many guesses
  s/he has left and the letters that the user has not yet guessed.

* Ask the user to supply one guess per round. Remember to make
  sure that the user puts in a letter!

* The user should receive feedback immediately after each guess 
  about whether their guess appears in the computer's word.

* After each guess, you should display to the user the 
  partially guessed word so far.

Follows the other limitations detailed in the problem write-up.
'''
# FILL IN YOUR CODE HERE AND DELETE "pass"


#keep running until
#1. Guesses is 0, tell them they lost and reveal secret word
#2. getGuessWord is true print congrualatory mesage and tell user their score






