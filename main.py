import accounts
import menu


def main():
    user_list = accounts.load("accounts.csv")
    admin_list = accounts.load("admin.csv")
    menu.main_menu(user_list, admin_list)


if __name__ == "__main__":
    main()
