class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = [] 
        
    def __repr__(self):
        return f"<Customer: {self.name}>"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")
    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))
    
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        customers = coffee.customers()
        if not customers:
            return None
        return max(customers, key=lambda c: sum(o.price for o in c.orders() if o.coffee == coffee))


