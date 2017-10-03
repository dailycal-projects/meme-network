import json
import requests
from time import sleep

endpoint = 'https://graph.facebook.com/v2.10/'
access_token = ''

fields = ['comments.limit(3000){message_tags,admin_creator,from}']

payload = {
	'access_token': access_token,
	'fields': ','.join(fields),
	'limit': 10
}

rows = []

def parse_response(response):
	for post in response['data']:
		comments = post.get('comments', None)

		if not comments:
			continue

		for comments_data in comments.get('data', None):
			data = {}
			data['from'] = comments_data['from']
			tagged_list = comments_data.get('message_tags', None)

			if not tagged_list:
				continue

			for tagged in tagged_list:
				name = tagged.get('name', None)
				if not name:
					continue
				data['to'] = {
					'id': tagged['id'],
					'name': tagged['name']
				}
				rows.append(data) 

def query(url, payload=None):
	r = requests.get(url, params=payload)
	print(r.url)
	response = r.json()
	parse_response(response)

	write_data()
	next_url = response['paging'].get('next', None)

	if next_url:
		sleep(1)
		query(next_url)
		
def write_data():
	with open('data/tags.json', 'w') as outfile:
		json.dump(rows, outfile)

url = endpoint + '1717731545171536/feed'
query(url, payload)
