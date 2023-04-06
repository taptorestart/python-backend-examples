from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


HOST = 'local.taptorestart.com'
PORT = 8000


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
