'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests 


url = 'http://demo.codingnomads.co:8080/tasks_api/users'

request_response = requests.get(url)

json_response = request_response.json()

for data in json_response['data']:
    print(data['email'])
