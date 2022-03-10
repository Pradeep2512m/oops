class government:
    def __init__(self):
        self.__price = 108

    def viewpetrolprice(self):
        print(self.__price)

    def hikeprice(self, price):
        self.__price = price

centralgovernment = government()
centralgovernment.viewpetrolprice()

centralgovernment.__price = 165
centralgovernment.viewpetrolprice()

centralgovernment.hikeprice(467)
centralgovernment.viewpetrolprice()