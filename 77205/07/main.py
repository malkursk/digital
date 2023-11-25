from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def main():
    return f"Работа №7. Flask. Назарова София МИхайловна, гр.44-23-169" 

@app.route("/2")
def lab2():
    return render_template('lab2/lab2.html')

@app.route("/3")
def lab3():
    return render_template('lab3/lab3.html')



