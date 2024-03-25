from datetime import datetime
from file_manager import save, load
from logger import log_entry

import display
import menu


def new_user(data, admin=False, session="SYSTEM"):
    username = None
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
                # balance = -100.00
            case "C":
                uid = new_id(username, admin, "current")
                # balance = -500.00
    else:
        uid = new_id(username, admin)
        balance = 0

    password = username[:3] + uid[8:]
    data.append([uid, username, password, balance])
    save(data, "accounts.csv") if not admin else save(data, "admin.csv")
    log_entry(f"created new user {uid} admin={admin}", session[0])
    print("Account created")


def new_id(username, admin=False, account_type="saving"):
    timestamp = round(datetime.timestamp(datetime.now()))
    identifier = username[:3].upper() + str(timestamp)
    if admin:
        identifier = identifier + "A"
    if account_type == "saving":
        identifier = identifier + "S"
    if account_type == "current":
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
                print("SUPERUSER MENU")  # add super menu
            case 1:
                session_user = validate_user(admin_list, user_id)
                if session_user:
                    log_entry(action=f"logged in as {session_user[0]}")
                    menu.admin_menu(user_list, session_user)
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


def view_user(user):
    print(f"ID:       {user[0]}\n"
          f"Username: {user[1]}")
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


def manage(data):
    # search & display results
    users = search(data)
    headings = ["UID", "USERNAME"]
    display.table(users, headings)
    # select user to edit
    while True:
        select = input("Select user #: ")
        if int(select) - 1 in range(len(users)):
            user = users[int(select) - 1]
            print(user)
            break
        else:
            print(f"Please select an item in range 1-{len(users) + 1}")
    # edit function here


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


if __name__ == "__main__":
    userlist = load("accounts.csv")
    manage(userlist)
