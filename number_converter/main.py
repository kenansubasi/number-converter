from helper import TurkishText


def main():
    """
    This block runs the code.
    It takes user's input and calls necessary methods then show the response.
    """
    while True:
        while True:
            number = input("\nPlease enter a number: ")
            if number.isdigit() is True:
                if len(number) > 21:
                    print("\n\033[1;32;91mPlease enter a value less than {number}!\033[0;37;40m".format(number=10**21))
                elif len(number) > 1 and number.startswith("0"):
                    print("\n\033[1;32;91mThe value you entered is incorrect!\033[0;37;40m")
                else:
                    break
            else:
                print("\n\033[1;32;91mThe value you entered is incorrect!\033[0;37;40m")

        turkish_text = TurkishText(number)
        turkish_text.convert_to_text()

        print("\n\033[1;32;40mNumber: {number}\033[0;37;40m".format(number=number))
        print("\033[1;32;40mTurkish: {text}\033[0;37;40m".format(text=turkish_text.text))

        while True:
            choice = input("\nDo you want to recalculate? [Y]/N: ")

            if choice in ["", "y", "Y", "n", "N"]:
                break
            else:
                print("\n\033[1;32;91mPlease enter a correct option!\033[0;37;40m")

        if choice in ["n", "N"]:
            exit()


if __name__ == "__main__":
    main()
