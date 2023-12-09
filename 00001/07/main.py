import json
import time
import os   
import datetime
import functions
from flask import render_template, Flask, request, jsonify, send_from_directory
from sqlalchemy.dialects.postgresql import JSON

from flask_restful import Resource, reqparse, abort, fields, marshal_with
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy


UPLOAD_FOLDER = 'C:/!Test/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'dat'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class WorkModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file = db.Column(db.String(255), nullable=False)
    params = db.Column(JSON, nullable=False)
    result_file = db.Column(db.String(255))
    time_to_operations = db.Column(db.Float)
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'file': self.file,
            'params': self.params,
            'createAt': self.createAt,
            'result_file': self.result_file,
            'time_to_operations': self.time_to_operations
        }


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

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/works', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(filename)

            dct = functions.build_dictionary(request.form)
            start = time.time()
            result = functions.crypto_cell(filename, dct)
            if os.path.isfile(result):
                work = WorkModel(file=request.files['file'].filename, params=json.dumps(dct),
                                 time_to_operations=time.time() - start,
                                 result_file='http://127.0.0.1:5000/files/' + os.path.basename(result))
                db.session.add(work)
                db.session.commit()
                return {"result": work.serialize, }, 200

            return {"result": 'неверные параметры', }, 400

        if request.method == 'GET':
            works = WorkModel.query.all()
            return jsonify(works=[i.serialize for i in works])

    except:
        return {"result": 'неверные параметры', }, 400

@app.route('/files/<name>', methods=['GET'])
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


app.add_url_rule(  # оставляет в браузере строку адреса при скачивании
    "/files/<name>", endpoint="download_file", build_only=True
)


@app.route('/delete/<name>', methods=['GET'])
def delete_file(name):

    pth = app.config["UPLOAD_FOLDER"] + name
    if os.path.exists(pth):
        os.remove(pth)
        return {'result': 'файл успешно удален'}, 410

    return {'result': 'файл не найден'}, 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
app.run()   