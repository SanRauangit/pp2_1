import random
def guess_num():
    name=input("Hello! What is your name? \n")
    secret_num=random.randint(1,20)
    guesses_taken=0
    print(f"Well,{name},i am thinking of a number between 1 and 20.")
    while True:
        guess_input=input("Take a guess \n")
        guesses_taken += 1
        if(guess_input.isdigit()):
            guess=int(guess_input)
            if(guess>20 or guess<1):
                print("Please enter a valid number between 1 and 20")
                guesses_taken -= 1
                continue
            if guess < secret_num:
                print("Your guess is too low.")
            elif guess > secret_num:
                print("Your guess is too high.")
            else:
                print(f"Well done,{name}! You guessed my number in {guesses_taken} guesses!")
                break
guess_num()