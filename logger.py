from file_manager import write
from display import current_time


def log_entry(action, session="SYSTEM", file="log.txt"):
    log = f"{current_time(2)}: [{session}] {action}\n"
    write(log, file)


def log_transaction(from_user, to_user=None, amount=0, transaction_type=None):
    if transaction_type == "Transfer":
        log_entry(f"Transaction: {transaction_type}, from: {from_user[0]} to: {to_user[0]}, amount: {amount}",
                  file="transaction_log.txt")
    else:
        log_entry(f"Transaction: {transaction_type}, user: {from_user[0]}, amount: {amount}",
                  file="transaction_log.txt")
