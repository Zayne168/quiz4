from dataclasses import dataclass

@dataclass
class fish:
    def __init__(self, species: str, price: float, weight: float): #$/lbs.
        self.species=species
        self.price=price
        self.weight=weight
    def __repr__(self) -> str:
        return f"Fish('{self.species}', ${self.price:.2f}, {self.weight}lbs.)"
    def addWeight(self,data)->None:
        self.weight+=data

#test material
myFish=fish("Goldfish", 2.99, 5.5)
print(myFish)
myFish.addWeight(4)
print(myFish)
#test material