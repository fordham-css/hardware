from flask import Flask, render_template,request,jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry bruh, this page ain't here", 404

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
