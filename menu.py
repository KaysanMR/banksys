import accounts
import display
import file_manager
import transaction
from transaction import transfer_funds
from logger import filter_transaction_log, log_transaction

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

# ... other imports ...

def perform_transfer(user, user_list):
    recipient_id = input("Enter the recipient's account ID: ")
    recipient = next((u for u in user_list if u[0] == recipient_id), None)

    if recipient is None:
        print("Recipient not found.")
        return

    while True:
        try:
            amount = float(input("Enter the amount to transfer: "))
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            break
        except ValueError as e:
            print("Invalid amount. Please enter a numeric value. Error: ", e)

    transfer_funds(user, recipient, amount, user_list)
    file_manager.save(user_list)




def user_menu(user, user_list):
    while True:
        display.box("BANKING", 32)
        display.greet(user)
        print("  1. My Account")
        print("  2. Deposit / Withdraw")
        print("  3. Bank Statement")
        print("  4. Transfer Funds")
        print("  5. Filter Transaction Log")
        print("  6. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("\n-----MY ACCOUNT-----")
                accounts.view_user(user)

            case "2":
                print("\n-----DEPOSIT/WITHDRAW-----")
                action = input("Deposit or Withdraw? (d/w): ")
                amount = float(input("Enter amount: "))
                if action.lower() == 'd':
                    transaction.deposit(user, amount)
                elif action.lower() == 'w':
                    transaction.withdraw(user, amount)
                else:
                    print("Invalid choice")
                file_manager.save(user_list)

            case "3":
                print("\n-----TRANSACTION HISTORY-----")
                transaction.generate_statement(user)

            case "6":
                match input("\nLog out? (y/n): "):
                    case "y":
                        break
                    case "n":
                        continue
                    case _:
                        print("Invalid choice")
            case "4":
                perform_transfer(user, user_list)
            case "5":
                filter_transaction_log_menu()

            case _:
                print("Invalid choice")

# if __name__ == "__main__":
def filter_transaction_menu():
    print("Filter Transaction Log Menu:")
    print("1. Filter by Date")
    print("2. Filter by Transaction Type")
    print("3. Filter by Sender")
    print("4. Filter by Receiver")
    print("5. Return to Previous Menu")
    choice = input("Enter your choice: ")
    return choice

def filter_transaction_log_menu():
    while True:
        choice = filter_transaction_menu()
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            transaction_log = log_transaction()
            filtered_log = filter_transaction_log({"date": date}, transaction_log)
            print_filtered_log(filtered_log)
        elif choice == "2":
            transaction_type = input("Enter transaction type: ")
            transaction_log = log_transaction()
            filtered_log = filter_transaction_log({"transaction_type": transaction_type}, transaction_log)
            print_filtered_log(filtered_log)
        elif choice == "3":
            sender = input("Enter sender username: ")
            transaction_log = log_transaction()
            filtered_log = filter_transaction_log({"from_user": sender}, transaction_log)
            print_filtered_log(filtered_log)
        elif choice == "4":
            receiver = input("Enter receiver username: ")
            transaction_log = log_transaction()
            filtered_log = filter_transaction_log({"to_user": receiver}, transaction_log)
            print_filtered_log(filtered_log)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")





def print_filtered_log(filtered_log):
    if filtered_log:
        print("Filtered Transaction Log:")
        for entry in filtered_log:
            print(entry)
    else:
        print("No transactions found for the specified criteria.")