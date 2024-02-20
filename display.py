from datetime import datetime
import accounts


def current_time():
  return datetime.now().strftime("%H:%M:%S %Y-%m-%d")  # Format time to time, date format


def greet(user=None):
  if user:
    print(f"Welcome, {user[1]}! It is currently {current_time()}")
  else:
    print(f"Welcome! It is currently {current_time()}")


def table(data, headings, cell_width=15):
  cell = str("{:^" + str(cell_width) + "}￨")
  format_row = "￨{:^3}￨" + cell * (len(headings))

  print(format_row.format("#", *headings))
  print(format_row.format(*("---",) + (("-" * cell_width),) * len(headings)))
  for index, item in enumerate(data):
    print(format_row.format(index + 1, *item))


if __name__ == "__main__":
  users = accounts.load("accounts.txt")
  headers = ["UID", "USERNAME"]
  table(users, headers)
