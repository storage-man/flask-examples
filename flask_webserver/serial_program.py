import serial
import time as t
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.flush()
timeout = 2
#line = ""
def get_line():
	t.sleep(0.5)
	#global line
	line = None
	while(line == None):
		if ser.in_waiting > 0:
			#line = ser.readline().decode('utf-8').rstrip()
			line = ser.readline()
    	return str(line)
def get_temperature():
	ti = t.time()
	temp = 0
	while temp == 0 and t.time()-ti<timeout:
		v = get_line()
        	array = v.split('=')
		if array[0] == "temperature":
			temp = int(array[1])
	return temp


