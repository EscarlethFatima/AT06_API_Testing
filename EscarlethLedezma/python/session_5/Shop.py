from EscarlethLedezma.python.session_5.Item import Item


class Shop:

    def __init__(self):
        self.list_items = []

    def add_item(self, name_item, price, quantity):
        '''Add a new item in the shop'''
        self.list_items.append(Item(name_item, price, quantity))

    def verify_availability(self, name_item, quantity):
        '''Verify if a item is available'''
        for item in self.list_items:
            return name_item == item.name and 0 < quantity <= item.quantity

    def get_price_item_in_shop(self, name_item):
        '''Return the price given the name item'''
        for item in self.list_items:
            if name_item == item.name:
                return item.price

    def update_amount_item(self, name_item, quantity):
        '''Update the stock'''
        for item in self.list_items:
            if name_item == item.name:
                item.quantity -= quantity
