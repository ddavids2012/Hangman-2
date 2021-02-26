import random
import sys
#from submission_001-hangman-conditional.hangman import select_random_letter_from


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    if len(sys.argv) > 1 and len(sys.argv) < 3:
        words_file = str(sys.argv[1])
        return (words_file)
    else:
        return "short_words.txt"


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    random_index = random.randint(0, len(word)-1)
    letter = word[random_index]
    hiddenword = ""
    for i in range(len(word)):
        if i == random_index:
            hiddenword = hiddenword + letter
        else:
            hiddenword = hiddenword + "_"
    return hiddenword
        

# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    for index in range(0,len(original_word)):
        if char == original_word[index] and answer_word[index] == "_":
            return True
    return False
    

# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    for index in range(0,len(original_word)):
        if char == original_word[index] and answer_word[index] == "_":
            return(answer_word[:index] + char + answer_word[index+1:])
    return (answer_word)


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 4:
        print ("""/----
|
|
|
|
_______""")
    elif number_guesses == 3:
        print("""/----
|   0
|
|
|
_______""")
    elif number_guesses == 2:
        print("""/----
|   0
|  /|\\
|
|
_______""")
    elif number_guesses == 1:
        print("""/----
|   0
|  /|\\
|   |
|
_______""")
    elif number_guesses == 0:
        print("""/----
|   0
|  /|\\
|   |
|  / \\
_______""")

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    print("Guess the word:",answer)
    guesses = 5
    while guesses > 0:
        guess = get_user_input()
        if is_missing_char(word, answer, guess) == True:
            answer = do_correct_answer(word, answer, guess)
            if answer == word:
                break
        elif guess in ["quit","exit"]:
            print ("Bye!")
            break
        else:
                guesses = guesses - 1
                do_wrong_answer(answer, guesses)
                if guesses == 0:
                    print("Sorry, you are out of guesses. The word was:",word)
                    break
    
# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)
    #print(selected_word)
    run_game_loop(selected_word, current_answer)