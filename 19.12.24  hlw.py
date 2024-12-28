#1.
def int_to_roman(num):
    roman_mappings = [
        (1000, "M"), (900, "CM"),
        (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"),
        (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"),
        (5, "V"), (4, "IV"),
        (1, "I")
    ]

    result = ""
    for value, symbol in roman_mappings:
        while num >= value:
            result += symbol
            num -= value

    return result
number = int(input("Enter an integer to convert to Roman numeral: "))
print(f"The Roman numeral for {number} is {int_to_roman(number)}")


#2.
sym=input()
roman_mappings = [("M",1000), ("CM",900),
        ("D",500), ("CD"400),
        ("C",100), ("XC"90),
        ("L",50), ("XL",40),
        ("X",10), ("IX",9),
        ("V",5), ("IV",4),
        ("I",1)]
num=0
for i in sym:
    
    
