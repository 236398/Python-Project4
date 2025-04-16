def count_even(lst):
    """
    Counts the number of even numbers in a list.
    
    Args:
        lst (list): List of integers
        
    Returns:
        int: Number of even numbers in the list
    """
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    return even_count

def get_user_input():
    """
    Gets integers from user until they press enter.
    
    Returns:
        list: List of integers entered by user
    """
    numbers = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Please enter a valid integer or press enter to stop")
    return numbers

def main():
    numbers = get_user_input()

    even_count = count_even(numbers)

    print(f"Number of even numbers: {even_count}")

if __name__ == "__main__":
    main()
