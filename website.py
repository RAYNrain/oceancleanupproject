from flask import Flask, url_for, redirect
from flask import Flask, request, send_from_directory
from flask import render_template
from jinja2 import Template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')

if __name__ == '__main__':
    app.run()