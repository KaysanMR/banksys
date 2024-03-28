from file_manager import write
from display import current_time
from datetime import datetime1

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


from datetime import datetime

def filter_transaction_log(transaction_log_entries, user, start_date=None, end_date=None):
    filtered_log = []

    for entry in transaction_log_entries:
        try:
            parts = entry.split(", ")
            timestamp_part, user_part = parts[0].split(": "), parts[1]
            timestamp_str = timestamp_part[0] + " " + timestamp_part[1]
            log_user = user_part.split(": ")[1]

            if log_user != user:
                continue

            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            if start_date and end_date:
                start_dt = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
                end_dt = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
                if not (start_dt <= timestamp <= end_dt):
                    continue

            filtered_log.append(entry)
        except (IndexError, ValueError):
            print(f"Skipping log entry: {entry}")

    return filtered_log







def get_transaction_log():
    with open("transaction_log.txt", "r") as file:
        return file.readlines()


if __name__ == "__main__":
    pass
