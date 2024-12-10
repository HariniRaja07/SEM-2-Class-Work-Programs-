#1.
class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

    def take_photo(self):
        print(f"Taking photo with resolution: {self.resolution}")

class Phone:
    def __init__(self, number):
        self.number = number

    def make_call(self):
        print(f"Calling to {self.number}")

    def send_message(self,message):
        print(f"Sending message to {self.number}: {message}")

class Smartphone(Camera, Phone):
    def __init__(self, resolution, number, brand, model):
        Camera.__init__(self, resolution)
        Phone.__init__(self, number)
        self.brand = brand
        self.model = model

    def display_device_info(self):
        self.take_photo()
        self.make_call()
        self.send_message("How are you?")

mobile= Smartphone("12MP", "7200211680", "Samsung", "Galaxy S21")
mobile.display_device_info()


#2.
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def student_info(self):
        print(f"Student Name: {self.name}\nCourse: {self.course}")

class StudentAthlete(Student):
    def __init__(self, name, course, sports):
        super().__init__(name, course)
        self.sports = sports

    def display_athlete_info(self):
        self.student_info()
        print(f"Sports: {self.sports}")

obj = StudentAthlete("Harini", "Artificial Intelligence", "Badminton")
obj.display_athlete_info()

