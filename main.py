import accounts


def main():
    userlist = accounts.load_users("accounts.txt")

    while True:
        print("\n-----MENU-----")
        print("1. Sign in")
        print("2. Create account")
        print("3. Exit")
        choice = int(input("Enter your choice: \n> "))

        match choice:
            case 1:
                print("\n-----SIGN IN-----")
                user = accounts.login(userlist)
                print(user)

            case 2:
                print("\n-----CREATE ACCOUNT-----")
                accounts.new_user(userlist)

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


if __name__ == "__main__":
    main()
