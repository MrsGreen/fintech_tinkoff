import requests
response = requests.get('https://api.github.com/users/MrsGreen')

print(response.status_code)
print(response.text)