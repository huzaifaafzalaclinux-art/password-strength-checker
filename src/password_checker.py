import re


def check_password(password):

    if len(password) < 12:
        return False, "Password must be at least 12 characters long."

    if not re.search(r"[A-Z]", password):
        return False, "Add at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Add at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return False, "Add at least one number."

    if not re.search(r"[^A-Za-z0-9]", password):
        return False, "Add at least one special character."

    common_passwords = [
        "password",
        "password123",
        "12345678",
        "123456789",
        "qwerty",
        "admin",
        "admin123"
    ]

    if password.lower() in common_passwords:
        return False, "This is a common password. Choose a different one."

    return True, "Strong password!"


def main():

    print("=" * 50)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 50)

    print("\nPassword requirements:")
    print("- At least 12 characters")
    print("- At least 1 uppercase letter")
    print("- At least 1 lowercase letter")
    print("- At least 1 number")
    print("- At least 1 special character")

    while True:

        password = input("\nEnter a complex password: ")

        strong, message = check_password(password)

        if strong:
            print("\n[+] PASSWORD ACCEPTED")
            print("[+] " + message)
            break

        else:
            print("\n[-] PASSWORD REJECTED")
            print("[-] " + message)
            print("[-] Please try again.")

    print("\n[+] PASSWORD CHECK COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    main()