class CashRegister:
    def __init__(self, cashier_name):
        self.cashier_name = cashier_name
        self.purchase = []

    def add_product(self, product, quantity=1):
        for item in self.purchase:
            if item["product"] == product:
                item["quantity"] += quantity
                return

        self.purchase.append({"product": product, "quantity": quantity, "price": product["price"]})

    def remove_product(self, product, quantity=1):
        for item in self.purchase:
            if item["product"] == product:
                if item["quantity"] <= quantity:
                    self.purchase.remove(item)

                else:
                    item["quantity"] -= quantity

                return

    def update_product_price(self, product, price):
        for item in self.purchase:
            if item["product"] == product:
                item["price"] = price
                return

    def get_purchase_items(self):
        return self.purchase

    def get_subtotal(self):
        subtotal = 0
        for item in self.purchase:
            subtotal = item["price"] * item["quantity"]
        return subtotal

    def get_total_taxes(self):
        subtotal = self.get_subtotal()
        return subtotal * 0.05
    def get_total(self):
        subtotal = self.get_subtotal()
        taxes = self.get_total_taxes()
        return subtotal + taxes

    def clear_purchase(self):
        self.purchase = []


product1 = {"name":"Pizza", "price": 9.99}
product2 = {"name": "Salad", "price": 5.99}
product3 = {"name": "Kebab", "price": 4.99}


register = CashRegister("Stefan")


register.add_product(product1)
register.add_product(product2, 3)
register.add_product(product3, 5)
print(register.get_purchase_items())

register.remove_product(product2, 1)

print(register.get_purchase_items())


register.update_product_price(product1, 14.99)

print(register.get_purchase_items())

print(register.get_subtotal())

print(register)