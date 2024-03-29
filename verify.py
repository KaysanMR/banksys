def verify_email(email):
    if not email:
        return False

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
    else:
        return False


def verify_phone(phone):
    if not phone:
        return False

    length_error = len(str(phone)) != 10
    type_error = not phone.isnumeric()

    if type_error:
        print("Phone number must contain only numbers.")
    if length_error:
        print("Phone number must be 10 characters long.")

    if not any([length_error, type_error]):
        print("Phone number validated.")
        return phone
    else:
        return False


def verify_employment(choice):
    if not choice:
        return False

    data_error = choice not in ["working", "student", "unemployed"]

    if not data_error:
        print("Employment validated.")
        return choice
    else:
        print("Please enter either employed, student, or unemployed.")
        return False


def verify_address(address):
    if not address:
        return False

    character_error = ([not char.isalnum() and char != " " for char in list(address)])
    # print([not char.isalnum() and char != " " for char in list(address)])

    if not any(character_error):
        print("Address validated.")
        return address
    else:
        print("Address can only contain alphanumeric characters.")
        return False


def validate_attribute(properties, select):
    while True:  # verify input!!
        new_property = input(f"Enter new {properties[select]}: ")
        match select:
            case 0:
                if verify_email(new_property):
                    return new_property
            case 1:
                if verify_phone(new_property):
                    return new_property
            case 2:
                if verify_employment(new_property):
                    return new_property
            case 3:
                if verify_address(new_property):
                    return new_property
