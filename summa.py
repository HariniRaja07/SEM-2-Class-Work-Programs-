class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayEmployeeInfo(self):
        print(f"Name:{self.name}\nAge:{self.age}")

class Manager(Employee):
    def __init__(self,name,age,eid):
        Employee.__init__(self,name,age)
        self.eid=eid
    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print(f"Employee Id:{self.eid}")

class Developer(Employee):
    def __init__(self,name,age,dept):
        Employee.__init__(self,name,age)
        self.dept=dept
    def displayDeveloperInfo(self):
        print(f"Department:{self.dept}")

class TeamLeader(Manager,Developer):
    def __init__(self,name,age,eid,dept,teamsize):
        Manager.__init__(self,name,age,eid)
        self.dept=dept
        self.teamsize=teamsize
    def displayTeamLeaderInfo(self):
        self.displayManagerInfo()
        print(f"Department:{self.dept}\nTeamSize:{self.teamsize}")


Name=input("Enter your name:")
Age=int(input("Enter your age:"))
Eid=input("Enter your EmployeeId:")
Dept=input("Enter your Department:")
Teamsize=input("Enter your TeamSize:")

details=TeamLeader(Name,Age,Eid,Dept,Teamsize)
details.displayTeamLeaderInfo()
