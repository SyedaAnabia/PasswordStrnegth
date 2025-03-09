import streamlit as st
import re
import random

# Common weak passwords list
COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "password123", "admin", "letmein", "welcome"]

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return "❌ Too common! Choose a more secure password.", "Weak", 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters required.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase & lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*()_+=-]", password):
        score += 1
    else:
        feedback.append("❌ Include one special character (!@#$%^&*).")

    # Strength Rating with Progress Bar Score
    if score == 5:
        return "✅ Strong Password!", "Strong", 100
    elif score >= 3:
        return "⚠️ Moderate Password - Improve security.", "Moderate", 60
    else:
        return "\n".join(feedback), "Weak", 30

# Strong Password Generator (20 chars)
def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
    return ''.join(random.choice(characters) for _ in range(20))

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

st.markdown("<h1 style='text-align: center;'>🔐 Advanced Password Strength Checker</h1>", unsafe_allow_html=True)

# Show/Hide Password Feature
show_password = st.checkbox("👁 Show Password", value=False)
password = st.text_input("Enter your password:", type="text" if show_password else "password")

# Strength Indicator with Progress Bar
if password:
    feedback, strength, progress = check_password_strength(password)
    st.progress(progress / 100)  # Convert 0-100 to 0-1 for progress bar
    st.subheader(f"Strength: {strength}")
    st.write(feedback)

# Strong Password Generator Button
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text("🔑 Suggested Strong Password: " + strong_password)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
