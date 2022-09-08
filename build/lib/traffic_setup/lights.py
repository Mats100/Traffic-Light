import time
import Rpi.GPIO as GPIO


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)  # Red
    GPIO.setup(22, GPIO.OUT)  # Yellow
    GPIO.setup(23, GPIO.OUT)  # Green


def control_traffic_lights(params):
    GPIO.output(21, 1)
    time.sleep(params['delay_green'])
    GPIO.output(21, 0)

    GPIO.output(22, 1)
    time.sleep(params['delay_yellow'])
    GPIO.output(22, 0)

    GPIO.output(23, 1)
    time.sleep(params['delay_red'])
    GPIO.output(23, 0)

    GPIO.output(22, 1)
    time.sleep(params['delay_yellow'])
    GPIO.output(22, 0)
