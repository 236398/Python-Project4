def get_last_element(lst):
    """
    Print the last element of the given list.
    The list is guaranteed to be non-empty.
    
    Args:
        lst (list): A non-empty list
    """
    print(lst[-1])

def main():
    user_list = []
    
    n = int(input("How many elements would you like to enter? "))
    
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)
    
    print("\nThe last element is:", end=" ")
    get_last_element(user_list)

if __name__ == "__main__":
    main()
