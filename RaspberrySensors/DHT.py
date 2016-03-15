#!/usr/bin/python
#RaspberrySensors v 0.1.5
#Temperature and Humidity Sensor DHT11 + LCD
#by Miorio 2016
#------------------------------My Build-------------------------------------
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
from time import sleep
from datetime import datetime
import settings
version = str(0.1.5)

print("Добро пожаловать в RaspberrySensors v." + version+ "\n")
print("\n")
print("-----ГЛАВНОЕ МЕНЮ-----\n")
print("1 - Начать измерения.\n")
print("2 - Настройки.\n")
print("3 - Выход.\n")
print("\n")
print("---------------------\n")

paramA = [1, 1, 1]

def menu(paramA):
    paramC = paramA
    userChoise = str(input("choise: "))
    if userChoise == "1":
        mainMeasure()
    elif userChoise == "2":
        param = settings.settingsMenu
        paramC = param
        paramC = paramA
    elif userChoise == "3":
            sys.exit
    else:
        print("error" + str(userChoise))
        sys.exit()
    return paramC

GPIO.setmode(GPIO.BCM)
sensor = Adafruit_DHT.DHT11
pin = 4

def main(paramC):
    if paramC == [1, 1, 1] :
        while True:
            mainMeasure()
    elif paramC == [1, 1, 0] :
        while True:
            writeLog(temp_measure(), hum_measure())
    elif paramC == [1, 0, 1] :
        while True:
            lcd_view()
    elif paramC == [0, 1, 1] :
        while True:
            lcd_view()
            writeLog(cleansreen_measureT(), cleansreen_measureH())
    elif paramC == [0, 0, 1] :
        while True:
            temp_measure()
    elif paramC == [0, 0, 0] :
        while True:
            print("ERROR! CHECK SETTINGS")
            main()
    else:
        print("Хотя бы один параметр должен быть включен: \n")
        paramC = settings(paramA)
    return paramC

    userChoise = str(input("choise: "))

def mainMeasure():
    try:
        while True:
            lcd_view()
            writeLog(temp_measure(), hum_measure())
    except KeyboardInterrupt:
       lcd = HD44780()
       lcd.message(" Good bye!")
       print("\n" + "Good bye!")
       time.sleep(3)
       lcd.clear()
       lcd.LCD_DISPLAYOFF
    return

class HD44780():
     
    # commands
    LCD_CLEARDISPLAY  = 0x01
    LCD_RETURNHOME    = 0x02
    LCD_ENTRYMODESET  = 0x04
    LCD_DISPLAYCONTROL= 0x08
    LCD_CURSORSHIFT   = 0x10
    LCD_FUNCTIONSET   = 0x20
    LCD_SETCGRAMADDR  = 0x40
    LCD_SETDDRAMADDR  = 0x80

    # flags for display entry mode
    LCD_ENTRYRIGHT = 0x00
    LCD_ENTRYLEFT = 0x02
    LCD_ENTRYSHIFTINCREMENT = 0x01
    LCD_ENTRYSHIFTDECREMENT = 0x00

    # flags for display on/off control
    LCD_DISPLAYON = 0x04
    LCD_DISPLAYOFF = 0x00
    LCD_CURSORON = 0x02
    LCD_CURSOROFF = 0x00
    LCD_BLINKON = 0x01
    LCD_BLINKOFF = 0x00

    # flags for display/cursor shift
    LCD_DISPLAYMOVE = 0x08
    LCD_CURSORMOVE = 0x00
    LCD_MOVERIGHT = 0x04
    LCD_MOVELEFT = 0x00

    # flags for function set
    LCD_8BITMODE = 0x10
    LCD_4BITMODE = 0x00
    LCD_2LINE = 0x08
    LCD_1LINE = 0x00
    LCD_5x10DOTS = 0x04
    LCD_5x8DOTS = 0x00

    def __init__(self, pin_rs=25, pin_e=24, pins_db=[23, 17, 27, 22]):

        self.pin_rs = pin_rs
        self.pin_e = pin_e
        self.pins_db = pins_db

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_e, GPIO.OUT)
        GPIO.setup(self.pin_rs, GPIO.OUT)
        for pin in self.pins_db:
            GPIO.setup(pin, GPIO.OUT)

        self.clear()

    def clear(self):
        """ Blank / Reset LCD """

        self.cmd(0x33) # $33 8-bit mode
        self.cmd(0x32) # $32 8-bit mode
        self.cmd(0x28) # $28 8-bit mode
        self.cmd(0x0C) # $0C 8-bit mode
        self.cmd(0x06) # $06 8-bit mode
        self.cmd(0x01) # $01 8-bit mode

    def cmd(self, bits, char_mode=False):
        """ Send command to LCD """

        sleep(0.001)
        bits=bin(bits)[2:].zfill(8)

        GPIO.output(self.pin_rs, char_mode)

        for pin in self.pins_db:
            GPIO.output(pin, False)

        for i in range(4):
            if bits[i] == "1":
                GPIO.output(self.pins_db[::-1][i], True)

        GPIO.output(self.pin_e, True)
        GPIO.output(self.pin_e, False)

        for pin in self.pins_db:
            GPIO.output(pin, False)

        for i in range(4,8):
            if bits[i] == "1":
                GPIO.output(self.pins_db[::-1][i-4], True)

        GPIO.output(self.pin_e, True)
        GPIO.output(self.pin_e, False)

    def message(self, text):
        """ Send string to LCD. Newline wraps to second line"""

        for char in text:
            if char == '\n':
                self.cmd(0xC0) # next line
            else:
                self.cmd(ord(char),True)

def cleansreen_measureT():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    time.sleep(9)
    return temperature
def cleansreen_measureM():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    time.sleep(9)
    return humidity

def temp_measure():
    print("Checking sensors...")
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%').format(temperature, humidity)
    else:
        print("Failed to get reading. Try again!")
    time.sleep(9)
    return temperature

def hum_measure():
    print("Checking sensors...")
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%').format(temperature, humidity)
    else:
        print("Failed to get reading. Try again!")
    time.sleep(9)
    return humidity

def firstLine():
    fileName = "measureDHT11.csv"
    WRITE = "w"
    measureData = open(fileName, WRITE)
    measureData.write("Temp." + ";" + "Humid." +";" + "Time" + "\n")
    measureData.close()
    return

def writeLog(temp, hum):
    fileName = "measureDHT11.csv"
    APPEND = "a"
    measureData = open(fileName, APPEND)
    date = datetime.strftime(datetime.now(), "%H:%M:%S")
    measureData.write(str(temp) + "C" + ";" + str(hum) + "%" + ";" + str(date) + "\n")
    measureData.close()
    return measureData

def lcd_view():
    while True:
        if __name__ == '__main__':
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            temp = " Temperature:" + str(temperature)+"C"
            hum = "Humidity:" + str(humidity)+ "%"
            lcd = HD44780()
            lcd.message(temp + '\n' + hum)
        return

menu(paramA)