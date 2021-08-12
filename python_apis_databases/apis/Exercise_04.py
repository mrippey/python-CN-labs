'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

import requests 

url = 'http://demo.codingnomads.co:8080/tasks_api/users'

user_info = {
    'id': 407,
    'first_name': 'Test',
    'last_name': 'Info',
    'email': 'example@example.com'
}

request_response = requests.put(url, json=user_info)

print(request_response.status_code)

view_new_user = requests.get(url)

print(view_new_user.content)
