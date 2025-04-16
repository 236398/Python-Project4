import math


def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


def main():
    try:
        a = float(input("Enter the length of AB: "))
        b = float(input("Enter the length of AC: "))
        hypotenuse = calculate_hypotenuse(a, b)
        print(f"The length of BC (the hypotenuse) is: {hypotenuse}")
    except ValueError:
        print("Please enter valid numerical values.")


if __name__ == "__main__":
    main()
