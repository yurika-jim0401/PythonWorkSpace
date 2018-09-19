import json
data = {"name": "jim", "age": 23}

with open("t.json", 'w') as f:
    json.dump(data, f)
with open("t.json", 'r') as f:
    d = json.load(f)
    print(d)
