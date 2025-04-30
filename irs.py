
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

IR_PIN = 17

GPIO.setup(IR_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(IR_PIN) == 0:
            print("Object detected!")
        else:
            print("No object.")
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()

























sudo apt update
sudo apt install python3-rpi.gpio



| IR Sensor Pin | Connects to Raspberry Pi | Notes |
|---------------|--------------------------|-------|
| VCC           | 3.3V or 5V (Pin 1 or 2)  | Use 5V for most modules |
| GND           | GND (Pin 6 or 9)         | Common ground |
| OUT           | GPIO 17 (Pin 11, BCM mode) | Digital signal output |
