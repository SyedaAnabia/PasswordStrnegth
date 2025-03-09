import re
import random

# Common weak passwords list
COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "password123"]

# Function to check password strength
def check_password_strength(password):
    score = 0
    
    # Check if password is in common passwords list
    if password.lower() in COMMON_PASSWORDS:
        print("❌ This password is too common! Choose a more secure one.")
        return

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        print("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        print("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        print("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        print("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 5:
        print("✅ Strong Password!")
    elif score >= 3:
        print("⚠️ Moderate Password - Consider adding more security features.")
    else:
        print("❌ Weak Password - Improve it using the suggestions above.")

# Function to generate a strong password
def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# User Input
password = input("Enter your password: ")
check_password_strength(password)

# Suggest strong password if needed
if input("Do you want a strong password suggestion? (yes/no): ").lower() == "yes":
    print("🔑 Suggested Strong Password: ", generate_strong_password())
