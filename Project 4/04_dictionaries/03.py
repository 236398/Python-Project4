import hashlib

def hash_password(password):
    """
    Hashes a password using SHA256 algorithm.
    
    Args:
        password (str): The password to hash
        
    Returns:
        str: The hexadecimal digest of the hashed password
    """
    hash_object = hashlib.sha256(password.encode())
 return hash_object.hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Verify if the provided password matches the stored hash for the given email.
    
    Args:
        email (str): The email to check
        password_to_check (str): The password to verify
        stored_logins (dict): Dictionary containing email:password_hash pairs
        
    Returns:
        bool: True if login is successful, False otherwise
    """
    if email not in stored_logins:
        return False

    stored_hash = stored_logins[email]

    password_hash = hash_password(password_to_check)

    return password_hash == stored_hash

if __name__ == "__main__":

    stored_logins = {
        "user1@example.com": hash_password("securepass1"),
        "user2@example.com": hash_password("strongpass2"),
        "admin@example.com": hash_password("adminpass123")
    }

    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Invalid email or password.")

    print("\nDemonstrating password hashing:")
    print(f"Hash of 'hello': {hash_password('hello')}")
    print(f"Hash of 'Hello': {hash_password('Hello')}")  
