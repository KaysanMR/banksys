from file_manager import write
from display import current_time


def log_entry(action, session="SYSTEM", file="log.txt"):
    log = f"{current_time(2)}: [{session}] {action}\n"
    write(log, file)


if __name__ == "__main__":
    account1 = "Kaysan"
    account2 = "Bakyt"
    amount = 500.00
    print("bar")
    log_entry(f"{account1} transferred {amount} to {account2}", file="transactions.txt")
    print("foo")
