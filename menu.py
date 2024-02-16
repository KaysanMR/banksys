from datetime import datetime
import accounts


def current_time():
    time = datetime.now().strftime("%H:%M:%S %Y-%m-%d")  # Format time to time, date format
    return time


def main_menu(data):
    while True:
        print("\n-----MENU-----")
        print(f"Welcome! It is currently {current_time()}")
        print("  1. Sign in")
        print("  2. Exit")
        choice = input("Enter your choice: \n> ")

        match choice:
            case "1":
                print("\n-----SIGN IN-----")
                user = accounts.login(data)
                user_menu(data, user)
            case "2":
                match input("\nAre you sure you want to exit? (y/n): > "):
                    case "y":
                        break
                    case "n":
                        continue
                    case _:
                        print("Invalid choice")
            case "admin":  # temp entry to admin menu
                admin_menu(data)
            case _:
                print("Invalid choice")


def admin_menu(data):
    while True:
        print("\n-----MENU-----")
        print("  1. Create account")
        print("  2. Manage accounts")
        print("  3. View logs")
        print("  4. Exit")
        choice = input("Enter your choice: > ")

        match choice:
            case "1":
                print("\n-----CREATE ACCOUNT-----")
                accounts.new_user(data)

            case "2":
                print("\n-----MANAGE ACCOUNTS-----")
                # Manage accounts

            case "3":
                print("\n-----LOGS-----")
                # Display logs

            case "4":
                match input("\nLog out? (y/n): > "):
                    case "y":
                        break
                    case "n":
                        continue
                    case _:
                        print("Invalid choice")

            case _:
                print("Invalid choice")


def user_menu(data, user):
    while True:
        print("\n-----MENU-----")
        print(f"Welcome, {user[1]}! It is currently {current_time()}")
        print("  1. My Account")
        print("  2. Deposit / Withdraw")
        print("  3. Bank Statement")
        print("  4. Exit")
        choice = input("Enter your choice: > ")

        match choice:
            case "1":
                print("\n-----MY ACCOUNT-----")
                accounts.view_user(user)

            case "2":
                print("\n-----DEPOSIT/WITHDRAW-----")
                # Deposit/Withdraw

            case "3":
                print("\n-----TRANSACTION HISTORY-----")
                # Display logs for user (in date range)

            case "4":
                match input("\nLog out? (y/n): > "):
                    case "y":
                        break
                    case "n":
                        continue
                    case _:
                        print("Invalid choice")

            case _:
                print("Invalid choice")


if __name__ == "__main__":
    current_time()
