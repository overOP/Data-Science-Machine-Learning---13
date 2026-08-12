print("Hello, Pradeep")

class A:
    def __init__(self, name: str, home: str) -> str:
        self.name = name
        self.home = home

class B(A):
    def __init__(self, name: str, home: str, newhome: str):
        super().__init__(name, home)
        self.newhome = newhome

class C(B):
    def __init__(self, name: str, home: str, newhome: str, car: str):
        super().__init__(name, home, newhome)
        self.car = car

    def all_data(self):
        return f"\nname: {self.name}\nhome: {self.home}\nnewhome: {self.newhome}\ncar: {self.car}"

data = C("pradeep", "mnr", "ktm", "bmw")

print(data.all_data())