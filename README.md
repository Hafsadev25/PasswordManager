# Password Manager 🔐

This is a small Python project I built to keep all my passwords in one place, securely, without trusting any website.

 What it does
- Save new passwords: For things like Gmail, Facebook, etc.
- Get passwords back: Just type the service name and it gives you the password.
- It's encrypted: I used the `cryptography` library, so everything in `vault.json` is encrypted. No one can read it without the key.

 How to run it
Super simple to run on your laptop:
1.  Download the code
2.  In your terminal, run: `pip install cryptography` 
3.  Then run: `python app.py`

 Important note
I’ve used a `.gitignore` file so that `secret.key` and `vault.json` never get uploaded to GitHub by mistake. Those two files stay only on your laptop.

---
I learned about encryption and file handling while building this. Right now it's a command-line tool. My next plan is to turn it into a Flask web app.
