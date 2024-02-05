def new_user(userlist):
    while True:
        username = input("Enter your username:")
        for user in userlist:
            if username in userlist:
                print("foo")

        password = input("Enter your password:")
        if input("Confirm password: ") == password:
            print("Account created")
            userlist.append([new_id(), username, password])
            # write(f"{new_id()}, {username}, {password}" + '\n')
            break
        else:
            print("Passwords do not match.")

def write(text):
    with open("accounts.txt", "a") as file:
        return file.write(text)


def load_users(filename):
    with open(filename, "r") as file:
        content = file.readlines()
        return [line.strip().split(',') for line in content]


def new_id():
    return "ABC123"


