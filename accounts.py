from datetime import datetime
from file_manager import save, load
from logger import log_function

import display
import menu


@log_function
def new_user(data, admin=False):
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

    uid = new_id(username, admin)
    password = username[:3] + uid[8:]

    data.append([uid, username, password])

    save(data, "accounts.csv") if not admin else save(data, "admin.csv")
    print("Account created")
    return [uid, username, password]


def new_id(username, admin=False):
    timestamp = round(datetime.timestamp(datetime.now()))
    identifier = username[:3].upper() + str(timestamp)
    if admin:
        identifier = identifier + "A"
    return identifier


def check_admin(user_id):
    if user_id == "SUPERUSER_A":
        return 0
    elif user_id[-1] == "A":
        return 1
    else:
        return 2


@log_function
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
                    menu.admin_menu(user_list, session_user)
                    return session_user
            case 2:
                session_user = validate_user(user_list, user_id)
                if session_user:
                    menu.user_menu(session_user)
                    return session_user


@log_function
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


if __name__ == "__main__":
    userlist = load("accounts.csv")
    manage(userlist)
