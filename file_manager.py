def load(filename):
    try:
        with open(filename, "r") as file:
            content = file.readlines()
            data = [line.strip().split(",") for line in content]
            # for user in data:
            #     if len(user) < 4:
            #         user.append(0)
            return data
    except FileNotFoundError:
        return None


def get(file="log.txt"):
    with open(file, "r") as file:
        return file.readlines()


def view(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
            input("Press ENTER to continue:")
    except FileNotFoundError:
        return None


def save(data, filename="accounts.csv"):
    with open(filename, "w") as file:
        for user in data:
            file.write(','.join(str(v) for v in user) + "\n")


def write(data, filename):
    with open(filename, "a") as file:
        file.write(data)


if __name__ == "__main__":
    users = load("accounts.csv")
    save(users)
