import csv
import json
from collections import Counter

nodes_set = set()
links_list = []

with open('data/tags.json', 'r') as infile:
	data = json.load(infile)
	for tag in data:
		nodes_set.add(
			(tag['from']['id'], tag['from']['name']))
		nodes_set.add(
			(tag['to']['id'], tag['to']['name']))

		links_list.append(tuple(
			[tag['from']['id'],
			tag['to']['id']]))

with open('data/nodes.csv', 'w') as outfile:
	writer = csv.writer(outfile)
	writer.writerow(['id','name'])
	writer.writerows(nodes_set)

links_counter = Counter(links_list)

links_data = []
for key, val in links_counter.items():
	data = {}
	data['source'] = key[0]
	data['target'] = key[1]
	data['weight'] = val
	links_data.append(data)

with open('data/edges.csv', 'w') as outfile:
	writer = csv.DictWriter(outfile, fieldnames=['source','target','weight'])
	writer.writeheader()
	writer.writerows(links_data)

"""nodes_data = []
for key, val in nodes_counter.items():
	nodes_data.append({'id': key, 'degree': val})

with open('data.json', 'w') as outfile:
	json.dump({
		"nodes": nodes_data,
		"links": links_data
	}, outfile)"""