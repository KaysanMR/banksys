import accounts
import menu


def main():
    user_list = accounts.load("accounts.txt")
    admin_list = accounts.load("admin.txt")
    menu.main_menu(user_list, admin_list)


if __name__ == "__main__":
    main()
