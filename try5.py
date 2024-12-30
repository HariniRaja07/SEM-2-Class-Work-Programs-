import re
def verify_password(password):
    ex=r'^(?=.*[A-Z].*[A-Z].*[A-Z])(?=.*[a-z])(?!.*[0-9])(?!.*[(!@#$%^&*()_+-=)]).{8,12}'
    if re.match(ex,password):
        print("The Password is strong")
    else:
        print("The Passwor is not strong,make a Strong password")
p=input("Enter your Password:")
verify_password(p)
