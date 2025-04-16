def affirmation_checker():
    target_affirmation = "I am capable of doing anything I put my mind to."
    
    while True:
        print("Please type the following affirmation:", target_affirmation)
        user_input = input()
        if user_input == target_affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation.")

if __name__ == "__main__":
    affirmation_checker()
