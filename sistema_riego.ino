 const int AirValue = 550;   //you need to replace this value with Value_1
const int WaterValue = 250;  //you need to replace this value with Value_2
int soilMoistureValue = 0;
int soilmoisturepercent=0;
void setup6() {
  pinMode(9, OUTPUT); // pin where relay trigger connected
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
}
void loop6() {
soilMoistureValue = analogRead(A0);  //put Sensor insert into soil
Serial.println(soilMoistureValue);
soilmoisturepercent = map(soilMoistureValue, AirValue, WaterValue, 0, 100);

if (soilmoisturepercent < 40) // change this at what level the pump turns on
  {
    Serial.println("seco, Pump turning on");
    digitalWrite(9, HIGH); // Low percent high signal to relay to turn on pump
  }
  else if (soilmoisturepercent > 50) // max water level should be
  {
    Serial.println("mojado, Pump turning off");
    digitalWrite(9, LOW); // high percent water high signal to relay to turn on pump
  }



if(soilmoisturepercent >= 100) // 100% --> sensor sunken in water
{
  Serial.println("100 %");
}
else if(soilmoisturepercent <=0) //0% sensor 
{
  Serial.println("0 %"); // dry or sensor in the air 
}
else if(soilmoisturepercent >0 && soilmoisturepercent < 100)
{
  Serial.print(soilmoisturepercent);
  Serial.println("%");
  
}
  delay(250);
}
