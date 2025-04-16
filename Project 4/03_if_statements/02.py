age = int(input("How old are you? "))

# Voting ages for each country
peturksbouipo_age = 16
stanlau_age = 25
mayengua_age = 48

# Check eligibility for Peturksbouipo
if age >= peturksbouipo_age:
    print(f"You can vote in Peturksbouipo where the voting age is {peturksbouipo_age}.")
else:
    print(f"You cannot vote in Peturksbouipo where the voting age is {peturksbouipo_age}.")

# Check eligibility for Stanlau
if age >= stanlau_age:
    print(f"You can vote in Stanlau where the voting age is {stanlau_age}.")
else:
    print(f"You cannot vote in Stanlau where the voting age is {stanlau_age}.")

# Check eligibility for Mayengua
if age >= mayengua_age:
    print(f"You can vote in Mayengua where the voting age is {mayengua_age}.")
else:
    print(f"You cannot vote in Mayengua where the voting age is {mayengua_age}.")
