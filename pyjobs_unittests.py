""" Unit tests for script which scrapes Indeed.com
for job listings related to Python then outputs the
most common skills in those listings """

import unittest
import PythonJobs
import indeed

class SetupAPI(unittest.TestCase):

    def setUp(self):

        self.client = PythonJobs.setup_client(PythonJobs.PUBLISHER_ID)

    def test_setup_returns_client_object(self):

        '''setup_client should return indeed.IndeedClient object'''

        self.assertEqual(type(self.client),indeed.IndeedClient)

class SearchJobsAPI(unittest.TestCase):

    def setUp(self):

        self.client = PythonJobs.setup_client(PythonJobs.PUBLISHER_ID)
        self.num_results, self.list_of_results = PythonJobs.search_indeed(self.client, PythonJobs.PARAMS)

    def test_search_indeed_retuns_total_results_as_int(self):    

        self.assertIsInstance(self.num_results, int)

    def test_search_indeed_returns_list_of_results_as_list(self):
        
        self.assertIsInstance(self.list_of_results, list)

    def test_search_indeed_len_of_list_equals_num_results(self):

        self.assertEqual(len(self.list_of_results), self.num_results)

class ProcessAllJobs(unittest.TestCase):

    def setUp(self):

        self.client = PythonJobs.setup_client(PythonJobs.PUBLISHER_ID)
        self.num_results, self.list_of_results = PythonJobs.search_indeed(self.client, PythonJobs.PARAMS)
        self.jobs_list = PythonJobs.process_all_jobs(self.list_of_results)

        for key in self.jobs_list.keys():

            self.test_key = key

    def test_process_jobs_returns_list(self):

        self.assertIsInstance(self.jobs_list, dict)

    def test_process_jobs_returns_correct_items_in_list(self):

        self.assertIn(self.test_key, self.jobs_list)
        self.assertIn('title', self.jobs_list[self.test_key])
        self.assertIn('title_plus_snippet', self.jobs_list[self.test_key])
        
if __name__ == '__main__':
    unittest.main()











