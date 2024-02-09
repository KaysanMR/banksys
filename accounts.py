from datetime import datetime


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
    save(data, "accounts.txt") if not admin else save(data, "admin.txt")
    print("Account created")


def set_pass(user, data):
    while True:
        password = input("Enter your password:")
        if input("Confirm password: ") == password:
            user[2] = password
            save(data)
            print("Password changed successfully.")
            break
        else:
            print("Passwords do not match.")


def load_users(filename):
    with open(filename, "r") as file:
        content = file.readlines()
        data = [line.strip('][\n').replace('\'', '').split(", ") for line in content]
        return data


def new_id(username, admin=False):
    timestamp = round(datetime.timestamp(datetime.now()))
    identifier = username[:3].upper() + str(timestamp)
    if admin:
        identifier = identifier + "A"
    return identifier


def save(data, file="accounts.txt"):
    with open(file, "w") as file:
        for user in data:
            file.write(repr([item for item in user]) + '\n')


def login(data):
    while True:
        uid = input("\nEnter your UID: ")

        try:
            user = [user for user in data if user[0] == uid][0]
            password = input("Enter your password: ")
            if password == user[2]:
                print("Logged in successfully.")
                return user
            else:
                print("Incorrect password, please try again.")

        except IndexError:
            print("UID does not match any known user. "
                  "\nPlease reach out to staff to create a new account.")


if __name__ == "__main__":
    userlist = load_users("accounts.txt")
    admins = load_users("admin.txt")
    print(admins)
    new_user(userlist)
