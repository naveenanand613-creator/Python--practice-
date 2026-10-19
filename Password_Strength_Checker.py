password = input("Enter your password: ")
if len(password) < 6:
    strength = "Weak"
elif password.isalnum() or password.isalpha():
    strength = "Medium"
else:
    strength = "Strong"
print("Password Length:", len(password))
print("Password Strength:", strength)
