import accounts
import display
import file_manager
import transaction
import logger
import bank_statement


def main_menu(user_list, admin_list):
    while True:
        display.box("MENU", 32)
        display.greet()
        print("  1. Sign in")
        print("  2. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("\n-----SIGN IN-----")
                accounts.login(user_list, admin_list)

            case "2":
                match input("\nAre you sure you want to exit? (y/n): "):
                    case "y":
                        break
                    case "n":
                        continue
                    case _:
                        print("Invalid choice")
            case _:
                print("Invalid choice")


def admin_menu(user_list, user):
    while True:
        display.box("ADMIN", 32)
        display.greet(user)
        print("  1. Create account")
        print("  2. Manage accounts")
        print("  3. View logs")
        print("  4. Exit")
        choice = input("Enter your choice: > ")

        match choice:
            case "1":
                print("\n-----CREATE ACCOUNT-----")
                accounts.new_user(user_list, admin=False, session=user)

            case "2":
                print("\n-----MANAGE ACCOUNTS-----")
                accounts.manage(user_list)

            case "3":
                print("\n-----LOGS-----")
                file_manager.view("log.txt")

            case "4":
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
                print("\n-----TRANSACTION HISTORY-----")
                bank_statement.filter_logs(user)

            case "4":
                transaction.perform_transfer(user, user_list)
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


if __name__ == "__main__":
    pass
