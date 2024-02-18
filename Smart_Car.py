import math
import random


class SmartCar:

    def __init__(self, x, y, xMove, yMove, aCheck, speed):
        self.speed = speed  # current speed of the car
        self.original_speed = speed
        self.original_xMove = xMove
        self.original_yMove = yMove
        # self.turning = False  # indicates whether the car is currently turning
        # self.turn_destination = None  # destination after turning
        self.x = x
        self.y = y
        self.xMove = xMove
        self.yMove = yMove
        self.aCheck = aCheck

        if random.randint(0, 1) == 1:
            self.moveOut = False
        else:
            self.moveOut = True

    def update_x(self, new_x):
        self.x = new_x

    def update_y(self, new_y):
        self.y = new_y

    def update_speed(self, new_speed):
        self.speed = new_speed

    def add_other_car(self, car):
        print("Adding other car")
        self.other_cars.append(car)

    def avoid_collision(self, other_cars):
        for car in other_cars:
            if car != self:  # Don't compare the car to itself
                # Calculate the future positions of the cars
                future_self_x = self.x + self.xMove * self.speed
                future_self_y = self.y + self.yMove * self.speed
                future_car_x = car.x + car.xMove * car.speed
                future_car_y = car.y + car.yMove * car.speed

                # Calculate the distance between the future positions
                distance = math.sqrt(
                    (future_car_x - future_self_x) ** 2
                    + (future_car_y - future_self_y) ** 2
                )

                if distance < 95:  # Assuming each car has a radius of 25 units
                    print(
                        "Collision predicted between cars at positions",
                        self.x,
                        self.y,
                        "and",
                        car.x,
                        car.y,
                    )

                    # Handle predicted collision here
                    if (self.x >= 100 and self.x <= 300) and (
                        self.y >= 100 and self.y <= 300
                    ):
                        self.xMove *= 1.1
                        self.yMove *= 1.1
                        car.xMove *= 0.9
                        car.yMove *= 0.9
                    elif (
                        (self.x >= 100 and self.x <= 300)
                        and (self.y >= 100 and self.y <= 300)
                        and (car.x >= 100 and car.x <= 300)
                        and (car.y >= 100 and car.y <= 300)
                    ):
                        if self.moveOut == car.moveOut:
                            self.moveOut = not self.moveOut
                        if self.moveOut:
                            self.xMove *= 1.1
                            self.yMove *= 1.1
                            car.xMove *= 0.9
                            car.yMove *= 0.9
                    else:
                        self.xMove *= 0.9
                        self.yMove *= 0.9  # Reduce speed to avoid collision
                        car.xMove *= 1.1
                        car.yMove *= 1.1
                else:
                    if self.xMove != self.original_xMove:
                        self.xMove += (self.original_xMove - self.xMove) / 15
                    elif self.yMove != self.original_yMove:
                        self.yMove += (self.original_yMove - self.yMove) / 15

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
            self.update_speed(
                min(self.speed, sender.speed)
            )  # Adjust speed based on the other car's speed

    # def turn(self, direction, destination):
    #     self.turning = True
    #     self.turn_destination = destination
    #     # Perform turning logic here

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
# car1 = SmartCar((100, 200))
# car2 = SmartCar((150, 250))

# car1.add_other_car(car2)
# car2.add_other_car(car1)

# car1.update_speed(5)
# car2.update_speed(3)

# car1.drive_to_destination()
# car2.drive_to_destination()
