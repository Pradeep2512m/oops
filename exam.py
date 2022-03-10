class student(object):
    def __init__(self,name,rollno,admndno,college):
        self.name = name
        self.rollno = rollno
        self.admndno = admndno
        self.college = college

    def displaydetails(self):
        print(self.name + "\n" + self.rollno + "\n" + self.admndno + "\n" + self.college)

class exam(student):
    def __init__(self,name,rollno,admndno,college,examname,englishmark,mathsmark,physicsmark,chemistrymark):
        self.examname = examname
        self.englishmark = englishmark
        self.mathsmark = mathsmark
        self.physicsmark = physicsmark
        self.chemistrymark = chemistrymark

        student.__init__(self,name,rollno,admndno,college)

    def printdetails(self):
        print("name =", self.name)
        print("rollno =", self.rollno)
        print("admndno =", self.admndno)
        print("college =", self.college)
        print("examname =", self.examname)
        print("englishmark =", self.englishmark)
        print("mathsmark =", self.mathsmark)
        print("physicsmark =", self.physicsmark)
        print("chemistrymark =", self.chemistrymark)

x = exam("pradeep","377","5748","ace","semester","46","67","86","69")
x.printdetails()
x.displaydetails()