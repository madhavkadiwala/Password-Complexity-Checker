import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase letter
    if re.search(r"[a-z]", password):
        score += 1

    # Number
    if re.search(r"[0-9]", password):
        score += 1

    # Special character
    if re.search(r"[@$!%*?&]", password):
        score += 1

    # Final result
    if score <= 2:
        return "❌ Weak Password"
    elif score == 3 or score == 4:
        return "⚠️ Medium Password"
    else:
        return "✅ Strong Password"


# -------- MAIN PROGRAM --------
password = input("Enter your password: ")
result = check_password_strength(password)
print("Password Strength:", result)
