def convert_feet_to_inches(feet):
    return feet * 12


def main():
    while True:
        try:
            feet = float(input("Enter length in feet: "))
            unit = 'foot' if feet == 1 else 'feet'
            inches = convert_feet_to_inches(feet)
            print(f"{feet} {unit} is {inches} inches.\n")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()