import string

def check_password_strength(password):

    score = 0
    feedback = []

   
    if len(password) < 8:
        print("Result: WEAK - Password is too short (minimum 8 characters needed)")
        return
    elif len(password) >= 12:
        score += 2
    else:
        score += 1

    # Rule 2: Check for uppercase letters
    has_upper = any(char.isupper() for char in password)
    if has_upper:
        score += 1
    else:
        feedback.append("add uppercase letters")

    # Rule 3: Check for numbers
    has_digit = any(char.isdigit() for char in password)
    if has_digit:
        score += 1
    else:
        feedback.append("add numbers")

    # Rule 4: Check for special symbols
    has_symbol = any(char in string.punctuation for char in password)
    if has_symbol:
        score += 1
    else:
        feedback.append("add special symbols like @, #, !")

    # Final result based on score
    if score <= 2:
        strength = "WEAK"
    elif score == 3:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    print(f"\nPassword: {password}")
    print(f"Result: {strength}")

    if feedback:
        print("Tips to improve: " + ", ".join(feedback))
    else:
        print("Great password! No improvements needed.")


# Main program
print("=== Password Strength Checker ===")
user_password = input("Enter your password: ")
check_password_strength(user_password)
