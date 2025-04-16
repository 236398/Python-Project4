def double_numbers(numbers):
    """
    Double each element in a list of numbers.
    
    Args:
        numbers (list): A list of numbers to be doubled
        
    Returns:
        list: A new list with each element doubled
    """
    return [num * 2 for num in numbers]


if __name__ == "__main__":
  
    test_list1 = [1, 2, 3, 4]
    test_list2 = [0, -1, 2.5, 10]
    test_list3 = [100, 200, 300]
    
    print(f"Original list: {test_list1}")
    print(f"Doubled list: {double_numbers(test_list1)}")
    print()
    
    print(f"Original list: {test_list2}")
    print(f"Doubled list: {double_numbers(test_list2)}")
    print()
    
    print(f"Original list: {test_list3}")
    print(f"Doubled list: {double_numbers(test_list3)}")
