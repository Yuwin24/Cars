class Car:
    def __init__(self,tyres,speed,company,color) :
        self.tyres = tyres
        self.speed = speed
        self.company = company
        self.color = color

    def calculate_speed(self,distance,time):
        speed = distance/time
        return speed



    def car_tyres(self):
        print("No of Tyres", self.tyres)
    
    def car_details(self):
        print("No of Tyres", self.tyres)
        print("Speed of car", self.speed)
        print("Company of car", self.company)
        print("color of car", self.color)

Car1 = Car(4,1205,"Ferrari","Red")
Car1.car_tyres()
Car1.car_details()
print("Speed of car is ", Car1.calculate_speed(120,30))
distance = int(input("Distance = "))
time = int(input("Time = "))
speed = Car1.calculate_speed(distance,time)
print(speed)