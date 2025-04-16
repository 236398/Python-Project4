def add_three_copies(lst, data):
    """
    Adds three copies of the given data to the list.
    Note: This function modifies the list in place and doesn't return anything.
    """
    lst.append(data)
    lst.append(data)
    lst.append(data)

def main():
    message = input("Enter a message to copy: ")
    
    my_list = []
    
    print("\nList before:", my_list)
    
    add_three_copies(my_list, message)
    
    print("List after:", my_list)

if __name__ == "__main__":
    main()
