'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body
'''


import requests 

url = 'http://demo.codingnomads.co:8080/tasks_api/users'

request_response = requests.get(url)

print(request_response.status_code)
print(request_response.content)
print(request_response.text)
