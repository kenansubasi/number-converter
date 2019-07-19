import unittest

from helper import TurkishText


class TestNumber(unittest.TestCase):
    """
    Test cases for the converted number to text.
    """

    def test_convert_to_text_turkish(self):
        """
        It tests the Turkish text equivalent of the number.
        """

        # 0 - 999
        with open("data/turkish/test_data_hundred.txt", "r") as f:
            data = f.read().splitlines()

        for number in range(0, 1000):
            turkish_text = TurkishText(number)
            turkish_text.convert_to_text()
            self.assertEqual(turkish_text.text, data[number])

        # 1000 - 111000
        with open("data/turkish/test_data_thousand.txt", "r") as f:
            data = f.read().splitlines()

        for number in range(1000, 111001):
            turkish_text = TurkishText(number)
            turkish_text.convert_to_text()
            self.assertEqual(turkish_text.text, data[number-1000])

        # 1000000 - 1111000
        with open("data/turkish/test_data_million.txt", "r") as f:
            data = f.read().splitlines()

        for number in range(1000000, 1111001):
            turkish_text = TurkishText(number)
            turkish_text.convert_to_text()
            self.assertEqual(turkish_text.text, data[number-1000000])


if __name__ == "__main__":
    unittest.main()
