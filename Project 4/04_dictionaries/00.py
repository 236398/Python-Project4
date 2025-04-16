def count_numbers():
    numbers = []
    print("Enter numbers (press Enter without typing anything to finish):")
    
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number!")

    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    for num, count in sorted(frequency.items()):
        print(f"{num} appears {count} times.")

if __name__ == "__main__":
    count_numbers()
