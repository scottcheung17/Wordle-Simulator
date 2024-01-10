import random
import sys
from termcolor import colored

def print_start():
    print("Guess the Wordle in 6 tries.")
    print("Each guess must be a valid 5-letter word.")
    print("The color of the tiles will change to show "
          "how close your guess was to the word\n")

def get_word():
    with open("dictionary.txt") as file:
        word_list = file.read().splitlines()
        return random.choice(word_list)
    
def word_exists(word):
    with open("dictionary.txt") as file:
        words = file.read()
        if word in words:
            return True
        else:
            return False
        
print_start()
replay = ""
while replay != "s":
    word = get_word()
    for attempt in range(1,7):
        guess = input().lower()
        
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        while len(guess) != 5 or not word_exists(guess):
            if len(guess) != 5:
                print("Please enter a 5 letter word")
            else:
                print("This word doesn't exist")
            guess = input().lower()

        for i in range(5):
            if guess[i] == word[i]:
                print(colored(guess[i], "green"), end = "")
            elif guess[i] in word:
                print(colored(guess[i], "yellow"), end = "")
            else:
                print(guess[i], end = "")
        print("")

        if guess == word:
            if attempt == 1:
                print(f"Congratulations, you got the answer in {attempt} try!")
                break
            print(f"Congratulations, you got the answer in {attempt} tries!")
            break
        elif attempt == 6:
            print(f"You failed :(, the wordle was {word}")
    replay = input("Wish to replay? Type s to stop.")