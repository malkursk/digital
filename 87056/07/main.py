from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route("/")
def main():
    return f"Работа №7. Flask Якунин Алексей Владимирович, гр 44-22-169"

@app.route("/2")
def lab2():
    return render_template('lab2/index.html')

@app.route("/3")
def lab3():
    return render_template('lab3/index2.html')
    