from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Universe! This is a my simple app built using Flask. A class project.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6565, debug=True)
