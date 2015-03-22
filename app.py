from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__,instance_relative_config=True)
app.config["DEBUG"] = True
#app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry bruh, this page ain't here", 404

@app.route("/")
def index():
	cur = get_db().cursor()
	return render_template("index.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=8080)
