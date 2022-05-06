import random

def play():
    print("Welcome to Guess The Number game!\n")

    number = random.randrange(1,10)
    attempts = 5

    for round in range (1, attempts +1):
        print("\nAttempt {} of {}".format(round, attempts))
        guess = int(input("Insert your guess number: "))
        print("Your guess is ", guess)

        right = guess == number
        higher = guess > number
        lower = guess < number

        if(right):
            print("\nYou found the secret number! You WIN!")
            break

        else:
            if(higher):
                print("\nTry again! Your guess is higher than the secret number.")
            elif(lower):
                print("\nTry again! Your guess is lower than the secret number.")

    print("=== END GAME ===")

if(__name__ == "__main__"):
    play()

