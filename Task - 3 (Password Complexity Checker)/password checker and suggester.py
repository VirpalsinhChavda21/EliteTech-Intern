import re
from collections import Counter

def password_strength(password):
    strength = {
        "Length": len(password) >= 8,
        "Uppercase": bool(re.search(r'[A-Z]', password)),
        "Lowercase": bool(re.search(r'[a-z]', password)),
        "Digit": bool(re.search(r'[0-9]', password)),
        "Special Char": bool(re.search(r'[\W_]', password))
    }
    
    if all(strength.values()):
        return "Strong password", None
    elif sum(strength.values()) >= 3:
        return "Moderate password", generate_suggested_password(password)
    else:
        return "Weak password", generate_suggested_password(password)

def generate_suggested_password(password):
    suggested_password = password

    # Ensure there's at least one uppercase letter
    if not any(char.isupper() for char in suggested_password):
        suggested_password = suggested_password.capitalize()

    # Ensure there's at least one special character
    if not any(char in "!@#$%^&*()_+=-[]{}|;:,.<>?/~" for char in suggested_password):
        suggested_password += "@"

    # Get digits from the original password
    digits = re.findall(r'\d', password)
    
    # If there are digits, use them to strengthen the password
    if digits:
        # Count the occurrences of each digit
        digit_counts = Counter(digits)
        # Get the most common digit
        most_common_digit = digit_counts.most_common(1)[0][0]
        
        # Add the most common digit repeated to reach the minimum length
        while len(suggested_password) < 12:
            suggested_password += most_common_digit
    else:
        # If no digits in the original password, add '123'
        suggested_password += "123"

    return f"Suggested stronger password: {suggested_password}"

# User input
password = input("Enter password to check: ")
strength, suggestion = password_strength(password)

print(strength)
if suggestion:
    print(suggestion)
else:
    print("Your password is already strong!")