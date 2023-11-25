from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return f"Работа №7. Flask. Булгакова Виктория Николаевна, гр. 44-23-167"

@app.route("/02")
def lab02():
    return render_template ('02/index.html')

@app.route("/03")
def lab03():
    return render_template ('03/index.html')