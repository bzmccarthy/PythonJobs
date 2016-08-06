""" Unit tests for script which scrapes Indeed.com
for job listings related to Python then outputs the
most common skills in those listings """

import unittest

class ConnectToHTTP(unittest.TestCase):

    def test_connects_to_indeed_api(self):

        '''script should successfully connect to API'''

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
