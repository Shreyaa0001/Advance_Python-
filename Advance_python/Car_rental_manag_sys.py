class Car:
    def __init__(self,car_no,Model,Rent_per_day,category):
        self.car_no = car_no
        self.Model = Model
        self.Rent_per_day = Rent_per_day
        self.category = category
    def display(self):
        print("Car number:",self.car_no)
        print("Model:",self.Model)
        print("Rent of the car per day:",self.Rent_per_day)
        print("Car category:",self.category)
class RentalAgency:
    def __init__(self):
        self.cars=[]
    def add_car(self,car):
        self.cars.append(car)        
    def display_all_cars(self):
        print("\n All Details:")
        for car in self.cars:
            car.display()


c1 = Car(9559,"i7","2000","Luxury")  
c2 = Car(3443,"i5","3000","Sedan")
d = RentalAgency()
d.add_car(c1)
d.add_car(c2)
d.display_all_cars() 
        