import random 

#counter for the number of attempts of the user
attempts = 0 
#counter for the correct answer/s of the user
correct_answers = 0

#function to generate a random number between 0 and 512 and format it to binary
def generate_binary():
    random_number = random.randint(0, 512)
    binary_digit = "{0:b}".format(int(random_number))
    return random_number, binary_digit

#function to get the user's answer and validate it
def get_answer():
    while True:
        try:
            answer = int(input("Your answer: "))
            return answer
        except ValueError:
            print("Please enter a number.")

#function to check the user's answer and update the score
def check_answer(random_number, answer):
    global attempts, correct_answers
    if answer == random_number:
        print("Number guessed correctly.")
        correct_answers += 1
    else:
        print("Number guessed incorrectly. Try again.\n")
    attempts += 1
    score = f"{correct_answers}/{attempts}"
    print(f"Score: {score}")

#function to ask the user if they want to continue playing
def continue_game():
    choice = input("\nDo you want to continue? (y/n): ").lower()
    return choice == 'y'

#main loop of the game
while True:
    print("\nBinary Digit Game\n")
    random_number, binary_digit = generate_binary()
    #just to know the random number ^.^ 
    #print(random_number)
    while True:
        print(f"Binary digit: {binary_digit}")
        answer = get_answer()
        check_answer(random_number, answer)
        if answer == random_number:
            break
    if not continue_game():
        break

score = f"{correct_answers}/{attempts}"
print(f"Final Score: {score}")