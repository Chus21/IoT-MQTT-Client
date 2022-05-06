import csv
import json
import paho.mqtt.client

def on_connect(client, userdata, flags, rc):
    print('connected (%s)' % client._client_id)
    client.subscribe(topic='weather/hsrw-kali', qos=2)

def on_message(client,userdata, message):
    print ('--------------------------------')
    print ('topic: %s' % message.topic)
    print ('payload: %s' % message.payload)
    print ('qos: %d' % message.qos)

def main () :
    client = paho.mqtt.client.Client(client_id='Jesus', clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('eolab.de', port=1883)
    client.loop_forever()

if __name__ == '__main__':
    main()


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
              
              
    