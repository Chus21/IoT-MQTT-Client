import csv
import json
import paho.mqtt.client

output_csv="output.csv"

#writes the CSV headers. I use 'w' to truncate the file and add headers on the first line
def write_csv_headers():
    headers = ("wind_speed","wind_direction","air_temperature","air_relhumidity","smp10","pqsl","soil_moisture","soil_tempblue","soil_tempred","air_pressure","precipitation","created_at")
    with open(output_csv, "w") as myfile:
        myfile.write(";".join(headers)+"\n")
    
#Generates a CSV line from a MQTT payload and append that line into the CSV file
def append_to_csv(payload):
    #parse payload as a JSON object
    jsonObj = json.loads(str(payload).replace("b'","").replace("'",""))
    #get all values fron the JSON object and store it in a list
    values = map(lambda key: str(jsonObj[key]), jsonObj.keys())
    #creates the line by joining all values separating them with a ;
    line = ";".join(values)

    #writes the json file (for debuging purposes)
    with open("output.json", "a") as myfile:
        myfile.write(str(payload)+"\n")

    #appends the line with vaules to the CSV file
    with open(output_csv, "a") as myfile:
        myfile.write(line+"\n")
    
def on_connect(client, userdata, flags, rc):
    print('connected (%s)' % client._client_id)
    client.subscribe(topic='weather/hsrw-kali', qos=2)

#this is run on every message received. basically it prints on the console
#the message and appends the payload to the CSV file
def on_message(client,userdata, message):
    print ('--------------------------------')
    print ('topic: %s' % message.topic)
    print ('payload: %s' % message.payload)
    print ('qos: %d' % message.qos)
    append_to_csv(message.payload)

def main () :
    write_csv_headers() #creates CSV file and write its CSV headers
    #infinite loop to get MQTT messages from the server
    client = paho.mqtt.client.Client(client_id='Jesus', clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('eolab.de', port=1883)
    client.loop_forever()

if __name__ == '__main__':
    main()
