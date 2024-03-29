from datetime import datetime


def current_time(select=1):
    format_1 = "%H:%M:%S %Y-%m-%d"
    format_2 = "%Y-%m-%d %H:%M:%S"
    choice = format_1 if select == 1 else format_2
    return datetime.now().strftime(choice)  # format time to time, date format


def greet(user=None):
    if user:
        print(f"Welcome, {user[1]}! It is currently {current_time()}")
    else:
        print(f"Welcome! It is currently {current_time()}")


def table(data, headings, cell_width=15):
    cell = str("{:^" + str(cell_width) + "}│")  # create format string "{:^n}"
    format_row = "│{:^4}│" + cell * (len(headings))
    divider_line = ("────",) + (("─" * cell_width),) * len(headings)
    # start printing table
    print(format_row.format("#", *headings))
    print(format_row.format(*divider_line))
    for index, item in enumerate(data):
        print(format_row.format(index + 1, *item))
    print("\n")


def box(content, width):
    print("\n")
    text_box = str("│{:^" + str(width) + "}│")
    print(f"┼{"─" * width}┼")
    print(text_box.format(content))
    print(f"┼{"─" * width}┼")


def confirm_exit():
    while True:
        confirm = input("Are you sure you want to exit? (y/n): ")
        if confirm.upper() == "Y":
            return True
        elif confirm.upper() == "N":
            return False
        else:
            print("Invalid input, please try again.")
