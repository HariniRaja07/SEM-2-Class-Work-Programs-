class Students:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def display(self):
        print(f"Sname:{self.name}\nSage:{self.age}\nScourse:{self.course}")


class Students_Info:
    def __init__(self,s_mail_id,s_no):
        self.s_mail_id=s_mail_id
        self.s_no=s_no
    def display_info(self):
        print(f"Smail_id:{self.s_mail_id}\nS_no:{self.s_no}")

    
class Details(Students,Students_Info):
    def __init__(self,name,age,course,s_mail_id,s_no,p_mail_id,p_no):
        super().__init(name,age,course)
        Students_info.__init__(s_mail_id,s_no)
        self.p_mail_id=p_mail_id
        self.p_no=p_no
    def show(self):
        self.display()
        self.display_info()
        print(f"Pmail_id:{self.p_mail_id}\nPno:{self.p_no}")


obj1=Details()
obj1.show()
