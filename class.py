class car:
    def __init__(self, model, color, year, customer, amount):
        self.model = model
        self.color = color
        self.year = year
        self.customer = customer
        self.amount = amount

    def printdata(self):
        print(self.model)
        print(self.color)
        print(self.year)
        print(self.customer)
        print(self.amount)

bmw = car("3 series","red","2020","pradde","250000")
benz = car("c class","blue","2021","vinoth","650000")

bmw.printdata()
benz.printdata()



