def bound_to_180(angle):
    # bound the angle to be with 360 degrees
    angle %= 360

    # if the angle > 180, transform into the corresponding negative value
    if angle >= 180:
        angle -= 360

    return angle


def is_angle_between(first_angle, middle_angle, third_angle):
    # bound all angles to 180
    first_angle = bound_to_180(first_angle)
    middle_angle = bound_to_180(middle_angle)
    third_angle = bound_to_180(third_angle)

    isBetween = False

    # determine the larger and smaller of the first and third angles
    # in order to determine if the middle angle lies between
    larger_angle = max(first_angle, third_angle)
    smaller_angle = min(first_angle, third_angle)

    # check if angle is between the two other angles, assuming non-inclusive.
    if smaller_angle < middle_angle and middle_angle < larger_angle:
        isBetween = True

    return isBetween
