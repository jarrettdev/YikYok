import requests
import io
import json
from bs4 import BeautifulSoup

'''
#TikTok url that is called each time the 'trending' page is loaded.
base_url = 'https://m.tiktok.com/api/item_list/?count=30&id=1&type=5&secUid=&maxCursor=0&minCursor=0&sourceType=12&appId=1233&region=US&language=en&verifyFp=&_signature=I-1eoAAgEB5-jtWqQ.se8CPtH7AAH1f'
#base_url = 'https://m.tiktok.com/api/item_list/?count=30&id=1&type=5&secUid=&maxCursor=0&minCursor=0&sourceType=12&appId=1233&region=US&language=en&verifyFp=verify_ka8jj7re_XQMKnGp3_6onR_4jqh_B2q8_XsdC3m65Mvbe&_signature=E8ySMAAgEBFOrxk63OQv.xPMkyAAE13'

#store the response from the get request
response = requests.get(base_url, headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"})

content = BeautifulSoup(response.text,'lxml')
with io.open('tik-response.html','w',encoding= 'utf-8') as html_file:
	html_file.write(content.text)
'''
#read from file
content = ''
with io.open('tik-response.html', 'r', encoding= 'utf-8') as html_file:
	for line in html_file.read():
		content += line

json_data = json.loads(content)
print(type(json_data))

test_chunk = json_data['items'][1]

print(type(test_chunk))
print(test_chunk['video']['playAddr'])

