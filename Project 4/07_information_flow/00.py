ADULT_AGE = 18

def is_adult(age):
    if age >= ADULT_AGE:
        return True
    else:
        return False

user_age_str = input("How old is this person?: ")
user_age = int(user_age_str)
result = is_adult(user_age)
print(result)
