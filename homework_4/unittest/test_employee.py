import unittest
from unittest.mock import patch
from employee import Employee


class TestForClass(unittest.TestCase):
    def setUp(self):
        self.TestClass = Employee('Carl', 'Johnson', 120)

    def test_email(self):
        self.assertEqual(self.TestClass.email, 'Carl.Johnson@email.com')
        self.assertIn(self.TestClass.email, 'AasdsdfserCarl.Johnson@email.comsdfsfdf')

    def test_fullname(self):
        self.assertEqual(self.TestClass.fullname, 'Carl Johnson')
        self.assertTrue(self.TestClass.fullname)

    def test_apply_raise(self):
        self.assertEqual(self.TestClass.pay, 120)
        self.TestClass.apply_raise()
        self.assertEqual(self.TestClass.pay, 126)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.text = 'Good_work'
        self.assertEqual(self.TestClass.monthly_schedule('january'), 'Good_work')


if __name__ == '__main__':
    unittest.main()
