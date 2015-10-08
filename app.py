from flask import Flask, render_template,request,jsonify
import urllib, json

app = Flask(__name__)
app.config["DEBUG"] = True

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry bruh, this page ain't here", 404

@app.route("/")
def hello():
	url = "https://sheetsu.com/apis/4b26cc3d"
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	data = data['result']

	return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
