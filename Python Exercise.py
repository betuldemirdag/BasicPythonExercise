
                    #  BASIC PYTHON EXERCISE  #



###############################################################################
# CALCULATOR
###############################################################################


while True:

    select = input("Select the function what you want (ex: add, multi, sub, divs): ")
    
    if select == "stop":
        break
    
    num_1 = int(input("Enter the 1st number: "))
    num_2 = int(input("Enter the 2nd number: "))
    
    add = num_1 + num_2
    multi = num_1*num_2
    sub = num_1-num_2
    divs = num_1/num_2

    def calculator(num_1, num_2, select):
   
        if select == "add":
            print("addition: ", add)
    
        elif select == "multi":
            print("multiple: ", multi)
        
        elif select == "sub":
            print("subtraction: ", sub)
            
        elif select == "divs":
            print("division: ", divs)
            
        else:
            print("Error! You selected the undefined function!") 
            

    calculator(num_1, num_2, select)

  
###############################################################################
# GUESS THE NUMBER
###############################################################################


import random

number = random.randint(1, 100)

while True:
   
    guess = int(input("Enter a number 1-100 which you guess: "))

    if guess == number:
        print("Congratulations! You win!") 
        break


    if guess > number:
        print("Your guess is too high!")

    elif guess < number:
        print("Your guess is too low!")
    
    else:
        print("You entered the undefined number. Please enter an integer number which is 1-100 ")



###############################################################################
# READ THE TEXT FILE AND COUNT THE WORDS
###############################################################################

with open('text file.txt', encoding="utf8") as file:
    file_content = file.read()
    file_content.lower()

    words = file_content.lower().split()
    print(len(words))
    
# Analyse the word

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(words, columns = ["Words"])
freq = df.value_counts().reset_index()
freq.columns = ['Word', 'Frequency']
freq = freq.sort_values(by="Frequency", ascending = False)

freq.head(10).plot(kind = "barh", x="Word", y="Frequency", legend = False)
plt.gca().invert_yaxis()
plt.title("Distribution of the Top 10 Words")
plt.xlabel("Frequency")
plt.ylabel("Word")
plt.show()


###############################################################################
# FIBONACCI SEQUENCE
###############################################################################

n = int(input("Enter a number: "))

def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1

    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

fibonacci_sequence = generate_fibonacci(n)
print(fibonacci_sequence)


###############################################################################
# PRIME NUMBER CHECKER
###############################################################################

num = int(input("Enter a number: "))

if num <= 1:
    print(f"The number {num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"The number {num} is a prime number.")
    else:
        print(f"The number {num} is not a prime number.")


###############################################################################
# ROCK, PAPER, SCISSORS GAME
###############################################################################


import random

move = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(move)
    player = input("Enter your move (rock, paper, scissors): ")
    
    if player not in move:
        print("Enter a valid move (rock, paper, scissors)" )
    elif player == computer:
        print("Your choice is the same choice with the computer, enter a different move")
    else: 
        True
        
        if True:

            if computer == "rock" and player == "paper":
                print("Computer's choice = ",computer,"Player is win!")
            elif computer == "rock" and player == "scissors":
                print("Computer's choice = ",computer,"Computer is win!")
            elif computer == "paper" and player == "rock":
                print("Computer's choice = ",computer,"Computer is win!")
            elif computer == "paper" and player == "scissors":
                print("Computer's choice = ",computer,"Player is win!")
            elif computer == "scissors" and player == "rock":
                print("Computer's choice = ",computer,"Player is win!")
            else:
                print("Computer's choice = ",computer,"Computer is win!")
        
            break


###############################################################################
# HANGMAN GAME
###############################################################################

import random

# List of words for the game
word_list = ["python", "apple", "model", "bookcase", "scientist", "orange", "cinema", "tablespoon", "frame", "library"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to play Hangman
def play_hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 5  # You can adjust the number of allowed attempts

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        print("Attempts left:", attempts)
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
                     
        if guess in word_to_guess:
            print("Good guess!")
            if set(guessed_letters) == set(word_to_guess):
                print("\nCongratulations! You've won. The word was:", word_to_guess)
                break
        
        else:
            print("Incorrect guess.")
            attempts -= 1
        
        print("Do you have any idea for word?")
        trial = input("yes/no:")
        if trial == "yes":
            idea = input("Please enter your idea: ")
            if idea == word_to_guess:
                print("\nCongratulations! You've won. The word was:", word_to_guess)
                break
            else:
                print("Wrong guess! Keep trying.")
        else:
            continue
            
    if attempts == 0:
        print("\nYou're out of attempts. The word was:", word_to_guess)
    
 
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_hangman()
    else:
        print("Thanks for playing!")

# Start the game
play_hangman()  



###############################################################################
# TO-DO LIST
###############################################################################

class ToDoList:
    def __init__(self):
        self.to_do = []
        self.index = []

    def add_to_do(self, task):
        self.to_do.append(task)

    def display(self):
        if not self.to_do:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.to_do, start=1):
                print(f"{i}. {task}")

if __name__ == "__main__":
    my_todo_list = ToDoList()
    
    for n in range(1, 11):
        my_todo_list.index.append(n)
    
    while True:
        user_input = input("Enter a task (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        my_todo_list.add_to_do(user_input)

    my_todo_list.display()



###############################################################################
# TEMPERATURE CONVERTER
###############################################################################

temperatures = ["celsius", "fahrenheit", "kelvin"]

while True:
    
    convert = str(input("Please enter the temperature you want to convert: "))
    convert = convert.lower()
    to = str(input("Please enter the temperature it will turn into: "))
    to = to.lower()

    if convert not in temperatures:
        print("Please enter the valid temperatures (celsius, fahrenheit, kelvin)")
    elif to not in temperatures:
        print("Please enter the valid temperatures (celsius, fahrenheit, kelvin)")
    else:
        break
    
degree = int(input("Please enter the degree: "))


if convert == "celsius" and to == "fahrenheit":
    f = (degree*(1.8))+ 32
    print(degree, "celsius = ",f, "fahrenheit" )
elif convert == "celsius" and to == "kelvin":
    k = degree + 273.15
    print(degree, "celsius = ",k, "kelvin" )
elif convert == "fahrenheit" and to == "celsius":
    c = (degree-32)/(1.8)
    print(degree, "fahrenheit = ",c, "celsius" )
elif convert == "fahrenheit" and to == "kelvin":
    k = (degree + 459.67)/(1.8)
    print(degree, "fahrenheit = ",k, "kelvin" )
elif convert == "kelvin" and to == "celsius":
    c = degree - 273.15
    print(degree, "kelvin = ",c, "celsius" )
else:
    f = (1.8)*degree - 459.67
    print(degree, "kelvin = ",f, "fahrenheit" )




























