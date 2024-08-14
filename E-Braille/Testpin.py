import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
STR = 21 #pin used for STR signal Braille Display
GPIO.setup(STR,GPIO.OUT)

while True:
    GPIO.output(STR, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(STR, GPIO.LOW)
    time.sleep(1)
