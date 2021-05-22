from flask import Flask, render_template, request
app = Flask(__name__,template_folder='.')
name = "azzedine"
machines = {
	    "television": {'name': 'television', 'state': 'GPIO.LOW', 'status': "OFF"},
    	"machine a laver": {'name': 'machine à laver', 'state': 'GPIO.LOW', 'status': "OFF"},
    	"lampe1": {'name': 'lampe ', 'state': 'GPIO.LOW',  'status': "OFF"},
	}
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
		print("status ",machines[machine]['status'],machine)
	else:
		machines[machine]['status'] = 'OFF'
		machines[machine]['state'] = 'ON'
		print("status ",machines[machine]['status'],machine)
	template = {'machines':machines}
	return render_template("index.html", **template,hello="after clicking");

if __name__ == "__main__":
    app.run()