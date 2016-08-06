import requests

r = requests.post('https://secure.dice.com/oauth/token',
                  data = {'Application type':'x-www-form-urlencoded',
                          'grant_type':'client_credentials'})
