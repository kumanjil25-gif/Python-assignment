class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
p=Person("Prabisha", 18)
print(p.__dict__)