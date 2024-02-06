from collections.abc import Iterable

class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @property
    def name(self):
        return (self.year+" "+self.make+" "+self.model)
    


#test material
myCar = Cars("Ford", "Mustang", "2002")
print(myCar.name)

#test material