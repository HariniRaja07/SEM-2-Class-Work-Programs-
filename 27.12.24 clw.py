class CreditCardPayment:
    def pay(self,amount):
        return f" The Amount {amount} is paid using Credit Card"

class PayPalPayment:
    def pay(self,amount):
        return f" The Amount {amount} is paid using PayPal"

class DebitCardPayment:
    def pay(self,amount):
        return f" The Amount {amount} is paid using Dedit Card"

class Payment:
    def payment(self,amount):
        return f" The Amount {amount} is paid "

def process_payment(object_getter,amount):
    print(object_getter.pay(amount))

cc=CreditCardPayment()
process_payment(cc,1000)

pp=PayPalPayment()
process_payment(pp,4000)

dc=DebitCardPayment()
process_payment(dc,6000)

