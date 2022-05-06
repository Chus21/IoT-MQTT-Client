import mqtt from "mqtt";
var client = mqtt.connect('mqtt://eolab.de:1883');
import fs from 'fs';
    client.on('connect', function() {
        client.subscribe("weather/hsrw-kali");
        console.log("Client has subscribed successfully");
    });

   client.on('message', function(topic,message){
        console.log( message.toString());

        fs.writeFile('result.py',message.toString(), function (err) {
            if (err) throw err;
            console.log('Saved!');
        }); 
    });