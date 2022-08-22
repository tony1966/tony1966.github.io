from flask import Flask
app = Flask(__name__)
app.debug=True

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/hello/<name>") 
def hello_name(name): 
    return "<h1>Hello, %s</h1>" % name 

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
