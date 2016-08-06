""" Unit tests for script which scrapes Indeed.com
for job listings related to Python then outputs the
most common skills in those listings """

import unittest
import PythonJobs
import indeed


PUBLISHER_ID = 8263932719076827

PARAMS = {
            'q' : "python",
            'l' : "19067",
            'userip' : "1.2.3.4",
            'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"}

class SetupAPI(unittest.TestCase):

    def test_setup_returns_client_object(self):

        '''setup_client should return indeed.IndeedClient object'''

        self.assertEqual(type(PythonJobs.setup_client(PUBLISHER_ID)),indeed.IndeedClient)

class SearchJobsAPI(unittest.TestCase):

    def test_total_results_returns_a_value(self):

        '''job search results should return a value'''

        self.assertTrue(PythonJobs.find_total_results(PUBLISHER_ID, PARAMS))

if __name__ == '__main__':
    unittest.main()
