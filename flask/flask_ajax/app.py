from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_image')
def get_image():
    parameter_dict = request.args.to_dict()
    print(parameter_dict['id'])
    image_id = parameter_dict['id']
    image_filename = "01_result.jpg"
    if image_id == "image1":
        image_filename = "01_result.jpg"
    elif image_id == "image2":
        image_filename = "02_result.jpg"
    return render_template('ajax_image.html', image_filename=image_filename)


if __name__ == '__main__':
    app.run()
