import csv
import json
import json

with open('result.py', 'r') as file:
    data = file.read()
info = json.loads(data)

print(info[0].keys())

with open("samplecsv.csv", 'w') as f: 
    reader = csv.reader(f)
    wr = csv.DictWriter(f, fieldnames = info[0].keys()) 
    wr.writeheader() 
    wr.writerows(info)

    fechas=data.read().split('||')
    print(fechas)