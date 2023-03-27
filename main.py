class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f'Name: {self.name}, breed: {self.breed}')


dog = Dog("Arnie", "Pug", 7)
dog.bark()
