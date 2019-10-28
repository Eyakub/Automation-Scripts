import requests

'''
Most commonly two types of requests are used:
- GET -> used to receives informations
- POST - > used to send information
'''

# status code
'''
1xx Informational   100-199
2xx Success         200-299
3xx Redirection     300-399
4xx Client error    400-499
5xx Server error    500-599
'''

# request.get(url)       -- response object
response = requests.get('http://google.com')
print(response.headers)

for key, value in response.headers.items():
    print(key, ' ', value)