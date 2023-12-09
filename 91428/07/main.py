from flask import Flask, render_template

app = Flask(__name__)

def converter(v,b1=10,b2=16):
     number = int(v, b1)
     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     if number ==0:
        return '0'
     result = []
     while number > 0:
        number, mod= divmod(number, b2)
        result.append(digits[mod])
     result = ''.join(reversed(result))
     return result

@app.route("/")
def main():
    return "<p>Практическая работа №7 группа 44-23-171 <h1>Александра Рубцова!</h1></p>"

@app.route("/02")
def route02():
    return render_template("02/index.html")

@app.route("/03")
def route03():
    return render_template("03/index.html")

@app.route("/calc/<a>")
def calc(a):
    return converter(a)