import random


def roll_dice():
    """
    Simulates rolling a six-sided die.
    Returns:
        int: A random integer between 1 and 6.
    """
    return random.randint(1, 6)


def roll_two_dice():
    """
    Rolls two six-sided dice.
    Returns:
        tuple: A tuple containing two integers representing the dice rolls.
    """
    return roll_dice(), roll_dice()


def print_roll_results(roll_number, die1, die2):
    """
    Prints the results of a dice roll.
    Args:
        roll_number (int): The current roll number.
        die1 (int): The value of the first die.
        die2 (int): The value of the second die.
    """
    print(f"Roll {roll_number}: Die 1 = {die1}, Die 2 = {die2}")


def main():
    """
    Simulates rolling two dice three times and prints the results.
    """
    num_rolls = 3  # Define the number of rolls
    
    for i in range(1, num_rolls + 1):
        die1, die2 = roll_two_dice()
        print_roll_results(i, die1, die2)

# Execute the main function


if __name__ == "__main__":
    main()
