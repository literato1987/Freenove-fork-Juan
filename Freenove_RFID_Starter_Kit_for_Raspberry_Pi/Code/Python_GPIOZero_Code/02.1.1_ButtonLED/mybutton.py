from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
    for i in range(-10,10):
        led.value = abs(i)/10
        sleep(0.1)  # off
    
