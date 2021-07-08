from flask import Flask, render_template, request
import RPi.GPIO as GPIO
app = Flask(__name__,template_folder='.')
GPIO.setwarnings(False)
name = "azzedine"
#to use raspberry pi board pin numbers
GPIO.setmode(GPIO.BCM)
#set up GPIO output channel
pins = [23,24,25]
machines = {
	    "television": {'name': 'television', 'pin':pins[0],'state': GPIO.LOW, 'status': "OFF"},
    	"machine a laver": {'name': 'machine à laver','pin':pins[1], 'state': GPIO.LOW, 'status': "OFF"},
    	"lampe1": {'name': 'lampe ','pin':pins[2], 'state': GPIO.LOW,  'status': "OFF"},
	}

for pin in pins:
	#print(pin)
	GPIO.setup(int(pin),GPIO.OUT)
	GPIO.output(pin,GPIO.LOW)

def set(pin,state):
	GPIO.output(pin,state)
#def reset(pin):
#GPIO.output(pin,GPIO.LOW)
@app.route("/")
def hello():
	template = {'machines':machines}
	return render_template("index.html", **template);
@app.route("/<machine>/<status>")
def hola(machine,status):
	print("hi ",machine)
	if status == "on":
		machines[machine]['status'] = 'ON'
		machines[machine]['state'] = 'OFF'
		set(machines[machine]['pin'],GPIO.HIGH)
		print("status ",machines[machine]['status'],machine)
	else:
		machines[machine]['status'] = 'OFF'
		machines[machine]['state'] = 'ON'
		set(machines[machine]['pin'],GPIO.LOW)
		print("status ",machines[machine]['status'],machine)
	template = {'machines':machines}
	return render_template("index.html", **template,hello="after clicking");

if __name__ == "__main__":
    app.run()