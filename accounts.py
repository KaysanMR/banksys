from datetime import datetime

import logger
from file_manager import save, load
from logger import log_entry

import display
import menu
import verify


def new_user(data, admin=False, session="SYSTEM"):
    username = None
    balance = 0

    while not username:
        username = input("Enter username:")
        for user in data:
            try:
                if username == user[1]:
                    print("Username already exists, please try again.")
                    username = None
            except IndexError:
                continue

    if not admin:
        match input("Select account type:\n"
                    "S -> Savings\n"
                    "C -> Current\n"
                    "Enter selection: ").upper():
            case "S":
                uid = new_id(username, admin, "saving")
            case "C":
                uid = new_id(username, admin, "current")

    else:
        uid = new_id(username, admin)

    password = username[:3] + uid[8:]
    user = [uid, username, password, balance]
    data.append(user)
    save(data, "accounts.csv") if not admin else save(data, "admin.csv")

    if not admin: add_info(user, data)

    log_entry(f"created new user {uid} admin={admin}", session[0])
    print("Account created")


def new_id(username, admin=False, acct_type="saving"):
    timestamp = round(datetime.timestamp(datetime.now()))
    identifier = username[:3].upper() + str(timestamp)
    if admin:
        identifier = identifier + "A"
    else:
        if acct_type == "saving":
            identifier = identifier + "S"
        if acct_type == "current":
            identifier = identifier + "C"
    return identifier


def check_admin(user_id):
    if user_id:
        if user_id == "SUPERUSER_A":
            return 0
        elif user_id[-1] == "A":
            return 1
        else:
            return 2


def login(user_list, admin_list):
    while True:
        user_id = input("\nEnter your UID: ")
        if user_id.upper() == "X": return

        match check_admin(user_id):
            case 0:
                session_user = validate_user([["SUPERUSER_A", "SUPERUSER", "Ac355-c0d3"]], user_id)
                if session_user:
                    log_entry(action=f"logged in as {session_user[0]}")
                    menu.super_menu(admin_list, ["SUPERUSER", "SUPERUSER"])
                    return session_user
            case 1:
                session_user = validate_user(admin_list, user_id)
                if session_user:
                    log_entry(action=f"logged in as {session_user[0]}")
                    menu.admin_menu(user_list, session_user, admin_list)
                    return session_user
            case 2:
                session_user = validate_user(user_list, user_id)
                if session_user:
                    menu.user_menu(session_user, user_list)
                    return session_user


def validate_user(data, user_id):
    try:
        user = [user for user in data if user[0] == user_id][0]  # fetch username from data
        password = input("Enter your password: ")
        if password == user[2]:
            print("Logged in successfully.")
            return user
        else:
            print("Incorrect password, please try again.")

    except IndexError:
        print("UID does not match any known user. "
              "\nEnter <X> to exit.")
        return None


def view_user(user, pause=True):
    print(f"ID:          {user[0]}")
    print(f"Username:    {user[1]}")
    print(f"Email:       {user[4]}")
    print(f"Phone:       {user[5]}")
    print(f"Occupation:  {user[6]}")
    print(f"Address:     {user[7]}")
    if pause:
        input("\nPress ENTER / RETURN to exit.")


def search(data):
    results = None
    repeat = False
    while not results:
        if repeat:
            print("No results for search term, please try again.")
        keyword = input("Search username or user ID: ").upper()
        results = [item for item in data if
                   keyword in item[0].upper() or
                   keyword in item[1].upper()]
        repeat = True
    return results


def select_account(data, session):
    # search & display results
    users = search(data)
    headings = ["UID", "USERNAME"]
    display.table(users, headings)
    # select user to edit
    while True:
        if len(users) == 1:
            select = 1
        else:
            select = input("Select user #: ")
        if int(select) - 1 in range(len(users)):
            user = users[int(select) - 1]
            view_user(user, pause=False)
            return user
        else:
            print(f"Please select an item in range 1-{len(users) + 1}")


def add_info(user, data):
    print("Updating details for user:", user[1])
    email, phone, address, employment = None, None, None, None

    while not verify.verify_email(email):
        email = input("Enter email address: ")

    while not verify.verify_phone(phone):
        phone = input("Enter phone number: ")

    while not verify.verify_address(address):
        address = input("Enter home address: ")

    while not verify.verify_employment(employment):
        employment = input("Select employment status (working/student/unemployed): ").lower()

    user.extend([email, phone, employment, address])
    save(data, "accounts.csv")

    print("User details updated.")


def edit_account(user, session):
    while True:
        print("\n1. Email")
        print("2. Phone number")
        print("3. Employment Status")
        print("4. Address")
        print("X. Exit\n")
        while True:
            match input("Select an attribute (1-4) to edit: "):
                case "1":
                    edit_attribute(user, 0, session)
                    break
                case "2":
                    edit_attribute(user, 1, session)
                    break
                case "3":
                    edit_attribute(user, 2, session)
                    break
                case "4":
                    edit_attribute(user, 3, session)
                    break
                case x if x.upper() == "X":
                    return
                case _:
                    print("Invalid input, please choose a number (1-4).")


def edit_attribute(user, select, session):
    index = select + 4
    properties = ["email", "phone number", "employment status", "address"]
    print(f"Current {properties[select]}: {user[index]}")

    new_property = verify.validate_attribute(properties, select)

    if new_property:
        while True:
            confirm = input(f"Change {properties[select]} to {new_property}? (y/n): ")
            if confirm.upper() == "Y":
                user[index] = new_property
                logger.log_entry(f"updated {user[0]}'s {properties[select]} to {new_property}", session[0])
                print(f"updated {properties[select]} to {new_property}.")
                break
            elif confirm.upper() == "N":
                return
            else:
                print("Invalid choice. Please enter (y/n).")


def change_password(user):
    while True:
        new_password = input("Enter new password: ")
        confirm = input("Are you sure you want to change password? (y/n): ")
        if confirm.upper() == "Y":
            user[2] = new_password
            return user
        elif confirm.upper() == "N":
            return
        else:
            print("Invalid input. Please select y/n. ")


def account_type(identifier):
    match identifier[-1]:
        case "S":
            return "savings"
        case "C":
            return "current"
        case "A":
            return "admin"
        case _:
            return None
