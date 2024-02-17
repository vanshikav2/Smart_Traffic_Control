# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from queue import Queue
from random import random


class Car:
    """ Car object contains the automated car model that interacts with other Car
    Objects and Intersection Objects

    ==== Attributes ====
    Destination: The destination of the car
    Lane: The current lane of the car
    Signal: The signal from the other car or intersection
    move: The direction of the car
    Speed: The speed of the car

    """
    def __init__(self, destination, speed, lane):
        self.destination = destination
        self.speed = speed
        self.lane = lane
        self.signal = None

    def reduce_speed(self):
        """
        Reduce speed to avoid collision
        """
        self.speed -= 5  # Example reduction rate, adjust as needed
        if self.speed < 0:
            self.speed = 0

    def change_lane(self, side):
        """
        Change lane if possible
        """
        if side == "right":
            self.lane = "Right"
        else:
            self.lane = "Left"

    def stop(self):
        """
        Stop the car
        """
        self.speed = 0

    def move_forward(self):
        """
        Move the car forward
        """
        # Example implementation: Increase speed by a fixed amount
        self.speed += 5

    def distance_to(self, other_car):
        """
        Calculate distance to another car
        :param other_car: Another car object
        :return: Distance between this car and the other car
        """
        # Euclidean distance between cars in 2D space
        return ((self.lane - other_car.lane) ** 2 + (self.speed - other_car.speed) ** 2) ** 0.5


class Intersection:
    """
    The intersection of the car objects where they need to move straight, left
    or right

    ==== Attributes ===
    signal: Signal for movement or stoppage returned to other cars on that
    intersection
    message: Queue of Message being received from other cars for movement
    lanes: The lanes of the intersection
    area:   Set of coordinates that is assigned as the area of this intersection
    """
    def __init__(self, message):
        self.signal = None
        self.message = Queue(message)
        self.cars = []

    def add_car(self, car):
        """
        When a new car enters the area of the intersection
        :param car:
        :return:
        """
        self.cars.append(car)

    def optimize_routes(self):
        """
        Optimize routes of cars to avoid collision
        :return:
        """
def optimize_routes(self):
    """
    Calculate the best route for the cars to go so that no collsion happen
    :param self:
    :return:
    """
    # Estimate speeds and adjust lanes to avoid collisions
    for i, car1 in enumerate(self.cars):
        for j, car2 in enumerate(self.cars):
            if i != j:  # Avoid comparing a car with itself
                if car1.detect_collision(car2):
                    # Collision detected, adjust speeds and lanes
                    if car1.speed > car2.speed:
                        car1.speed = car2.speed
                    else:
                        car2.speed = car1.speed

                    # Assume lane change command from intersection
                    car1.change_lane("Left")
                    car2.change_lane("Middle")

    # Additional logic for handling different directions
    for car in self.cars:
        if car.destination == "Downtown":
            # Logic for cars going downtown
            # Adjust speeds, lanes, etc.
            pass
        elif car.destination == "Suburb":
            # Logic for cars going to the suburb
            # Adjust speeds, lanes, etc.
            pass

    # Handle cars approaching from different directions
    for car in self.cars:
        if car.lane == "Left":
            # Logic for cars turning left
            # Yield to oncoming traffic, adjust speeds, etc.
            pass
        elif car.lane == "Right":
            # Logic for cars turning right
            # Yield to pedestrians, adjust speeds, etc.
            pass
        elif car.lane == "Middle":
            # Logic for cars going straight
            # Maintain speed, avoid collisions, etc.
            pass

class Lane:
    """
    The lane on the road that contains all the cars.

    === Attributes ==
    direction: The direction of the lane {N,W,E,S}

    """



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("hello")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
