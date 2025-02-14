import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    # print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    # print("  ", len(wordlist), "words loaded.")
    return wordlist


word_list = load_words()


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    A sequence is a list, string
    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------
#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters,
    or the empty string "". You may not assume that the string will only contain
    lowercase letters, so you will have to handle uppercase and mixed case strings
    appropriately.

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    points_for_letter = []
    sum_of_points = 0

    word = word.lower()
    word_length = len(word)

    for letter in word:
        if letter in SCRABBLE_LETTER_VALUES:
            points_for_letter.append(SCRABBLE_LETTER_VALUES.get(letter))

    for i in points_for_letter:
        sum_of_points = sum_of_points + i

    second_component_calc = int(7 * word_length) - 3 * (n - word_length)

    if second_component_calc <= 0:
        second_component_calc = 1

    total_score = sum_of_points * second_component_calc
    return total_score


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    # Just showing the letters
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')  # print all on the same line
    print()  # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(0, 1):
        hand["*"] = 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    hand_copy = hand.copy()
    for letter in word:
        if letter in hand_copy.keys():
            if hand_copy.get(letter) > 0:
                hand_copy[letter] = hand_copy.get(letter) - 1

            elif hand_copy.get(letter) == 0:
                break

        elif letter not in hand_copy:
            break

    return hand_copy


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word_copy = word[:]
    hand_copy = hand.copy()

    if word not in word_list:
        if "*" in word:
            for vowel in VOWELS:
                word_copy = word_copy.replace("*", vowel)
                if word_copy in word_list:
                    return True

                elif word not in word_list:
                    word_copy = word[:]
                    continue

        return False

    elif word in word_list:
        for letter in word:
            if letter in hand_copy.keys():
                if hand_copy.get(letter) > 0:
                    hand_copy[letter] = hand_copy.get(letter) - 1

                elif hand_copy.get(letter) == 0:
                    return False

            elif letter not in hand_copy.keys():
                return False

        return True


# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    count = 0
    for (key, item) in hand.items():
        if item > 0:
            count = count + 1

    return count


def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score

    total_score_in_game = 0

    print("Current Hand: ")
    display_hand(hand)

    while calculate_handlen(hand) > 0:

        word = input("Enter Word, or " + "!!" + " to indicate that you are finished: ")
        word = word.lower()

        if word == "!!":
            print("You have ended the game \n")
            break

        if is_valid_word(word, hand, word_list):
            n = calculate_handlen(hand)
            current_score = get_word_score(word, n)
            print("\"%s\" earned %d points" % (word, current_score))
            total_score_in_game = total_score_in_game + current_score
            print("Total Score: ", total_score_in_game)
            hand = (update_hand(hand, word))
            display_hand(hand)
            continue

        else:
            print("Invalid word, try again")
            updated_hand = (update_hand(hand, word))
            display_hand(updated_hand)
            continue

    print("Total Score for this hand: ", total_score_in_game)
    print("----------------------------------")
    return total_score_in_game


# Problem #6: Playing a game
#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    if letter == "*":
        print("Not Possible")
        letter = input(str("Which letter would you like to replace"))
    elif letter in CONSONANTS:
        new_letter = random.choice(CONSONANTS)
    elif letter in VOWELS:
        new_letter = random.choice(VOWELS)

    frequency_of_letter = hand.get(letter)
    del hand[letter]
    hand[new_letter] = frequency_of_letter
    return hand


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    HAND_SIZE = int(input("What is the hand size: "))
    num_of_hands = int(input("Enter total number of hands: "))
    series_score = 0
    num_of_sub = 0
    num_of_replays = 0
    score_after_repeat = 0
    score_before_repeat = 0
    i = 0

    while i <= num_of_hands:

        hand = deal_hand(HAND_SIZE)
        display_hand(hand)

        if num_of_sub < 1:
            sub_letter = str(input("Would you like to subsitute a letter: "))
            if sub_letter == "yes":
                num_of_sub = num_of_sub + 1
                letter = input(str("Which letter would you like to replace: "))
                hand = substitute_hand(hand, letter)
                score_before_repeat = play_hand(hand, word_list)

            elif sub_letter == "no":
                score_before_repeat = play_hand(hand, word_list)

        if num_of_sub > 1:
            print("No Sub")
            score_before_repeat = play_hand(hand, word_list)

        if num_of_replays < 1:
            replay_hand = input(str("Would you like to replay the hand: "))
            if replay_hand == "yes":
                num_of_replays = num_of_replays + 1
                score_after_repeat = play_hand(hand, word_list)
                if score_after_repeat > score_before_repeat:
                    score_before_repeat = score_after_repeat

            elif replay_hand == "no":

                continue

        elif num_of_replays > 1:
            print("Already replayed")
            continue

        series_score = series_score + score_before_repeat

        i = i + 1

    print("Total Score over all hands", series_score)
    return series_score


# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
