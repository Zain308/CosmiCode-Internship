class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"

def animal_sound(animal):
    print(animal.speak())

if __name__ == "__main__":
    # Example usage
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    bird = Bird("Tweety")
    
    animal_sound(dog)
    animal_sound(cat)
    animal_sound(bird)