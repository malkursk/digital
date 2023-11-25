from flask import Flask, render_template

app = Flask(__name__)

@app.route("/calc/<a>/<b>")
def calc(a,b):
    return f"{int(a)*int(b)}"

@app.route("/")
def main():
    return f"Работа №7. Flask. Иванова Мария Петровна, гр. 44-22-180"

@app.route("/02")
def lab02():
    return render_template('02/index.html')

@app.route("/03")
def lab03():
    return render_template('03/index.html')

# flask --app main run

