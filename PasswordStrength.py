import streamlit as st
import re
import random

# Common weak passwords list
COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "password123", "admin", "letmein"]

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return "❌ Too common! Choose a more secure password.", "Weak", "🔴"

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

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include one special character (!@#$%^&*).")

    # Strength Rating with color
    if score == 5:
        return "✅ Strong Password!", "Strong", "🟢"
    elif score >= 3:
        return "⚠️ Moderate Password - Improve security.", "Moderate", "🟡"
    else:
        return "\n".join(feedback), "Weak", "🔴"

# Strong Password Generator (16 chars)
def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
    return ''.join(random.choice(characters) for _ in range(16))

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

st.markdown("<h1 style='text-align: center;'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)

# Password Input Field
password = st.text_input("Enter your password:", type="password")

# Live Strength Indicator
if password:
    feedback, strength, color = check_password_strength(password)
    st.markdown(f"<h3 style='color: {color};'>Strength: {strength}</h3>", unsafe_allow_html=True)
    st.write(feedback)

# Strong Password Generator Button
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text("🔑 Suggested Strong Password: " + strong_password)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
