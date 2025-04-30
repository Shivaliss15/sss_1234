
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(2)






















sudo apt update
sudo apt install python3-pip libgpiod2
pip3 install --upgrade adafruit-blinka
pip3 install adafruit-circuitpython-dht
