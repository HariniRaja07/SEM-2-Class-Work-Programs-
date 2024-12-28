class Commerce: 
    def __init__(self,base_price,discount_percentage=0,tax_percentage=0): 
        self.base_price=base_price 
        self.discount_percentage=discount_percentage 
        self.tax_percentage=tax_percentage 
    def calculate_final(self): 
        if base_price <0 or discount_percentage <0 or tax_percentage<0: 
            raise ValueError ("Invalid amount") 
        else: 
            discount_amount=((discount_percentage)/100)*base_price 
            tax_amount=(tax_percentage/100)*base_price 
            total_price=(base_price+tax_amount)-discount_amount 
            return total_price 
base_price=float(input("Enter the base price of the product")) 
tax_percentage=float(input("Enter the tax percentage")) 
discount_percentage=float(input("enter the discount percentage")) 
 
try: 
    c=Commerce(base_price,discount_percentage,tax_percentage) 
    result=c.calculate_final() 
    print(result) 
except ValueError as e: 
    print(e) 
