from datetime import datetime, date
from file_manager import get


def filter_logs(user):
    uid = user[0]
    logs = get("transaction_log.txt")
    filtered_logs = [log for log in logs if uid in log]
    while True:
        print("1. Filter Last n entries")
        print("2. Filter entries by date")
        print("X. Exit")

        choice = input("Select an option (1/2/X): ")

        match choice:
            case "1":
                while True:
                    amount = input("Show how many entries?: ")
                    if amount.isnumeric():
                        # print(f"Showing last {amount} entries:\n")
                        try:
                            [print(log) for log in filtered_logs[-int(amount):]]  # last n items in filtered_logs
                        except IndexError:
                            [print(log) for log in filtered_logs]
                        break
            case "2":
                start_date, end_date = get_dates()
                logs_in_range = []
                for log in filtered_logs:
                    log_date = split_date(log[:10])
                    if start_date <= log_date <= end_date:
                        logs_in_range.append(log)
                [print(log) for log in logs_in_range]

            case x if x.upper() == "X":
                return


def get_dates():
    while True:
        print("Enter start date: ")
        start_date = split_date(validate_date())

        print("Enter end date: ")
        end_date = split_date(validate_date())

        if end_date > start_date:
            break
        else:
            print("End date must be after start date.")

    return start_date, end_date


def split_date(date_string):
    year, month, day = [int(item) for item in date_string.split("-")]
    return date(year, month, day)


def validate_date():
    while True:
        date_input = input()
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Please enter a date in YYYY-MM-DD format.")


if __name__ == "__main__":
    filter_logs(["HOU1708434041S", 0, 0])


#
#
# def filter_transaction_log_menu(transaction_log_entries, user):
#     print("1. Display all transactions for user")
#     print("2. Display all transactions for user within a date range")
#     choice = input("Enter your choice: ")
#
#     start_date = end_date = None
#     if choice == "2":
#         start_date = get_validated_date("Enter start date (YYYY-MM-DD): ")
#         end_date = get_validated_date("Enter end date (YYYY-MM-DD): ")
#
#     filtered_log = filter_transaction_log(transaction_log_entries, user, start_date, end_date)
#
#     if filtered_log:
#         print("Filtered Transaction Log:")
#         for entry in filtered_log:
#             print(entry)
#     else:
#         print("No transactions found for the specified criteria.")
#
#
# def print_filtered_log(filtered_log):
#     if filtered_log:
#         print("Filtered Transaction Log:")
#         for entry in filtered_log:
#             print(entry)
#     else:
#         print("No transactions found for the specified criteria.")
#
#
# def filter_transaction_log(transaction_log_entries, user, start_date=None, end_date=None):
#     filtered_log = []
#
#     for entry in transaction_log_entries:
#         try:
#             date_str, details = entry.split(",", 1)[0].split(" ", 1)
#             entry_date = datetime.strptime(date_str, "%Y-%m-%d").date()
#
#             if user not in details:
#                 continue
#
#             if start_date and end_date:
#                 start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
#                 end_dt = datetime.strptime(end_date, "%Y-%m-%d").date()
#                 if not (start_dt <= entry_date <= end_dt):
#                     continue
#
#             filtered_log.append(entry)
#         except Exception as e:
#             print(f"Error processing entry: {entry}, Error: {e}")
#
#     return filtered_log


