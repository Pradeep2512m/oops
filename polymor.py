class birds:
    def fly(self):
        print("all birds can fly")

class pigeon(birds):
    def fly(self):
        super().fly()
        print("pigeon can fly")

ob = pigeon()
ob.fly()
