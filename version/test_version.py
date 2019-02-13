import unittest
from version import Utilities

class TestUtilities(unittest.TestCase):
    def test_check_version(self):
        expected = 'v3.2.1'
        self.assertIsNone(Utilities.check_version(expected))

        expected = None
        with self.assertRaises(AssertionError):
            Utilities.check_version(expected)

        expected = 'v'
        with self.assertRaises(AssertionError):
            Utilities.check_version(expected)

        expected = 1
        self.assertIsNone(Utilities.check_version(expected))

        expected = 12.2
        self.assertIsNone(Utilities.check_version(expected))

        expected = bytes('v3.2.1')
        self.assertIsNone(Utilities.check_version(expected))

        expected = bytes('v')
        with self.assertRaises(AssertionError):
            Utilities.check_version(expected)

    def test_get_major(self):
        get_major = Utilities.get_major

        actual = 10

        expected = get_major(10)
        self.assertEqual(actual, expected)

        expected = get_major('v10')
        self.assertEqual(actual, expected)

        expected = get_major(10.112)
        self.assertEqual(actual, expected)

        expected = get_major('v10.15.123')
        self.assertEqual(actual, expected)

        expected = get_major('10.13.0')
        self.assertEqual(actual, expected)

        expected = get_major('10.132')
        self.assertEqual(actual, expected)

    def test_get_minor(self):
        pass

    def test_get_patch(self):
        pass
