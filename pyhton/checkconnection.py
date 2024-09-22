import requests

TOKEN = 'YOUR-BOT-API' #ENTER YOUR BOT API
url = f'https://api.telegram.org/bot{TOKEN}/getMe'

response = requests.get(url)
print(response.json())
