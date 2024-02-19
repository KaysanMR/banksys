import accounts
import menu


def main():
    userlist = accounts.load_file("accounts.txt")
    menu.main_menu(userlist)


if __name__ == "__main__":
    main()
