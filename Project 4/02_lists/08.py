MAX_LENGTH = 3

def shorten(lst):
    """
    Removes elements from the end of lst until it is MAX_LENGTH items long.
    Prints each removed element.
    If lst is already shorter than MAX_LENGTH, leaves it unchanged.
    
    Args:
        lst (list): The list to be shortened
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(removed_item)

def main():
    values = []
    
    while True:
        user_input = input("Enter a value: ")
        if user_input == "":
            break
        values.append(user_input)
    
    print("\nShortening list...")
    shorten(values)
    print("Final list:", values)

if __name__ == "__main__":
    main()
