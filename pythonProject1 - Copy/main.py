import random

number = input("enter a number: ")
if number.isdigit():
    number = int(number)
    if number <=0:
        print("Please enter a larger number next time")
        quit()
else:
    print("please enter a number next time")
    quit()
r = random.randint(0,number)
guess = 0
while True:
    guess+=1
    user = input("Make a guess: ")
    if user.isdigit():
        user = int(user)
    else:
        print("please enter a number next time")
        continue
    if user == r:
        print("Congrats")
        break
    elif user > r:
        print("You were above the number")
    else:
        print("you are below the number")

print("You have guessed in: " + str(guess))





