import random

num = random.randint(1, 100)

print("This is program where you must try to guess the number the computer has chosen.")
guess = 0
count = 0
while num != guess:
    guess = int(input("Please enter your guess: "))
    count += 1
    if guess > num:
        print("Your guess was too high")
    elif guess < num:
        print("Your guess was too low")

print("Congrats you got it right! The correct number was",num,"and it took",count, "guesses.")
