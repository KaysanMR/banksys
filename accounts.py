from datetime import datetime


def new_user(data):
    username = None
    while not username:
        username = input("Enter username:")
        for user in data:
            if username == user[1]:
                print("Username already exists, please try again.")
                username = None

    uid = new_id(username)
    password = username[:3] + uid[8:]

    data.append([uid, username, password])
    save(data)


def set_pass(user):
    while True:
        password = input("Enter your password:")
        if input("Confirm password: ") == password:
            print("Account created")
            user[2] = password
            break
        else:
            print("Passwords do not match.")


def load_users(filename):
    with open(filename, "r") as file:
        content = file.readlines()
        data = [line.strip('][\n').replace('\'', '').split(", ") for line in content]
        return data


def new_id(username):
    timestamp = round(datetime.timestamp(datetime.now()))
    identifier = username[:3].upper() + str(timestamp)
    return identifier


def save(data):
    with open("accounts.txt", "w") as file:
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
    print(userlist)
    login(userlist)

