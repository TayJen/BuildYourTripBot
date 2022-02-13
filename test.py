import json


with open('labels.json', 'r') as fp:
    labels = json.load(fp)
    pred = labels['12']
    print(pred)
