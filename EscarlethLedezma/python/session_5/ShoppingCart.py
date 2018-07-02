from EscarlethLedezma.python.session_5.Shop import Shop


class ShoppingCart:
    def __init__(self, shop):
        self.shop = shop
        self.items_purchase_amount = {}
        self.items_purchase_price = {}

    def add_purchase(self):
        '''Add a new purchase according to valid items'''
        item = input('Insert the item to purchasing:')
        quantity = int(input('Insert the quantity to purchasing(only numbers):'))
        while True:
            if self.shop.verify_availability(item, quantity):
                self.items_purchase_amount[item] = quantity
                self.items_purchase_price[item] = quantity * self.shop.get_price_item_in_shop(item)
                self.shop.update_amount_item(item, quantity)
                break
            else:
                print('The item is not available')
                break

    def perform_purchase(self):
        '''Perform a new purchase'''
        while True:
            continue_purchase = input('Do you wanna buy?(yes/no)')
            if continue_purchase.lower() == 'yes':
                self.add_purchase()
            else:
                break

    def calculate_total_price(self):
        '''Calculate the total price purchase'''
        total_price = 0
        for i in self.items_purchase_price:
            total_price += self.items_purchase_price[i]
        return total_price

    def print_products_purchased(self):
        '''Print the purchase with name items and prices'''
        print('********PURCHASED ITEMS********')
        for item in self.items_purchase_price:
            print('ITEM:', item)
            print('TOTAL_PRICE:', self.items_purchase_price[item])
            print('*******************************')

    def balance(self, cash_paid):
        '''Pay the purchase'''
        total_price = int(self.calculate_total_price())
        if cash_paid < total_price:
            return "Cash paid not enough"
        return cash_paid - total_price


print('******************Welcome to Shopping Page******************')
store = Shop()
store.add_item('A8', 500, 10)
store.add_item('A7', 400, 10)
store.add_item('A6', 300, 10)

shopping_cart = ShoppingCart(store)

shopping_cart.perform_purchase()
shopping_cart.print_products_purchased()
print('The total price is:', shopping_cart.calculate_total_price())
print('The balance is:', shopping_cart.balance(100))
