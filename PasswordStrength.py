import streamlit as st
import re
import random
import pyperclip

# Common weak passwords list
COMMON_PASSWORDS = ["password", "123456", "qwerty", "abc123", "password123", "letmein", "welcome", "admin"]

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return "❌ Too common! Choose a secure password.", "Weak 😞", 0, "red"

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

    # Strength Rating with Emoji & Progress Color
    if score == 5:
        return "✅ Strong Password! 😎", "Strong", 100, "green"
    elif score >= 3:
        return "⚠️ Moderate Password 😐 - Improve security.", "Moderate", 60, "orange"
    else:
        return "\n".join(feedback), "Weak 😞", 30, "red"

# Strong Password Generator (20 chars)
def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
    return ''.join(random.choice(characters) for _ in range(20))

# Copy password to clipboard
def copy_to_clipboard(password):
    pyperclip.copy(password)

# Streamlit UI
st.set_page_config(page_title="🔐 Password Strength Checker", page_icon="🔒", layout="centered")

# Custom CSS for Neon Look
st.markdown("""
    <style>
    body { background-color: #121212; color: white; text-align: center; }
    h1 { color: #00FFD1; text-align: center; }
    .stTextInput>div>div>input { border: 2px solid #00FFD1; border-radius: 10px; padding: 10px; }
    .stButton>button { background: #00FFD1; color: black; font-size: 18px; border-radius: 8px; }
    .stProgress>div>div { border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🔐 Cyberpunk Password Strength Meter</h1>", unsafe_allow_html=True)

# Password Input Field
password = st.text_input("Enter your password:", type="password")

# Live Strength Indicator with Colored Progress Bar & Emoji
if password:
    feedback, strength, progress, color = check_password_strength(password)
    st.progress(progress / 100)  # Convert 0-100 to 0-1 for progress bar
    st.markdown(f"<h3 style='color: {color};'>Strength: {strength}</h3>", unsafe_allow_html=True)
    st.write(feedback)

# Strong Password Generator Button
if st.button("🛠 Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text("🔑 Suggested Strong Password: " + strong_password)
    if st.button("📋 Copy Password to Clipboard"):
        copy_to_clipboard(strong_password)
        st.success("✅ Password Copied!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #00FFD1;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
