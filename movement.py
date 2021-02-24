# Wagon Movement API - Software interface with hardware
#
# Once we've figured out where the wagon needs to be, this
# will be the interface we use to get the wagon moving in
# in the right direction.
#
# No logistic calculations should go here, this is for
# interfacing with hardware after the calculation has
# been made.
#

def set_steering_angle(angle):
    """Sends signal to set the steering angle of the front wheels of the wagon.

    Args:
        angle: The angle to turn the wheels from neutral (-45 through 45).

    """
    pass

# Potentially send higher speed if the person is further away,
# for now a default value can be sent for going foreward and backward?
def set_wagon_speed(speed):
    """ Sends signal to drive motor and set the wagon in motion.

    Args:
      speed: A value representing the speed to drive the wagon at.

    """
    pass 
