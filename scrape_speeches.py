import csv, requests

endpoint = "https://api.millercenter.org/speeches"
out_file = "data/speeches.csv"

r = requests.post(url=endpoint)
data = r.json()
items = data['Items']

while 'LastEvaluatedKey' in data:
    parameters = {"LastEvaluatedKey": data['LastEvaluatedKey']['doc_name']}
    r = requests.post(url=endpoint, params=parameters)
    data = r.json()
    items += data['Items']
    print(f'{len(items)} speeches')

# Assuming each item in 'items' is a dictionary
with open(out_file, "w", newline='') as out:
    writer = csv.DictWriter(out, fieldnames=items[0].keys())
    writer.writeheader()
    writer.writerows(items)
    print(f'wrote results to file: {out_file}')

# import json, requests, sys

# endpoint = "https://api.millercenter.org/speeches"
# out_file = "speeches.json"

# r = requests.post(url=endpoint)
# data = r.json()
# items = data['Items']

# while 'LastEvaluatedKey' in data:
#     parameters = {"LastEvaluatedKey": data['LastEvaluatedKey']['doc_name']}
#     r = requests.post(url = endpoint, params = parameters)
#     data = r.json()
#     items += data['Items']
#     print(f'{len(items)} speeches')

# with open(out_file, "w") as out:
#     out.write(json.dumps(items))
#     print(f'wrote results to file: {out_file}')