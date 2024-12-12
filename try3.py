#1.
class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def first(self):
        if not self.password[0].isupper():
            return "Invalid: Password must have to start with Uppercase."
    def validate(self):
        if len(self.password) <8:
            return "Invalid: Password must be at least 8 characters long."
        if not any(char.isupper() for char in self.password):
            return "Invalid: Password must have at least one uppercase letter."
        if not any(char.islower() for char in self.password):
            return "Invalid: Password must have at least one lowercase letter."
        if not any(char.isdigit() for char in self.password):
            return "Invalid: Password must have at least one digit."
        
        special_characters = "!@#$%^&*(),.?\":{}|<>"
        if not any(char in special_characters for char in self.password):
            return "Invalid: Password must have at least one special character."
        return "Valid: Password meets all the requirements."

password = input("Enter your password: ")
validator = PasswordValidator(password)
re=validator.first()
result=validator.validate()
print(re)
print(result)
