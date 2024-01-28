def create():
  username = input("Enter your username:")
  password = input("Enter your password:")
  if input("Confirm password: ") ==  password:
    print("Account created")
    return [username, password]
  else:
    print("Passwords do not match")
    return create()

def store(credentials):
  with open("accounts.txt", "a") as file:
    file.write(', '.join(credentials) + '\n')


store(create())

  