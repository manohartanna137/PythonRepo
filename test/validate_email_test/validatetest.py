import unittest
from src.validate_email_address_14.utils import validate_email

class TestValidateEmail(unittest.TestCase):

    def test_valid_email(self):
        email = 'user@example.com'
        result = validate_email(email)
        self.assertTrue(result)




if __name__ == '__main__':
    unittest.main()
