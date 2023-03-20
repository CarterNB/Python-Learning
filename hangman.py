import random

words = ["piggy","kitten","hyena","zebra","lion","hippo"]

chosen = words[random.randint(0, len(words) - 1)]
sol = [0] * len(chosen)
print("welcome to hangman your word is", len(chosen), "long")
life = 3
check = ""
while life != 0 and check != chosen:
    guess = input("Enter your guess: ")
    count = 0
    flag = 0
    if flag != 1:
        for i in range(0, len(chosen)):
            if guess == chosen[i]:
                sol[i] = guess
                count += 1
                check = "".join([str(c) for c in sol])
                check = check.strip()
                flag = 1
    if count == 0:
        life -= 1
        print("There are no", guess, "(s) in the puzzle you have", life, "guesses remaining")
    elif count != 0:
        print(check)
        print("There are", count, guess, "(s) and you have", life, "guesses remaining")

if life == 0:
    print("You have lost. The correct word was " + chosen + ". Better luck next time")
else:
    print("Congrats you have guessed the word with", life, "guess(es) remaining")
