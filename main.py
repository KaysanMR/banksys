import accounts, menu


def main():
    userlist = accounts.load_users("accounts.txt")
    menu.main_menu(userlist)


if __name__ == "__main__":
    main()
