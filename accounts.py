def new_user(userlist):
    while True:
        username = None
        while not username:
            username = input("Enter your username:")
            for user in userlist:
                if username == user[1]:
                    print("Username already exists, please try again.")
                    username = None
                    continue

        password = input("Enter your password:")
        if input("Confirm password: ") == password:
            print("Account created")
            userlist.append([new_id(), username, password])

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


def new_id():
    return "ABC123"


def save(data):
    for x in data:
        write(f"{[user for user in data]}" + '\n')


# userlist = load_users("accounts.txt")
# print(userlist)
# for i in range(3):
#     new_user(userlist)
#     print(userlist)
