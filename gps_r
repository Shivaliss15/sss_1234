

import serial
import time

# Set up serial connection to GPS module
gps = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)

def parse_gpgga(data):

    parts = data.split(',')
    if len(parts) > 6:
        latitude = parts[2]
        lat_direction = parts[3]
        longitude = parts[4]
        long_direction = parts[5]

        # Convert latitude and longitude to a more readable format
        latitude = float(latitude[:2]) + float(latitude[2:]) / 60
        if lat_direction == 'S':
            latitude = -latitude

        longitude = float(longitude[:3]) + float(longitude[3:]) / 60
        if long_direction == 'W':
            longitude = -longitude

        return latitude, longitude
    return None, None

while True:
    data = gps.readline().decode('utf-8').strip()
    if data.startswith('$GPGGA'):
        latitude, longitude = parse_gpgga(data)
        if latitude is not None and longitude is not None:
            print(f"Latitude: {latitude}, Longitude: {longitude}")
    time.sleep(1)


















enable uart:
sudo raspi-config
interface => serial port
no -> yes
finist reboot


sudo apt update && sudo apt upgrade
sudo apt install -y python3-pip
pip install pyserial pynmea2
sudo apt install gpsd gpsd-clients python-gps
sudo reboot




VCC → 5V (Pin 2 on Raspberry Pi)

GND → GND (Pin 6 on Raspberry Pi)

TX (GPS) → RX (GPIO 15, Pin 10 on Raspberry Pi)

RX (GPS) → TX (GPIO 14,
