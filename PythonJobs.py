'''
This script will connect to the Indeed API, perform a job
search for Python jobs in the Philadelphia/19067 area, then
collate and clean those results to figure out the most relevant
skills needed and present them to the user
'''

from indeed import IndeedClient

PUBLISHER_ID = 8263932719076827

PARAMS = {
    'q' : "python",
    'l' : "19067",
    'userip' : "1.2.3.4",
    'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"}

def main():

    client = setup_client(PUBLISHER_ID)

    all_jobs = search_indeed(client, PARAMS)
    jobs_list = process_all_jobs(all_jobs)
    term_frequencies = analyze_results(jobs_list)

    present_results(term_frequencies)

def setup_client(publisher_id):

    client = IndeedClient(publisher_id)

    return client

def search_indeed(publisher_id, params):

    all_jobs = []

    num_total_results = find_total_results(publisher_id, params)

    for i in range(num_total_results):
        all_jobs.append(get_jobs(start, params))

    return all_jobs

def process_all_jobs(all_jobs):

    jobs_list = {}

    for job in all_jobs:

        extract_id
        add_snippet
        snippet_to_list
        clean_snippet

def analyze_results(jobs_list):

    find_frequencies

    return term_frequencies

def find_total_results(client, params):

    

    pass

if __name__ == '__main__':
    main()
