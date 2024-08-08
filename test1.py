import json
import os

with open('xxx.json', 'r') as j:
    data = json.load(j)

for i in data:
    print(i)

print("这是主干分支的commit")