class Order:
    def __init__(self, customer_name, food_item, order_amount, category):
        self.customer_name = customer_name
        self.food_item = food_item
        self.order_amount = order_amount
        self.category = category

    def display(self):
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Order Amount:", self.order_amount)
        print("Category:", self.category)

class Restaurant:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def display_all_orders(self):
        print("\nAll Orders:")
        for order in self.orders:
            order.display()

o1 = Order("Shreyaa", "Paneer Tikka", 250, "Veg")
o2 = Order("Kirti", "Chicken Biryani", 300, "Non-Veg")
o3 = Order("Shreya", "Masala Dosa", 150, "Veg")
r = Restaurant()
r.add_order(o1)
r.add_order(o2)
r.add_order(o3)
r.display_all_orders()