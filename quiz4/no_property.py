
class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def name(self):
        print(self.year+" "+self.make+" "+self.model)
    


#test material
myCar = Cars("Ford", "Mustang", "2002")
myCar.name()

#test material