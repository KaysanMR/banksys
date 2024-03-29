import accounts
import display
import file_manager
import transaction
from filter_logs import filter_logs


def main_menu(user_list, admin_list):
    while True:
        display.box("MENU", 32)
        display.greet()
        print("  1. Sign in")
        print("  X. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("\n-----SIGN IN-----")
                accounts.login(user_list, admin_list)

            case x if x.upper() == "X":
                match input("\nAre you sure you want to exit? (y/n): "):
                    case "y":
                        break
                    case "n":
                        continue
                    case _:
                        print("Invalid choice")
            case _:
                print("Invalid choice")


def admin_menu(user_list, user, admin_list):
    while True:
        display.box("ADMIN", 32)
        display.greet(user)
        print("  1. Create account")
        print("  2. Manage accounts")
        print("  3. View logs")
        print("  4. Generate User Bank Statement")
        print("  5. Change Password")
        print("  X. Exit")
        choice = input("Enter your choice: > ")

        match choice:
            case "1":
                print("\n-----CREATE ACCOUNT-----")
                accounts.new_user(user_list, admin=False, session=user)

            case "2":
                print("\n-----MANAGE ACCOUNTS-----")
                customer = accounts.select_account(user_list, session=user)
                accounts.edit_account(customer, session=user)
                file_manager.save(user_list)

            case "3":
                print("\n-----LOGS-----")
                filter_logs(user, file="log.txt")

            case "4":
                print("\n-----GENERATE BANK STATEMENT-----")
                customer = accounts.select_account(user_list, session=user)
                filter_logs(customer, file="transaction_log.txt")
                print(f"{customer[1]}'s CURRENT BALANCE: {user[3]}")

            case "5":
                print("\n-----CHANGE PASSWORD-----")
                accounts.change_password(user)
                file_manager.save(admin_list, filename="admin.csv")

            case x if x.upper() == "X":
                match input("\nLog out? (y/n): "):
                    case "y":
                        break
                    case "n":
                        continue
                    case _:
                        print("Invalid choice")

            case _:
                print("Invalid choice")


def user_menu(user, user_list):
    while True:
        display.box("BANKING", 32)
        display.greet(user)
        print("  1. My Account")
        print("  2. Deposit / Withdraw")
        print("  3. Bank Statement")
        print("  4. Transfer Funds")
        print("  5. Change Password")
        print("  X. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("\n-----MY ACCOUNT-----")
                accounts.view_user(user)

            case "2":
                print("\n-----DEPOSIT/WITHDRAW-----")
                while True:
                    action = input("Deposit or Withdraw? (d/w): ")
                    if action.lower() == 'd':
                        amount = float(input("Enter amount: "))
                        transaction.deposit(user, amount)
                        break
                    elif action.lower() == 'w':
                        amount = float(input("Enter amount: "))
                        transaction.withdraw(user, amount)
                        break
                    else:
                        print("Invalid choice")
                file_manager.save(user_list)

            case "3":
                print("\n-----GENERATE BANK STATEMENT-----")
                filter_logs(user, file="transaction_log.txt")
                print(f"CURRENT BALANCE: {user[3]}")

            case "4":
                transaction.perform_transfer(user, user_list)
                file_manager.save(user_list)

            case "5":
                print("\n-----CHANGE PASSWORD-----")
                accounts.change_password(user)
                file_manager.save(user_list)

            case x if x.upper() == "X":
                match input("\nLog out? (y/n): "):
                    case "y":
                        break
                    case "n":
                        continue
                    case _:
                        print("Invalid choice")

            case _:
                print("Invalid choice")


def super_menu(admin_list, user):
    while True:
        display.box("ADMIN", 32)
        display.greet(user)
        print("  1. Create admin account")
        print("  2. View logs")
        print("  X. Exit")
        choice = input("Enter your choice: > ")

        match choice:
            case "1":
                print("\n-----CREATE ACCOUNT-----")
                accounts.new_user(admin_list, admin=True, session=user)

            case "2":
                print("\n-----LOGS-----")
                filter_logs(user, file="log.txt")

            case x if x.upper() == "X":
                match input("\nLog out? (y/n): "):
                    case "y":
                        break
                    case "n":
                        continue
                    case _:
                        print("Invalid choice")

            case _:
                print("Invalid choice")


if __name__ == "__main__":
    pass
