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
            break

    def test_process_jobs_returns_list(self):

        self.assertIsInstance(self.jobs_list, dict)

    def test_process_jobs_returns_correct_items_in_list(self):

        self.assertIn(self.test_key, self.jobs_list)
        self.assertIn('title', self.jobs_list[self.test_key])
        self.assertIn('title_plus_snippet', self.jobs_list[self.test_key])

    def test_process_jobs_title_plus_snippet_is_list(self):

        self.assertIsInstance(self.jobs_list[self.test_key]['title_plus_snippet'], list)

class CleanSnippetWorks(unittest.TestCase):

    def setUp(self):

        self.test_list = ['AAAAA', 'a,-.\\a.++/,:a,</b><b>*()||']
        self.bad_chars = ',.|()*:+-/'

    def test_words_are_made_lowercase(self):

        self.assertTrue(PythonJobs.clean_snippet(self.test_list)[0].islower())

    def test_words_do_not_contain_bad_chars(self):

        for character in self.bad_chars:

            self.assertNotIn(character,PythonJobs.clean_snippet(self.test_list)[1])

    def test_whether_bold_stripped(self):

        self.assertNotIn('<b>',PythonJobs.clean_snippet(self.test_list)[1])

    def test_whether_bold_end_stripped(self):

        self.assertNotIn('</b>',PythonJobs.clean_snippet(self.test_list)[1])

    def test_whether_backslash_stripped(self):

        self.assertNotIn('\\',PythonJobs.clean_snippet(self.test_list)[1])

class ReturnOnlyPythonJobs(unittest.TestCase):

    def setUp(self):

        self.client = PythonJobs.setup_client(PythonJobs.PUBLISHER_ID)
        self.num_results, self.list_of_results = PythonJobs.search_indeed(self.client, PythonJobs.PARAMS)
        self.jobs_list = PythonJobs.process_all_jobs(self.list_of_results)
        self.jobs_list = PythonJobs.only_python_jobs(self.jobs_list)

    def test_every_job_should_contain_word_python(self):

        for job in self.jobs_list:

            self.assertIn('python', self.jobs_list[job]['title'].lower()) 
        
if __name__ == '__main__':
    unittest.main()











