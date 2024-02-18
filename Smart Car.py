import math

class SmartCar:
    def __init__(self, destination):
        self.speed = 0  # current speed of the car
        
        
        self.position = (0, 0)  # current position of the car (x, y)
        self.destination = destination  # destination of the car
        
        
        
        self.turning = False  # indicates whether the car is currently turning
        self.turn_destination = None  # destination after turning
        self.other_cars = []  # list of other cars nearby
        
    def update_position(self, new_position):
        self.position = new_position

    def update_speed(self, new_speed):
        self.speed = new_speed

    def add_other_car(self, car):
        self.other_cars.append(car)

    def avoid_collision(self):
        for car in self.other_cars:
            distance = math.sqrt((car.position[0] - self.position[0])**2 + (car.position[1] - self.position[1])**2)
            if distance < 10:  # Assuming a safe distance of 10 units
                if self.turning and car.turning:
                    if self.turn_destination == car.turn_destination:
                        # Cars have same turn destination, adjust speed to avoid collision
                        self.update_speed(min(self.speed, distance - 1))
                else:
                    # Adjust speed to avoid collision
                    self.update_speed(min(self.speed, distance - 1))

    def communicate_intent(self):
        for car in self.other_cars:
            car.receive_intent(self, self.turning, self.turn_destination)

    def receive_intent(self, sender, turning, turn_destination):
        # Receive intent from another car
        if self.turning and turning:
            if self.turn_destination == turn_destination:
                # Both cars have same turn destination, adjust behavior
                # For example, one car could slow down to allow the other to turn first
                pass
        # Handle other cases as needed
        if not turning and not self.turning:  # If both cars are going straight
            self.update_speed(min(self.speed, sender.speed))  # Adjust speed based on the other car's speed

    def turn(self, direction, destination):
        self.turning = True
        self.turn_destination = destination
        # Perform turning logic here

    def drive_to_destination(self):
        while self.position != self.destination:
            self.avoid_collision()
            self.communicate_intent()  # Exchange intentions with other cars
            if self.turning:
                if self.position == self.turn_destination:
                    self.turning = False
                    self.turn_destination = None
                else:
                    continue  # Wait until reaching the turn destination
            # Drive towards destination
            self.update_position((self.position[0] + self.speed, self.position[1]))


# Example usage:
car1 = SmartCar((100, 200))
car2 = SmartCar((150, 250))

car1.add_other_car(car2)
car2.add_other_car(car1)

car1.update_speed(5)
car2.update_speed(3)

car1.drive_to_destination()
car2.drive_to_destination()
