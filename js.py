import csv
import json



with open('result.py', 'r') as file:
    data = file.read().replace('\n', '')
    
    info = json.loads(data)
    fieldnames = info.keys()
    

    print(info.keys())

    with open("samplecsv.csv", 'w') as f: 
            reader = csv.reader(f)
            wr = csv.DictWriter(f, fieldnames = info.keys()) 
            wr.writeheader() 
            wr.writerows(info.keys)
