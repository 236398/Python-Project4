def subtract_seven(num):
    return num - 7

def main():
    number = int(input("Enter a number: "))
    result = subtract_seven(number)
    print(f"{number} minus 7 is {result}")

if __name__ == "__main__":
    main()
