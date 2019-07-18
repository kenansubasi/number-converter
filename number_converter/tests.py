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

        # 123
        turkish_text = TurkishText(123)
        turkish_text.convert_to_text()
        self.assertEqual(turkish_text.text, "yüzyirmiüç")

        # 2145
        turkish_text = TurkishText(2145)
        turkish_text.convert_to_text()
        self.assertEqual(turkish_text.text, "ikibinyüzkırkbeş")

        # 15040
        turkish_text = TurkishText(15040)
        turkish_text.convert_to_text()
        self.assertEqual(turkish_text.text, "onbeşbinkırk")

        # 501147
        turkish_text = TurkishText(501147)
        turkish_text.convert_to_text()
        self.assertEqual(turkish_text.text, "beşyüzbirbinyüzkırkyedi")


if __name__ == "__main__":
    unittest.main()
