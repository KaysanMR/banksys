def load(filename):
    try:
        with open(filename, "r") as file:
            content = file.readlines()
            data = [line.strip().split(",") for line in content]
            return data
    except FileNotFoundError:
        return None


def save(data, file="accounts.csv"):
    with open(file, "w") as file:
        for user in data:
            file.write(",".join(user) + '\n')


def write(data, file):
    with open(file, "a") as file:
        file.write(data)
