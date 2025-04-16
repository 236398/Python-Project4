def double(num):
    """
    Returns the result of multiplying num by 2.
    
    Args:
        num (float): The number to double
        
    Returns:
        float: The input number multiplied by 2
    """
    return num * 2

def main():
    num = float(input("Enter a number: "))

    result = double(num)

    print(f"Double that is {result}")

if __name__ == "__main__":
    main()
