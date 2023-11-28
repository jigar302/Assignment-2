# This server runs on Pi, sends Pi's your 4 arguments from the vcgencmds, sent as Json object.

# details of the Pi's vcgencmds - https://www.tomshardware.com/how-to/raspberry-pi-benchmark-vcgencmd
# more vcgens on Pi 4, https://forums.raspberrypi.com/viewtopic.php?t=245733
# more of these at https://www.nicm.dev/vcgencmd/
# JIGAR HUNDAL
# 100891267

import socket
import os, time
import json

s = socket.socket()
host = '10.102.13.67' # Localhost
port = 5000
s.bind((host, port))
s.listen(5)





def get_core_temperature():
    #Core Temperature from Pi using vcgencmd
    t = os.popen('vcgencmd measure_temp').readline()  # gets core temperature
    # Extracting temperature value from the string
    temperature = t.split('=')[1].split("'")[0]
    return temperature

def get_voltage():
    # Gets the Voltage using vcgencmd
    voltage = os.popen('vcgencmd measure_volts').readline().strip()
    return voltage

def get_clock_frequency():
    # Clock Frequency using vcgencmd
    frequency = os.popen('vcgencmd measure_clock arm').readline().strip()
    return frequency

def get_memory_usage():
    # Memory Usage using vcgencmd
    mem_usage = os.popen('vcgencmd get_mem arm').readline().strip()
    return mem_usage
while True:
        c, addr = s.accept()
        print('Got connection from', addr)

       
        core_temp = get_core_temperature()
        voltage = get_voltage()
        clock_freq = get_clock_frequency()
        mem_usage = get_memory_usage()

        # Creating JSON objects for each data point
        data = {
          "Core Temperature": core_temp,
            "Voltage": voltage,
            "Clock Frequency": clock_freq,
            "Memory Usage": mem_usage         
        
        }

        # Send data to client
        res = bytes(str(data), 'utf-8')  # Convert dictionary to bytes
        c.send(res)  # Send data as bytes
        c.close()
        
