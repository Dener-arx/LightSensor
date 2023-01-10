import RPi.GPIO as GPIO
import time

__author__ = 'Adapted from Adafruit'
__license__ = "GPL"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) 

#define the pin that goes to the circuit
pin_to_circuit = 29

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    while True:
        light_level = rc_time(pin_to_circuit)
        if light_level < 20:
            ledpin = 18
            GPIO.output(ledpin,GPIO.LOW)
            ledpin = 16
            GPIO.output(ledpin,GPIO.HIGH)
            print("luz")
        else:
            ledpin = 16
            GPIO.output(ledpin,GPIO.LOW)
            ledpin = 18
            GPIO.output(ledpin,GPIO.HIGH)
            print("não luz")

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
