import csv
import json



with open('result.py', 'r') as file:
    data = file.read().replace('\n', '')
    
    info = json.loads(data)
    fieldnames = info.keys()
    values = info.values()
    nms = [fieldnames, values]

    f = open('samplecsv.csv', 'w')

    with f:

        writer = csv.writer(f)
        
        for row in nms:
            writer.writerow(row)
        print(info.keys())

    

    #with open("samplecsv.csv", 'w') as f: 
     #         reader = csv.reader(f)
      #        wr = csv.DictWriter(f, fieldnames)
       #       wr.writeheader()
        #      
         #     wr.writerow({'wind_direction':3.0})
              #wr.writerow({'wind_speed':1.0, 'wind_direction':3.0})
              
              
    