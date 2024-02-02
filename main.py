import accounts

userlist = accounts.load_users("accounts.txt")


def menu():
    while True:
        print("\n")
        print("1. Sign in")
        print("2. Create account")
        print("3. Exit")
        choice = int(input("Enter your choice: \n> "))

        match choice:
            case 1:
                print("sign in")
            case 2:
                print("\nCREATE ACCOUNT")
                accounts.new_user()
            case 3:
                match input("\nAre you sure you want to exit? (y/n) \n> "):
                    case "y":
                        break
                    case "n":
                        continue
                    case _:
                        print("Invalid choice")
            case _:
                print("Invalid choice")

            # menu()


print(userlist[0])
