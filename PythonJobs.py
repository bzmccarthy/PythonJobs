'''
This script will connect to the Indeed API, perform a job
search for Python jobs in the Philadelphia/19067 area, then
collate and clean those results to figure out the most relevant
skills needed and present them to the user
'''

import indeed

def main():

    all_jobs = search_indeed(publisher_id, params)
    jobs_list = extract_ids(all_jobs)
    jobs_list = add_snippets(jobs_list)
    jobs_list = snippets_to_list(jobs_list)
    jobs_list = clean_snippets(jobs_list)
    term_frequencies = find_term_freq(jobs_list)

    present_results(term_frequencies)

publisher_id = 8263932719076827

params = {
    'q' : "python",
    'l' : "austin",
    'userip' : "1.2.3.4",
    'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
}

if __name__ == '__main__':
    main()
