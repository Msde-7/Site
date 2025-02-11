from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/who')
def who():
    return render_template('who.html')

@app.route('/goals')
def goals():
    return render_template('goals.html')

@app.route('/difference')
def difference():
    return render_template('difference.html')

@app.route('/platform')
def platform():
    return render_template('platform.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0') 