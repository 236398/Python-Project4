def calculate_energy(mass):
    """
    Calculates energy using Einstein's mass-energy equivalence formula.
    Args:
        mass (float): The mass in kilograms.
    Returns:
        float: The equivalent energy in joules.
    """
    C = 299792458  # Speed of light in m/s
    return mass * C ** 2


def main():
    """
    Continuously prompts the user for mass and calculates the equivalent 
    energy.
    """
    while True:
        try:
            mass = float(input("Enter kilos of mass: "))
            energy = calculate_energy(mass)
            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print("C = 299792458 m/s")
            print(f"{energy} joules of energy!\n")
        except ValueError:
            print("Please enter a valid numerical mass value.")

# Execute the main function


if __name__ == "__main__":
    main()