def check_password(pw):
    strength = 0

    if len(pw) >= 8:
        strength += 1
    if any(char.isdigit() for char in pw):
        strength += 1
    if any(char.isupper() for char in pw):
        strength += 1
    if any(char in "!@#$%^&*" for char in pw):
        strength += 1

    if strength <= 2:
        print("Weak Password")
    elif strength == 3:
        print("Medium Password")
    else:
        print("Strong Password")

password = input("Enter password: ")
check_password(password)