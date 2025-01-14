from password import Password
from cracker import Cracker
from secret import PASSWORD


def main():
    password = Password(PASSWORD)
    cracker = Cracker(password=password, trials=10000)

    cracker.crack_password()


if __name__ == "__main__":
    main()
