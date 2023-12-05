from flask import Flask, render_template

app = Flask(__name__)

def converter(v,b1=17,b2=12):   
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

@app.route("/")
def main():
    return "Практическая работа 7. Flask. <h2>Костинова Мария Анатольевна</h2> гр. - 44-23-167"


@app.route("/02")
def route02():
    return render_template("02/index.html")


@app.route("/03")
def route03():
    return render_template("03/index.03.html")


