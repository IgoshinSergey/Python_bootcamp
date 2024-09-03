from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from mimetypes import guess_type
import os


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        file = request.files['file']
        if file:
            mimetype = guess_type(file.filename)[0]
            if mimetype and mimetype.startswith('audio/'):
                file.save(os.path.join(UPLOAD_FOLDER, secure_filename(file.filename)))
                return render_template('index.html', files=os.listdir(UPLOAD_FOLDER))
            else:
                return "Non-audio file detected", 400

    return render_template('index.html', files=os.listdir(UPLOAD_FOLDER))


@app.route('/files', methods=['GET'])
def get_files():
    return os.listdir(UPLOAD_FOLDER)


if __name__ == "__main__":
    app.run(debug=True, port=8888)
