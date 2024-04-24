import driver
import utils
import sys


if __name__ == "__main__":
    utils.print_navigation()
    option = utils.get_user_choice()
    driver = driver.SoteraDriver()

    match option:
        case 1:
            driver.login()

        case 2:
            driver.register()

        case _:
            sys.exit(1)
