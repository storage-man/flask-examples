from flask import Flask, render_template
app = Flask(__name__,template_folder='.')
name = "azzedine"
@app.route("/")
def hello():
	return render_template("index.html", message=name);

if __name__ == "__main__":
    app.run()