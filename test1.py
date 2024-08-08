import json
import os

with open('xxx.json', 'r') as j:
    data = json.load(j)

for i in data:
    print(i)

print("这是特性分支的commit")
