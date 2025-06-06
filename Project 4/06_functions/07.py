def print_multiple(message, repeats):
    """
    Prints a message multiple times.
    
    Args:
        message (str): The message to print
        repeats (int): Number of times to print the message
    """
    for _ in range(repeats):
        print(message, end=" ")

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == "__main__":
    main()
