from flask import Flask
app = Flask(__name__)
app.debug=True

@app.route("/") 
@app.route("/hello1") 
@app.route("/hello2") 
def hello():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
