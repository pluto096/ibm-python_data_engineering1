"""
Created on Sat Jul 15 12:07:36 2023

@author: oluwapelumi
"""
#Car dealership's inventory management system.

class Vehicle:
    #initializing defult color for all vehicles to white
    color = "white"

    #Constructor
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seat_capacity = None
    
    #Assign seating capacity to a vehicle
    def assignSeatCapacity(self, seat_capacity):
        self.seat_capacity = seat_capacity
    #Display properties of the car   
    def displayProp(self):
        print("Properties:")
        print("The max speed of the car is: ", self.max_speed)
        print("The colour of the car is: ", self.color)
        print("The mileage of the car is: ", self.mileage)
        print("The seating capacityof the car is: ", self.seat_capacity)        

#create the first object
vehicle1 = Vehicle(200, 50000)
vehicle1.assignSeatCapacity(5)
vehicle1.displayProp()

#create the second object
vehicle2 = Vehicle(180, 75000)
vehicle2.assignSeatCapacity(4)
vehicle2.displayProp()
