import streamlit as st
import re

def get_bg_image():
    bg_image_url = "https://source.unsplash.com/random/1600x900/?technology,security"
    st.markdown(f"""
        <style>
            .stApp {{
                background: url('{bg_image_url}') no-repeat center center fixed;
                background-size: cover;
            }}
        </style>
    """, unsafe_allow_html=True)

def check_password_strength(password):
    strength = "Weak"
    color = "red"
    score = 0
    
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    
    if score == 1 or score == 2:
        strength = "Weak"
        color = "red"
    elif score == 3:
        strength = "Moderate"
        color = "orange"
    elif score >= 4:
        strength = "Strong"
        color = "green"
    
    return strength, color, score

def main():
    st.set_page_config(page_title="Password Strength Meter", layout="centered")
    get_bg_image()
    
    st.markdown("<h1 style='text-align: center; color: white;'>🔒 Password Strength Meter</h1>", unsafe_allow_html=True)
    
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        strength, color, score = check_password_strength(password)
        st.markdown(f"<h3 style='color: {color}; text-align: center;'>Strength: {strength}</h3>", unsafe_allow_html=True)
        
        # Progress bar from 0 to 1
        st.progress(score / 5.0)

if __name__ == "__main__":
    main()
