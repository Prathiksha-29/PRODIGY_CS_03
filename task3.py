import re

def assess_password_strength(password):
    # Define criteria for strong password
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'[0-9]', password)
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Assess the password strength
    if length_criteria and uppercase_criteria and lowercase_criteria and number_criteria and special_char_criteria:
        strength = "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and (number_criteria or special_char_criteria):
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide feedback based on the strength
    feedback = "Password Strength: " + strength + "\n"
    if not length_criteria:
        feedback += "- Password should be at least 8 characters long.\n"
    if not uppercase_criteria:
        feedback += "- Password should contain at least one uppercase letter.\n"
    if not lowercase_criteria:
        feedback += "- Password should contain at least one lowercase letter.\n"
    if not number_criteria:
        feedback += "- Password should contain at least one number.\n"
    if not special_char_criteria:
        feedback += "- Password should contain at least one special character.\n"

    return feedback

# Example usage
password = input("Enter your password to assess its strength: ")
print(assess_password_strength(password))
