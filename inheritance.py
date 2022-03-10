class person(object):
    def __init__(self,name,aadhar,phone):
        self.name = name
        self.aadhar = aadhar
        self.phone = phone

    def displaydetails(self):
        print(self.name + "\n" + self.aadhar + "\n" + self.phone)

class employee(person):
    def __init__(self,name,aadhar,phone,salary,designation):
        self.salary = salary
        self.designation = designation

        person.__init__(self,name,aadhar,phone)

    def printdetails(self):
        print("name =", self.name)
        print("aadhar =", self.aadhar)
        print("phone =", self.phone)
        print("salary =", self.salary)
        print("designation =", self.designation)

x = employee("pradeep","54678","84956313","30000","manager")
x.printdetails()
x.displaydetails()