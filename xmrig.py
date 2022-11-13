import flask
from flask import Flask

app = Flask(__name__)

html = open("xmrig.html", "r")

@app.route("/")
def xmrig():
	global html
	return f"{html.read()}"

app.run(host="0.0.0.0", port=3333)