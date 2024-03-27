from file_manager import write
from display import current_time


def log_entry(action, session="SYSTEM", file="log.txt"):
    log = f"{current_time(2)}: [{session}] {action}\n"
    write(log, file)


def log_transaction(from_user, to_user=None, amount=0, transaction_type=None):
    if transaction_type == "Transfer":
        log_entry(f"Transaction: {transaction_type}, from: {from_user[1]} to: {to_user[1]}, amount: {amount}", file="transaction_log.txt")
    else:
        log_entry(f"Transaction: {transaction_type}, user: {from_user[1]}, amount: {amount}", file="transaction_log.txt")



def filter_transaction_log(filter_criteria, transaction_log_entries):
    filtered_log = []

    for entry in transaction_log_entries:
        try:
            timestamp, details = entry.split(": ", 1)
            details_parts = details.split(", ")
            transaction_type = details_parts[0].split(": ")[1]

            # Adjust the parsing according to your log format
            from_user = details_parts[1].split(": ")[1] if len(details_parts) > 1 else None
            to_user = details_parts[2].split(": ")[1] if len(details_parts) > 2 else None
            amount = float(details_parts[3].split(": ")[1]) if len(details_parts) > 3 else None

            if (filter_criteria.get("date") and filter_criteria["date"] not in timestamp) or \
               (filter_criteria.get("transaction_type") and transaction_type != filter_criteria["transaction_type"]) or \
               (filter_criteria.get("from_user") and from_user and from_user != filter_criteria["from_user"]) or \
               (filter_criteria.get("to_user") and to_user and to_user != filter_criteria["to_user"]):
                continue

            filtered_log.append(entry)
        except IndexError:
            print(f"Skipping malformed log entry: {entry}")

    return filtered_log


def get_transaction_log():
    with open("transaction_log.txt", "r") as file:
        return file.readlines()


if __name__ == "__main__":
    pass
