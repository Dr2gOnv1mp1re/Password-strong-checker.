import re
import random
import string

# Function to check password strength
def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add digits.")

    if re.search(r"\W", password):
        strength += 1
    else:
        feedback.append("Add special characters.")

    return strength, feedback

# Function to generate a strong password
def generate_strong_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(12))

# Main interactive script
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    strength, suggestions = check_password_strength(user_password)

    if strength == 5:
        strength_label = "Very Strong"
    elif strength >= 3:
        strength_label = "Moderate"
    else:
        strength_label = "Very Weak"

    print("\n----- Password Strength Result -----")
    print(f"Password         : {user_password}")
    print(f"Strength         : {strength_label} ({strength}/5)")

    if suggestions:
        print("Suggestions      :")
        for s in suggestions:
            print(f" - {s}")

    print(f"Strong Password  : {generate_strong_password()}")
