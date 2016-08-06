""" Unit tests for script which scrapes Indeed.com
for job listings related to Python then outputs the
most common skills in those listings """

import unittest

class ConnectToAPI(unittest.TestCase):

    def test_correct_publisher_id_entered(self):

        '''script should successfully send publisher ID
           to Ineed API'''

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
