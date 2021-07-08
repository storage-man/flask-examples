from flask import Flask, render_template, request,redirect
app = Flask(__name__,template_folder='.')
#***********************************************************************
labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]
#***********************************************************************
#render_template("index.html", **template,hello="after clicking")
name = "azzedine"
machines = {
	    "television": {'name': 'television', 'state': 'GPIO.LOW', 'status': "OFF"},
    	"machine a laver": {'name': 'machine à laver', 'state': 'GPIO.LOW', 'status': "OFF"},
    	"lampe1": {'name': 'lampe ', 'state': 'GPIO.LOW',  'status': "OFF"},
	}
@app.route("/")
def hello():
    line_labels=labels
    line_values=values
    template = {'machines':machines,"title":'Bitcoin Monthly Price in USD', "max":17000, "labels":line_labels, "values":line_values};
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
    #return ;
    return redirect("/", code=302);
@app.route("/chart")
def hello2():
    line_labels=labels
    line_values=values
    template = {'machines':machines}
    return render_template('index.html',**template)
if __name__ == "__main__":
    app.run()