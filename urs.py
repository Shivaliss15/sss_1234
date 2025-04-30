

import RPi.GPIO as GPIO
import time

# Define GPIO pins
TRIG = 16
ECHO = 18

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Send a 10µs pulse to TRIG
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Wait for ECHO to go HIGH
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    # Wait for ECHO to go LOW
    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    # Calculate duration and distance
    duration = end_time - start_time
    distance = (duration * 34300) / 2  # in cm
    return round(distance, 2)

try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist} cm")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()


















sudo apt update
sudo apt install python3-rpi.gpio



| Sensor Pin | Connects To Raspberry Pi | Notes |
|------------|--------------------------|-------|
| VCC        | 5V (Pin 2 or 4)          | Sensor needs 5V to work |
| GND        | GND (Pin 6, 9, etc.)     | Common ground |
| TRIG       | GPIO 16 (BCM mode → Pin 36) | Output signal to trigger ultrasonic pulse |
| ECHO       | GPIO 18 (BCM mode → Pin 12) | **Must pass through voltage divider** |
