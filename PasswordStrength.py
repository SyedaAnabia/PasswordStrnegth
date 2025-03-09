import re
import random

# Common weak passwords list
COMMON_PASSWORDS = {"password", "123456", "qwerty", "abc123", "password123", "letmein", "welcome", "admin", "123456789"}

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Blacklist Check
    if password.lower() in COMMON_PASSWORDS:
        return "❌ Too common! Choose a secure password.", "Weak 😞", 1

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase & lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include one special character (!@#$%^&*).")

    # Strength Rating
    if score == 5:
        return "✅ Strong Password! 😎", "Strong", 5
    elif score >= 3:
        return "⚠️ Moderate Password 😐 - Consider adding more security features.", "Moderate", score
    else:
        return "\n".join(feedback), "Weak 😞", score

# Strong Password Generator (20 chars)
def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Get user input
password = input("Enter your password: ")
message, strength, score = check_password_strength(password)

print("\n🔍 Password Analysis:")
print(message)

if strength == "Weak 😞":
    print("\n💡 Suggestion: Try this strong password →", generate_strong_password())
elif strength == "Strong":
    print("🎉 Your password is secure!")
