import unittest
from datetime import date
from main import calculate_age, is_leap_year, parse_birthdate, render_stars, weekday_name


class BirthdateTests(unittest.TestCase):
    def test_date_validation(self):
        self.assertEqual(parse_birthdate(29, 2, 2024, date(2024, 11, 8)), date(2024, 2, 29))
        with self.assertRaises(ValueError):
            parse_birthdate(29, 2, 2023, date(2024, 11, 8))
        with self.assertRaises(ValueError):
            parse_birthdate(1, 1, 2030, date(2024, 11, 8))

    def test_leap(self):
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1900))
        self.assertTrue(is_leap_year(2024))

    def test_weekday(self):
        self.assertEqual(weekday_name(date(2024, 11, 8)), 'пятница')

    def test_age(self):
        self.assertEqual(calculate_age(date(2000, 11, 9), date(2024, 11, 8)), 23)
        self.assertEqual(calculate_age(date(2000, 11, 8), date(2024, 11, 8)), 24)

    def test_render(self):
        output = render_stars('09 11 2024')
        self.assertEqual(len(output.splitlines()), 7)
        self.assertIn('*', output)
        with self.assertRaises(ValueError):
            render_stars('09.11.2024')


if __name__ == '__main__':
    unittest.main()
