def print_even_odd_sequence(start, end):
    """
    Prints a sequence of numbers with their even/odd status.
    
    Args:
        start (int): Starting number
        end (int): Ending number (inclusive)
    """
    for num in range(start, end + 1):
        status = "even" if num % 2 == 0 else "odd"
        print(f"{num} {status}", end=" ")

def main():
    print_even_odd_sequence(10, 19)

if __name__ == "__main__":
    main()
