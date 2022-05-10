import json
import csv
import requests

flight = json.loads(open('flight.json').read())
response = requests.get(f'http://{flight["address"]}:{flight["port"]}').json()
res = []
for obj in response:
    if obj['visible_size'] < int(flight['size']):
        continue
    real_size = obj['visible_size'] * int(flight['height']) * int(flight['scale'])
    res.append((obj['name'], obj['visible_size'], real_size))
with open('sizes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(
        csvfile, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(('name', 'visible_size', 'real_size'))
    for obj in sorted(res, key=lambda x: (-x[2], x[0])):
        writer.writerow(obj)
