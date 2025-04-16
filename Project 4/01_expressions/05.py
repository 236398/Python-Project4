def main():
    try:
        dividend = int(input("Please enter an integer to be divided: "))
        divisor = int(input("Please enter an integer to divide by: "))
        quotient = dividend // divisor
        remainder = dividend % divisor
        print(
            (
                f"The result of this division is {quotient} "
                f"with a remainder of {remainder}"
            )
        )
    except ValueError:
        print("Please enter valid integer values.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")


if __name__ == "__main__":
    main()
