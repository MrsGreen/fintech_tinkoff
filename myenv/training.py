import requests
response = requests.get('https://api.github.com/users/MrsGreen')
print(response.text)
print(response.status_code)