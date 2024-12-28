import re
def verify_password(password):
    ex=r'^(?=.*[A-Z].*[a-z].*[0-9])(?!.[(!@#$%^&*()-_+=)]).{8,}$'
    
    if re.match(ex,password):
        print("Password is strong")
    else:
        print("Password is not strong")
        
password=input("Enter the password:")
verify_password(password)


#----->(?=.)----->must present(irukanum)
#----->(?!.)------>must not present(irukakoodathu)
