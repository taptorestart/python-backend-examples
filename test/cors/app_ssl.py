import ssl

from flask import Flask, render_template

context = ssl.SSLContext()
pem = "/Users/taptorestart/local.taptorestart.com.pem"  # Set your pem file path
key = "/Users/taptorestart/local.taptorestart.com-key.pem"  # Set your key pem file path
context.load_cert_chain(pem, key)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


HOST = 'local.taptorestart.com'
PORT = 8000


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True, ssl_context=context)
