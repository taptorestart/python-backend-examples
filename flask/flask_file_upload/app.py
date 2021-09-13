from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload_test')
def upload():
    return render_template("upload.html")


@app.route('/upload_test_with_simple_button')
def upload_test_with_simple_button():
    return render_template("upload_simple_button.html")


# https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/
@app.route('/upload_test_with_secure_filename')
def upload_test_with_secure_filename():
    return render_template("upload_test_with_secure_filename.html")


@app.route('/upload', methods=['POST'])
def post_upload_file():
    file = request.files['file']
    filename = file.filename
    path_to_save = "static/files"
    file.save(os.path.join(path_to_save, filename))
    filepath = "files/" + filename
    print(file.content_type)
    if 'image' in file.content_type:
        return render_template("uploaded_image.html", filepath=filepath)
    else:
        return filename


@app.route('/upload_with_secure_filename', methods=['POST'])
def upload_and_save_secure_filename():
    file = request.files['file']
    filename = secure_filename(file.filename)
    path_to_save = "static/files"
    file.save(os.path.join(path_to_save, filename))
    filepath = "files/" + filename
    print(file.content_type)
    if 'image' in file.content_type:
        return render_template("uploaded_image.html", filepath=filepath)
    else:
        return filename


if __name__ == '__main__':
    app.run()
