import random
number = random.randint(1, 10)
guess=0
count=0

while guess!= number and guess!= "exit":
    guess=input("Please guess a number between 1 and 9 and When you want to end the game type 'exit': ")

    if guess=="exit":
        print("Game End")
        break

    guess=int(guess)
    count+=1
    if guess not in range(1, 10):
        print("guess a number between 1 and 9!")
    elif guess < number:
        print("You have guessed too low!")
    elif guess > number:
        print("You have guessed too high!")
    else:
        print("you have guess exactly right")
        print("You guess exact number in {} tries".format(count))
