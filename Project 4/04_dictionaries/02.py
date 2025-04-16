def fruit_shop():
    fruits = {
        "apple": 1.50,
        "durian": 25.00,
        "jackfruit": 15.00,
        "kiwi": 2.00,
        "rambutan": 10.00,
        "mango": 3.00
    }
    
    total_cost = 0

    for fruit, price in fruits.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: "))
                if quantity >= 0:  
                    break
                else:
                    print("Please enter a non-negative number.")
            except ValueError:
                print("Please enter a valid number.")

        cost = price * quantity
        total_cost += cost

    print(f"\nYour total is ${total_cost:.1f}")

if __name__ == "__main__":
    fruit_shop()
