import random 

MAX_TRIES = 6

def print_home_page():
    HANGMAN_ASCII_ART = "Welcome to the game Hangman\n " """ 
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/ \n"""
                         
                         
    print(HANGMAN_ASCII_ART, MAX_TRIES)


HANGMAN_PHOTOS = {1:''' x-------x''', 2:
'''    x-------x
    |
    |
    |
    |
    |
'''
,3: '''
    x-------x
    |       |
    |       0
    |
    |
    |
''' ,4:'''
    x-------x
    |       |
    |       0
    |       |
    |
    |
''',5: '''
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |'''
,6:'''
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |''', 7:'''
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
'''}


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks if the input letter is valid for the game.
    
    :param letter_guessed: The letter guessed by the player
    :param old_letters_guessed: List of letters already guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if the input is valid, False otherwise
    :rtype: bool
    """
    if (len(letter_guessed) > 1) and (not letter_guessed.isalpha()):
        return False
    elif not letter_guessed.isalpha():
        return False
    elif len(letter_guessed) > 1:
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    else:
        return True
        
        
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Tries to update the list of old letters guessed by the player.
    
    :param letter_guessed: The letter guessed by the player
    :param old_letters_guessed: List of letters already guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if the letter was successfully added to the list, False otherwise
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        letter_guessed = letter_guessed.lower()
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        old_letters_guessed.sort()
        print('X')
        print('->'.join(old_letters_guessed))
        return False

     
 

def show_hidden_word(secret_word, old_letters_guessed):
    """
    Shows the hidden word with guessed letters revealed and unguessed letters hidden.
    
    :param secret_word: The secret word to be guessed
    :param old_letters_guessed: List of letters already guessed by the player
    :type secret_word: str
    :type old_letters_guessed: list
    :return: The hidden word with guessed letters revealed and unguessed letters hidden
    :rtype: str
    """
    str = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            str += letter
        else:
            str += " _ "
    return str
    
    
def check_win(secret_word, old_letters_guessed):
    """
    Checks if all letters in the secret word have been guessed.
    
    :param secret_word: The secret word to be guessed
    :param old_letters_guessed: List of letters already guessed by the player
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True if all letters in the secret word have been guessed, False otherwise
    :rtype: bool
    """
    for letter in secret_word:
        if letter  not in old_letters_guessed:
            return False
    return True
        
        
def print_hangman(num_of_tries):
    """
    Prints the hangman ASCII art corresponding to the number of incorrect guesses.
    :param num_of_tries: Number of incorrect guesses made by the player
    :type num_of_tries: int
    """
    print(HANGMAN_PHOTOS[num_of_tries])
 

def choose_word(file_path, index):
    """
    Chooses a word from a text file based on the given index.

    :param file_path: Path to the text file containing a list of words
    :param index: Index of the chosen word (1-based)
    :type file_path: str
    :type index: int
    :return: A tuple containing the number of unique words in the file and the chosen word
    :rtype: tuple
    """
    with open(file_path, 'r', encoding='iso-8859-1') as f:
        words = f.read().split()  # Split the file content into a list of words

    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    num_unique_words = len(unique_words)

    # Adjust the index to be 0-based and handle circular indexing
    index = (index - 1) % num_unique_words

    chosen_word = unique_words[index]

    return num_unique_words, chosen_word
     

old_letters_guessed = []

def main():
    print_home_page()
    url = input("enter the url of the file: ")
    choosen_word_ind = int(input("enter the index of your choosen word: "))
    secret_word = choose_word(url, choosen_word_ind)[1]
    print("Let's start!")
    print_hangman(1)
    lines_of_guess = '_ ' * len(secret_word)
    print(lines_of_guess)
    end_of_game = False
    num_of_tries = 1
    while (num_of_tries <= MAX_TRIES) and (end_of_game == False):
        guess = input("Guess a letter: " )
        if try_update_letter_guessed(guess, old_letters_guessed):
            guess = guess.lower()
            if guess not in secret_word:
                num_of_tries += 1
                print(":(")
                print_hangman(num_of_tries)
                print(show_hidden_word(secret_word, old_letters_guessed))
            else:
                print(show_hidden_word(secret_word, old_letters_guessed))
        end_of_game = check_win(secret_word, old_letters_guessed)
    if end_of_game:
        print("WIN")
    else:
        print("LOSE")

        
        
if __name__ == "__main__":
    main()

