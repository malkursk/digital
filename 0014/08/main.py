from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Практическая работа №7. FLASK. Безалтынных Александр Олегович</h1> гр. 44-23-170."

@app.route("/02")
def route02():
    return render_template("02/index.html")

@app.route("/03")
def route03():
    return render_template("03/index.html")

def converter(v,b1=8,b2=10):
    number = int(v,b1)
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number == 0:
        return '0'
    result = []
    while number>0:
        number, mod = divmod(number, b2)
        result.append(digits[mod])
    result = ''.join(reversed(result))
    return result

@app.route("/calc/<a>")
def calc(a):
    return converter(a)