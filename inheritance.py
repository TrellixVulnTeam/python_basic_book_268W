class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old!"

    def speak(self,sound):
        return f"{self.name} says {sound}"


class Jack(Dog):
    def speak(self,sound="Arf"):
        return f"{self.name} says {sound}"


miles = Jack("two", 24, "jackie")
miles.speak()
