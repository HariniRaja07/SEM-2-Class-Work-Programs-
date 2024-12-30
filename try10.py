def Type(phone):
    if phone[0:3].isdigit() and phone[3]=="-" and phone[4:8].isdigit():
        return "The Phone number is valid"
    else:
        return "Enter the valid phone number"
phone=input("Enter a phone number:")
print(Type(phone))
