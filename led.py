
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pins = [2, 3, 4, 17, 27, 22, 10]

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        # Turn ON odd-indexed LEDs (0, 2, 4, 6) and OFF even
        for i in range(len(led_pins)):
            if i % 2 == 0:
                GPIO.output(led_pins[i], GPIO.HIGH)
            else:
                GPIO.output(led_pins[i], GPIO.LOW)
        time.sleep(0.5)

        # Turn ON even-indexed LEDs (1, 3, 5) and OFF odd
        for i in range(len(led_pins)):
            if i % 2 == 0:
                GPIO.output(led_pins[i], GPIO.LOW)
            else:
                GPIO.output(led_pins[i], GPIO.HIGH)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Cleaning up...")
    GPIO.cleanup()






sudo apt update
sudo apt install python3-rpi.gpio
