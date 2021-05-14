from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "world"
    return 'Hello, the new world!'

if __name__=="__main__":
    app.run()


