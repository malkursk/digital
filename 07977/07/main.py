from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def main():
    return f"Работа №7: Flask. Васильева Мария Валерьевна, гр. 44-23-168"


@app.route("/2")
def lab2():
    return render_template('02/index.html')

@app.route("/3")
def lab3():
    return render_template('03/index.html')







