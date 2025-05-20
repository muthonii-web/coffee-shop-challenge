class Coffee:
    def __init__(self, name):
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)

    def add_order(self, order):
        self._orders.append(order)

    def customers(self):
        return list(set(order.customer for order in self._orders))
