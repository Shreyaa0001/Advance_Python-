#Write a program to implement a Configurable Payment Processing System Using Strategy Pattern.
# Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


# Context Class
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Usage
processor = PaymentProcessor(UPIPayment())
processor.process_payment(500)

processor.set_strategy(CreditCardPayment())
processor.process_payment(1200)

processor.set_strategy(PayPalPayment())
processor.process_payment(2000)