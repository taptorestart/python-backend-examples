from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os


PROJECT_PATH = os.getenv('PROJECT_PATH')
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}/db.sqlite'.format(PROJECT_PATH)
db = SQLAlchemy(app)


# Model
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))
    price = db.Column(db.Integer)


# Home
@app.route('/')
def index():
    return "Welcome in our restaurant!"


# GET /menus
@app.route('/menus', methods=['GET'])
def get_menus():
    menus = []
    for m in Menu.query.all():
        menu = {}
        menu['id'] = m.id
        menu['name'] = m.name
        menu['price'] = m.price
        menus.append(menu)
    return jsonify({"menus": menus})


# GET /menus/id
@app.route('/menus/<int:menu_id>', methods=['GET'])
def get_menus_by_id(menu_id):
    m = Menu.query.filter_by(id=menu_id).first()
    menu = {}
    menu['id'] = m.id
    menu['name'] = m.name
    menu['price'] = m.price
    return menu


# POST /menus
@app.route('/menus', methods=['POST'])
def create_menus():
    req = request.get_json()
    print(req)
    menu = Menu(name=req['name'], price=req['price'])
    db.session.add(menu)
    db.session.commit()
    return jsonify(req), 201


# PUT /menus
@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menus(menu_id):
    req = request.get_json()
    Menu.query.filter_by(id=menu_id).update(dict(name=req['name'], price=req['price']))
    db.session.commit()
    return jsonify(req)


# DELETE /menus
@app.route('/menus/<int:menu_id>', methods=['DELETE'])
def delete_menus(menu_id):
    Menu.query.filter_by(id=menu_id).delete()
    db.session.commit()
    return ''
