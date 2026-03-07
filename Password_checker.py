import re

# Common passwords list
common_passwords = ["123456", "password", "12345678", "qwerty", "abc123"]

password = input("Enter your password: ")

score = 0
suggestions = []

# Check common password
if password in common_passwords:
    print("\n⚠ WARNING: This is a very common password!")
    score = 0
else:

    # Length
    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase
    if re.search("[A-Z]", password):
        score += 20
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase
    if re.search("[a-z]", password):
        score += 20
    else:
        suggestions.append("Add lowercase letters")

    # Numbers
    if re.search("[0-9]", password):
        score += 20
    else:
        suggestions.append("Include numbers")

    # Special characters
    if re.search("[@#$%^&*!]", password):
        score += 20
    else:
        suggestions.append("Add special characters")

# Progress bar
bars = score // 10
progress = "█" * bars + "░" * (10 - bars)

print("\nPassword Strength")
print(f"[{progress}] {score}%")

# Strength level
if score < 40:
    print("Strength Level: WEAK")
    print("Estimated crack time: Few seconds")
elif score < 80:
    print("Strength Level: MEDIUM")
    print("Estimated crack time: Few hours")
else:
    print("Strength Level: STRONG")
    print("Estimated crack time: Years")

# Suggestions
if suggestions:
    print("\nSuggestions to improve:")
    for s in suggestions:
        print("-", s)
