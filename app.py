import streamlit as st
from cryptography.fernet import Fernet
import json
import os

DB_FILE = "vault.json"
KEY_FILE = "secret.key"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return key

key = load_key()
fer = Fernet(key)

def load_vault():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_vault(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

st.title("🔒 My Secure Password Manager")

menu = ["Add Password", "View Passwords"]
choice = st.sidebar.selectbox("Menu", menu)

vault = load_vault()

if choice == "Add Password":
    st.subheader("Add New Password")
    site = st.text_input("Website/App Name")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Save"):
        if site and user and pwd:
            encrypted_pwd = fer.encrypt(pwd.encode()).decode()
            vault[site] = {"user": user, "pwd": encrypted_pwd}
            save_vault(vault)
            st.success(f"Saved for {site}!")
        else:
            st.error("All fields are required")

elif choice == "View Passwords":
    st.subheader("Your Saved Passwords")
    if not vault:
        st.info("No passwords saved yet.")
    else:
        for site, data in vault.items():
            with st.expander(site):
                st.write(f"**Username:** {data['user']}")
                decrypted_pwd = fer.decrypt(data['pwd'].encode()).decode()
                st.write(f"**Password:** {decrypted_pwd}")