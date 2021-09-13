from app import Menu


if __name__ == '__main__':
    for menu in Menu.query.all():
        print('id: {}'.format(menu.id))
        print('name: {}'.format(menu.name))
        print('price: {} WON'.format(menu.price))
