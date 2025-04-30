exp 7 interfacing all


import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
import busio
from adafruit_character_lcd.character_lcd_i2c import Character_LCD_I2C

# —————— I²C LCD Setup ——————
i2c = busio.I2C(board.SCL, board.SDA)
lcd = Character_LCD_I2C(i2c, 16, 2)

# —————— Sensor & GPIO Pins ——————
TRIG    = 5     # Ultrasonic trigger
ECHO    = 6     # Ultrasonic echo
IR_PIN  = 16    # IR digital output
DHT_PIN = board.D4  # DHT11 data

# —————— Initialization ——————
def init_gpio():
    dht_device = adafruit_dht.DHT11(DHT_PIN)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(IR_PIN, GPIO.IN)
    GPIO.output(TRIG, GPIO.LOW)
    return dht_device

# —————— Read DHT11 with error handling ——————
def read_dht11(dht_device):
    try:
        return dht_device.temperature, dht_device.humidity
    except RuntimeError:
        return None, None

# —————— Measure distance (HC-SR04) ——————
def measure_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        end = time.time()

    return round((end - start) * 34300 / 2, 2)

# —————— Main loop & LCD display ——————
def main():
    dht = init_gpio()
    try:
        while True:
            # 1) Temp & Humidity
            temp, hum = read_dht11(dht)
            lcd.clear()
            if temp is not None and hum is not None:
                lcd.message = f"Temp:{temp:.1f}C\nHum:{hum:.1f}%"
            else:
                lcd.message = "DHT ERR"
            time.sleep(1)

            # 2) Distance
            dist = measure_distance()
            lcd.clear()
            lcd.message = f"Dist:{dist:.1f}cm"
            time.sleep(1)

            # 3) IR sensor status
            if GPIO.input(IR_PIN) == 0:
                lcd.clear()
                lcd.message = "Object Detected"
            else:
                lcd.clear()
                lcd.message = "No Object     "
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()





























sudo raspi-config
# → Interface Options → I2C → Enable
sudo apt install -y i2c-tools python3-smbus
# Verify the LCD appears (e.g. at 0x27):
sudo i2cdetect -y 1



pip3 install adafruit-circuitpython-charlcd




| Sensor Pin | RPi Pin | Notes |
|------------|---------|-------|
| VCC        | 3.3V (Pin 1) or 5V (Pin 2) | Either works |
| GND        | GND (Pin 6) | Ground |
| DATA       | GPIO 4 (Pin 7) | Signal line |


| Sensor Pin | RPi Pin | Notes |
|------------|---------|-------|
| VCC        | 3.3V (Pin 1) | Power |
| GND        | GND (Pin 6) | Ground |
| OUT        | GPIO 16 (Pin 36) | Digital signal input |

| Sensor Pin | RPi Pin | Notes |
|------------|---------|-------|
| VCC        | 5V (Pin 2) | Power |
| GND        | GND (Pin 6) | Ground |
| TRIG       | GPIO 5 (Pin 29) | Output from Pi |
| ECHO       | GPIO 6 (Pin 31) | **Use voltage divider (1kΩ + 2kΩ)** to drop from 5V to 3.3V |


| LCD Pin         | Raspberry Pi Pin    | Notes                              |
|-----------------|---------------------|------------------------------------|
| VCC             | 5 V  (Pin 2 or 4)    | Power                              |
| GND             | GND  (Pin 6, 9, 14…) | Ground                             |
| SDA (Data)      | GPIO 2 (SDA1, Pin 3)| I²C Data line                      |
| SCL (Clock)     | GPIO 3 (SCL1, Pin 5)| I²C Clock line                     |
