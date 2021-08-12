'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests 

url = 'http://demo.codingnomads.co:8080/tasks_api/users'

user_info = {
    'first_name': 'Michael',
    'last_name': 'Rippey',
    'email': 'example@example.com'
}

request_response = requests.post(url, json=user_info)

print(request_response.status_code)

view_new_user = requests.get(url)

print(view_new_user.content)
