'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''

import requests 

url = 'http://demo.codingnomads.co:8080/tasks_api/users'


request_response = requests.put(url + '/407')

print(request_response.status_code)

