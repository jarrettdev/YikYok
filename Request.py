import requests

base_url = 'https://www.tiktok.com/trending?lang=en'

req = requests.get(base_url, headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"})

print('request', req.text)