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
    possible_matches = []
    for other_word in list_of_words():
        # match_with_gaps(my_word, other_word)
        if match_with_gaps(my_word, other_word):
            possible_matches.append(other_word)
            continue
        else:
            continue

    if not possible_matches:
        print("No Matches")
    else:
        print(possible_matches)

my_word = "t_ _ t"
show_possible_matches(my_word)


