import accounts
import menu


def main():
    userlist = accounts.load_users("accounts.txt")
    admins = accounts.load_users("admin.txt")
    menu.main_menu(userlist, admins)


if __name__ == "__main__":
    main()
