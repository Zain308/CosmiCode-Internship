class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start_engine(self):
        return f"{self.brand} {self.model}'s engine started."
    
    def stop_engine(self):
        return f"{self.brand} {self.model}'s engine stopped."

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def honk(self):
        return f"{self.brand} {self.model} honks: Beep Beep!"
    
    def start_engine(self):
        return f"{self.brand} {self.model}'s V6 engine roars to life."

class Bike(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar
    
    def wheelie(self):
        return f"{self.brand} {self.model} pops a wheelie!"
    
    def start_engine(self):
        return f"{self.brand} {self.model}'s engine revs up."

if __name__ == "__main__":
    # Example usage
    car = Car("Toyota", "Camry", 2020, 4)
    print(car.start_engine())
    print(car.honk())
    print(car.stop_engine())
    
    bike = Bike("Harley-Davidson", "Sportster", 2018, False)
    print(bike.start_engine())
    print(bike.wheelie())
    print(bike.stop_engine())