from microbit import *
import radio

radio.on()  # Turn on the radio
radio.config(channel=1)  # Set to the same channel as the transmitter

while True:
    incoming = radio.receive()
    if incoming:
        if incoming == 'stop':
            break  # Stop the loop if 'stop' signal is received
        else:
            volume_data = int(incoming)  # Convert the received string back to an integer
            # Here you can add code to do something with the volume_data