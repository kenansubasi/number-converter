
class NumberHelper(object):
    """
    This class includes helper methods and values.
    """
    digit_values = {}
    step_values = {}
    extra_values = {}

    def __init__(self, number):
        self.number = str(number)
        self.text = ""

    def convert_number_part_to_text(self, number_part, step):
        raise NotImplementedError

    def convert_to_text(self):
        """
        This method converts the given number to text.
        It divides the number into groups of 3 first.
        It then sends these sections to the convert_number_part_to_text function.
        As a result, it fills the text variable.
        """
        if self.number.isdigit() is False:
            pass
        elif self.number == "0":
            self.text = self.digit_values.get(self.number, "")
        else:
            reversed_number = "".join(reversed(self.number))
            number_list = [reversed_number[i:i+3] for i in range(0, len(reversed_number), 3)]

            for step, number_part in enumerate(number_list):
                self.text = "{number_part_text}{old_text}".format(
                    number_part_text=self.convert_number_part_to_text(number_part, step),
                    old_text=self.text)


class TurkishText(NumberHelper):
    """
    This class includes the Turkish text equivalent of numbers and the function that
    converts them into Turkish.
    """
    digit_values = {
        "0": "sıfır",
        "1": "bir",
        "2": "iki",
        "3": "üç",
        "4": "dört",
        "5": "beş",
        "6": "altı",
        "7": "yedi",
        "8": "sekiz",
        "9": "dokuz",
        "10": "on",
        "20": "yirmi",
        "30": "otuz",
        "40": "kırk",
        "50": "elli",
        "60": "altmış",
        "70": "yetmiş",
        "80": "seksen",
        "90": "doksan"
    }
    extra_values = {
        "hundred": "yüz",
    }
    step_values = {
        0: "",
        1: "bin",
        2: "milyon",
        3: "milyar",
        4: "trilyon",
        5: "katrilyon",
        6: "kentilyon"
    }


    def convert_number_part_to_text(self, number_part, step):
        """
        It returns Turkish text for the given number part.
        @params {String} number_part ("123")
        @params {Integer} step (1 = bin)
        """
        part_text = ""
        len_number_part = len(number_part)

        for index, value in enumerate(number_part):
            if value == "0":
                pass
            elif index == 0:
                if not ((len_number_part == 1 and value == "1" or number_part == "100") and step == 1):
                    part_text = self.digit_values.get(value, "") + part_text
            elif index == 1:
                part_text = self.digit_values.get(value + "0", "") + part_text
            elif index == 2:
                part_text = self.extra_values.get("hundred", "") + part_text
                if value != "1":
                    part_text = self.digit_values.get(value, "") + part_text

        if number_part != "000":
            part_text = part_text + self.step_values.get(step, "")

        return part_text
