def generate_email_address(first_name, last_name):
    """
    Generates a default Kean email address based on the first name and last name.
    The default Kean email address consists of the first letter of the first name,
    a period, the entire last name all in lower case appended with @kean.edu.
    """
    email_address = f"{first_name[0].lower()}.{last_name.lower()}@kean.edu"
    return email_address


def generate_password(last_name, birth_year, security_answer):
    """
    Generates a default password based on the first name, security question answer, and birthyear.
    The default password is a sequence of 3 letters from last name, birthyear,
    and 3 letters from the security question answer all in upper case.
    """
    password = f"{last_name[-3:].upper()}{birth_year}{security_answer[:3].upper()}"
    return password


def main():
    # Prompt user for personal information
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    security_answer = input("(Security Question) Favorite car maker: ")
    birth_year = input("Enter birth year: ")

    # Generate default email address and password
    email_address = generate_email_address(first_name, last_name)
    password = generate_password(last_name, birth_year, security_answer)

    # Display email information
    print(f"{first_name} {last_name}")
    print(f"Kean email: {email_address}")
    print(f"Kean password: {password}")


if __name__ == '__main__':
    main()
d