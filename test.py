import json


with open('data/labels.json', 'r') as fp:
    labels = json.load(fp)
    pred = labels['12']
    print(pred)

print('Git Test')
