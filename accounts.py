from datetime import datetime


def new_user(data):
    username = None
    while not username:
        username = input("Enter username:")
        for user in data:
            if username == user[1]:
                print("Username already exists, please try again.")
                username = None
            else:
                break

    uid = new_id(username)
    password = uid[:6]
    data.append([uid, username, password])


def set_pass(user):
    while True:
        password = input("Enter your password:")
        if input("Confirm password: ") == password:
            print("Account created")
            user[2] = password
            break
        else:
            print("Passwords do not match.")


def write(text):
    with open("accounts.txt", "a") as file:
        return file.write(text)


def load_users(filename):
    with open(filename, "r") as file:
        content = file.readlines()
        return [line.strip().split(', ') for line in content]


def new_id(username):
    timestamp = round(datetime.timestamp(datetime.now()))
    identifier = username[:3].upper() + str(timestamp)
    return identifier


def save(data):
    for x in data:
        write(f"{[user for user in data]}" + '\n')


if __name__ == "__main__":
    userlist = load_users("accounts.txt")
    print(userlist)
    new_user(userlist)
    print(userlist)
