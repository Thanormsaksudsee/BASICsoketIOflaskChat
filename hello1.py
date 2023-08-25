from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/student")  
def show():
    return "<p>Test!</p>"

if __name__=="__main__" :
    app.run(debug=True)