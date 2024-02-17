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
