from datetime import datetime

# def get_transaction_log():
#     with open("transaction_log.txt", "r") as file:
#         return file.readlines()
#
#
# def get_validated_date(prompt):
#     while True:
#         date_input = input(prompt)
#         try:
#             datetime.strptime(date_input, "%Y-%m-%d")
#             return date_input
#         except ValueError:
#             print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
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


if __name__ == "__main__":
    pass
