import random

def guess_number():
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        try:
            guess = int(input("Enter a guess: "))
            
            if guess == secret_number:
                print(f"Congrats! The number was: {secret_number}")
                break
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print("Your guess is too low")
                
        except ValueError:
            print("Please enter a valid number between 0 and 99")

if __name__ == "__main__":
    guess_number() 