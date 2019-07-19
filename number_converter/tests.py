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

        with open("data/turkish_test_data.txt", "r") as f:
            data = f.read().splitlines()

        for number in range(0, 30000):
            turkish_text = TurkishText(number)
            turkish_text.convert_to_text()
            self.assertEqual(turkish_text.text, data[number])


if __name__ == "__main__":
    unittest.main()
