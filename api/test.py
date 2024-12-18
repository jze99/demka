import unittest

class TestExample(unittest.TestCase):

    def test_success_1(self):
        self.assertEqual(1 + 1, 2)

    def test_success_2(self):
        self.assertTrue(True)

    def test_success_3(self):
        self.assertIn(3, [1, 2, 3])

    def test_success_4(self):
        self.assertIsNone(None)

    def test_success_5(self):
        self.assertGreater(5, 3)

    def test_failure_1(self):
        self.assertEqual(1 + 1, 3)  # Ошибка

    def test_failure_2(self):
        self.assertTrue(False)  # Ошибка

    def test_failure_3(self):
        self.assertIn(4, [1, 2, 3])  # Ошибка

    def test_failure_4(self):
        self.assertIsNone(1)  # Ошибка

    def test_failure_5(self):
        self.assertGreater(3, 5)  # Ошибка

if __name__ == "__main__":
    unittest.main()
