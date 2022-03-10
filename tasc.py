class student:
    def __init__(self, name, rollno, admndno, college):
        self.name = name
        self.rollno = rollno
        self.admndno = admndno
        self.college = college

    def printdata(self):
        print(self.name)
        print(self.rollno)
        print(self.admndno)
        print(self.college)

person1 = student("pradeep","1524","746","ace")
person2 = student("vinoth","7832","264","ahe")


person1.printdata()
person2.printdata()



