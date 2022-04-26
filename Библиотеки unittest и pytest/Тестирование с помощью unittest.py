import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_one(self):
        self.assertEqual(reverse('a'), 'a')

    def test_pol(self):
        self.assertEqual(reverse('aba'), 'aba')

    def test_str(self):
        self.assertEqual(reverse('abc'), 'cba')

    def test_wrong_type_int(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_wrong_type_list(self):
        with self.assertRaises(TypeError):
            reverse(list('abc'))


if __name__ == '__main__':
    unittest.main()
