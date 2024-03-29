from file_manager import write
from display import current_time
from datetime import datetime

def log_entry(action, session="SYSTEM", file="log.txt"):
    log = f"{current_time(2)}: [{session}] {action}\n"
    write(log, file)


def log_transaction(from_user, to_user=None, amount=0, transaction_type=None):
    if transaction_type == "Transfer":
        log_entry(f"Transaction: {transaction_type}, from: {from_user[1]} to: {to_user[1]}, amount: {amount}",
                  file="transaction_log.txt")
    else:
        log_entry(f"Transaction: {transaction_type}, user: {from_user[1]}, amount: {amount}",
                  file="transaction_log.txt")

def get_transaction_log():
    with open("transaction_log.txt", "r") as file:
        return file.readlines()



def filter_transaction_log(transaction_log_entries, user, start_date=None, end_date=None):
    filtered_log = []

    for entry in transaction_log_entries:
        try:
            date_str, details = entry.split(",", 1)[0].split(" ", 1)
            entry_date = datetime.strptime(date_str, "%Y-%m-%d").date()

            if user not in details:
                continue

            if start_date and end_date:
                start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
                end_dt = datetime.strptime(end_date, "%Y-%m-%d").date()
                if not (start_dt <= entry_date <= end_dt):
                    continue

            filtered_log.append(entry)
        except Exception as e:
            print(f"Error processing entry: {entry}, Error: {e}")

    return filtered_log







if __name__ == "__main__":
    account1 = "Kaysan"
    account2 = "Bakyt"
    amount = 500.00
    print("bar")
    log_entry(f"{account1} transferred {amount} to {account2}", file="transactions.txt")
    print("foo")
