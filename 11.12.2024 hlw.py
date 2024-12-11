#1.
import re
class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def validate(self):
        if len(self.password) < 8:
            return "Invalid: Password must be at least 8 characters long."
        if not any(char.isupper() for char in self.password):
            return "Invalid: Password must have at least one uppercase letter."
        if not any(char.islower() for char in self.password):
            return "Invalid: Password must have at least one lowercase letter."
        if not any(char.isdigit() for char in self.password):
            return "Invalid: Password must have at least one digit."
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", self.password):
            return "Invalid: Password must have at least one special character."
        
        return "Valid: Password meets all the requirements."

password = input("Enter your password: ")
validator = PasswordValidator(password)
result = validator.validate()
print(result)


#2.
class TextProcessor:
    def __init__(self, text):
        self.text = text

    def split_into_sentences(self):
        return self.text.split(". ")

    def process_sentences(self):
        sentences = self.split_into_sentences()
        result = []
        for sentence in sentences:
            clean_sentence = sentence.strip(".!?").strip()
            word_count = len(clean_sentence.split())
            result.append((sentence.strip(), word_count))
        return result
text = input("Enter a paragraph of text: ")
processor = TextProcessor(text)
sentences = processor.split_into_sentences()
print("Split Sentences:")
for sentence in sentences:
    print(f"\"{sentence.strip()}\"")
processed = processor.process_sentences()
print("\nProcessed Sentence Data:")
for sentence, word_count in processed:
    print(f"Sentence: \"{sentence}\", Word Count: {word_count}")

    
