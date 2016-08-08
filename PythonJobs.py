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
    'limit' : 25,
    'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"}

def main():

    client = setup_client(PUBLISHER_ID)
    num_results, list_of_results = search_indeed(client, PARAMS)
    jobs_list = process_all_jobs(list_of_results)
    print(jobs_list)
    term_frequencies = analyze_results(jobs_list)
    present_results(term_frequencies)

def setup_client(publisher_id):

    client = IndeedClient(publisher_id)

    return client

def search_indeed(client, params):

    list_of_results = []
    search_response = client.search(**params)

    num_results = search_response['totalResults']

    for i in range(1,num_results+1,25):

        params['start']=i

        search_response = client.search(**params)
        results = search_response['results']

        if i <= num_results-25:
            list_of_results += results
        else:
            list_of_results += results[:num_results-i+1]

    return num_results, list_of_results

def process_all_jobs(list_of_results):

    jobs_list = {}

    for job in list_of_results:

        jobs_list[job['jobkey']]={}
        jobs_list[job['jobkey']]['title'] = job['jobtitle']
        jobs_list[job['jobkey']]['title_plus_snippet'] = job['jobtitle'] + ' ' + job['snippet']
        jobs_list[job['jobkey']]['title_plus_snippet'] = jobs_list[job['jobkey']]['title_plus_snippet'].split()
        jobs_list[job['jobkey']]['title_plus_snippet'] = clean_snippet(jobs_list[job['jobkey']]['title_plus_snippet'])

    return jobs_list

def clean_snippet(title_snip_list):

    cleaned_list = [word.lower().strip() for word in title_snip_list]
    cleaned_list = [word.replace(',','') for word in cleaned_list]
    cleaned_list = [word.replace('.','') for word in cleaned_list]
    cleaned_list = [word.replace('|','') for word in cleaned_list]
    cleaned_list = [word.replace('(','') for word in cleaned_list]
    cleaned_list = [word.replace(')','') for word in cleaned_list]
    cleaned_list = [word.replace('*','') for word in cleaned_list]
    cleaned_list = [word.replace('<b>','') for word in cleaned_list]
    cleaned_list = [word.replace('</b>','') for word in cleaned_list]
    cleaned_list = [word.replace(':','') for word in cleaned_list]
    cleaned_list = [word.replace('+','') for word in cleaned_list]
    cleaned_list = [word.replace('-','') for word in cleaned_list]
    cleaned_list = [word.replace('\\','') for word in cleaned_list]
    cleaned_list = [word.replace('/','') for word in cleaned_list]

    return cleaned_list

def analyze_results(jobs_list):

    find_frequencies

    return term_frequencies

if __name__ == '__main__':
    main()
