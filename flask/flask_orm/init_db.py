from app import db, Menu


if __name__ == '__main__':
    db.create_all()
    db.session.add(Menu(name='Bulgogi', price=15000))
    db.session.add(Menu(name='Samgyeopsal', price=12000))
    db.session.add(Menu(name='Ddukbokki', price=4000))
    db.session.add(Menu(name='Bibimbap', price=8000))
    db.session.add(Menu(name='Seolleongtang', price=10000))
    db.session.commit()
