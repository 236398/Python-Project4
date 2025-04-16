def sum_numbers(numbers):
    """
    Calculate the sum of numbers in a list.
    
    Args:
        numbers (list): A list of numbers to be summed
        
    Returns:
        float: The sum of all numbers in the list
    """
    return sum(numbers)

if __name__ == "__main__":

    test_list1 = [1, 2, 3, 4, 5]
    test_list2 = [10.5, 20.3, 30.7]
    test_list3 = [-1, 0, 1]
    
    print(f"Sum of {test_list1}: {sum_numbers(test_list1)}")
    print(f"Sum of {test_list2}: {sum_numbers(test_list2)}")
    print(f"Sum of {test_list3}: {sum_numbers(test_list3)}")
