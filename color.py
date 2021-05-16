from flask import Flask
app = Flask(__name__)

@app.route('/')
def color():
    return '{"color": "red"}'

