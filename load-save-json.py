import json

with open('test.json') as f:
    data = json.load(f)
    print(data)

with open('test.json', 'w') as f:
    data['key'] = 311
    print(data)
    json.dump(data, f)