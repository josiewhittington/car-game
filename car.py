from math import cos, dist, radians, sin


class Car:
    """ A ckass with functions that represent turning and driving a car
    
    Attributes:
        x (float): x-coordinate of car
        y (float): y-coordinate of car
        heading (float): where the car is going in degrees
    """
    def __init__(self, x = 0.0, y = 0.0, heading = 0.0):
        self.x = x
        self.y = y
        self.heading = heading
        
    def turn(self, degrees):
        """ Determines how many degrees a car turns
        
        Args: 
            degrees (float): how many degrees the car will turn
        """
        self.degrees = degrees
        self.heading = (self.degrees + self.heading)%360
      
    def drive(self, distance):
        """ Determines the distance and direction of a car
        
        Args:
            distance (float): distance the car goes 
        """
        d = distance
        h = radians(self.heading)
        self.x += d*sin(h)
        self.y -= d*cos(h)
        
        
def sanity_check():
    c = Car()
    c.turn(90.0)
    c.drive(10.0)
    c.turn(30.0)
    c.drive(20.0)
    print(f'Location: {c.x}, {c.y}\nHeading: {c.heading}')
    return c
    
    
if __name__ == "__main__":
    sanity_check()         