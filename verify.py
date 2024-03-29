def verify_email(email):
    valid_domains = ["gmail.com", "outlook.com", "live.com", "hotmail.com", "mail.apu.edu.my"]

    specials = [char for char in list(email) if not char.isalnum()]

    def check_format():
        if email.rfind("@") < 1:
            return True
        elif specials.index(".") < specials.index("@") and specials[-1] != ".":
            return True
        elif len([i for i in specials if i == "@"]) > 1:  # count repeats of @
            return True
        elif [i for i in specials if i != "@" and i != "."]:
            return True
        else:
            return False

    def check_length():
        if 7 >= len(email) >= 45:
            return True
        else:
            return False

    def check_chars():
        if email.isdigit():
            return True
        elif not email.islower():
            return True
        else:
            return False

    def check_domain():
        error = False
        if email.find("@") > 0:
            email_domain = email.split("@")[1]
        for domain in valid_domains:
            if email.find(domain) > 0:
                error = False
                break
            else:
                error = True
        return error

    format_error = check_format()
    length_error = check_length()
    character_error = check_chars()
    domain_error = check_domain()

    if format_error:
        print("Email must be in the format name@domain.com, with no additional special characters.")

    if length_error:
        print("Email address must be between 7 and 45 characters long.")

    if character_error:
        print("Email address cannot contain capital letters, and cannot contain only numbers.")

    if domain_error:
        print(f"Please enter an email for one of the valid domains, {valid_domains}")

    if not any([format_error, length_error, character_error, domain_error]):
        print("Email Validated.")
        return email


def verify_phone(phone):
    pass


def main():
    while True:
        email_address = input("Enter email address to validate: ")
        verify_email(email_address)


if __name__ == "__main__":
    main()
