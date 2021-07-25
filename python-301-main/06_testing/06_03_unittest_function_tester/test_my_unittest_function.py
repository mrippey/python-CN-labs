import unittest
import requests
from requests.api import patch
from my_unittest_function import connect_to_site
class TestFunc(unittest.TestCase):

    def test_http_resp_200(self):
        self.assertEqual(connect_to_site('https://python.org'), 200)

    def test_requests_exception(self):
       with self.assertRaises(requests.exceptions.RequestException):
           connect_to_site('google.com')

    def test_that_will_not_pass(self):
        with self.assertRaises(ValueError):
            connect_to_site('https://google.com')

   

if __name__ == "__main__":
    unittest.main(verbosity=2)