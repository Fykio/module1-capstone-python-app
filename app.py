from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Universe! This is a my simple app built using Flask.'

if __name__ == '__main__':
    app.run()
