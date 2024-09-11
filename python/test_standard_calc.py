from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0


# test for positive angles that remain positive after bounding
def test_bound_positive_angle():
    assert bound_to_180(90) == 90
    assert bound_to_180(1) == 1
    assert bound_to_180(450) == 90
    assert bound_to_180(360) == 0


# test for negative angles that remain negative after bounding
def test_bound_negative_angle():
    assert bound_to_180(-90) == -90
    assert bound_to_180(-1) == -1
    assert bound_to_180(-450) == -90
    assert bound_to_180(-360) == 0


# test for angles that change sign after bounding
def test_bound_crossing_boundary():
    assert bound_to_180(180) == -180
    assert bound_to_180(270) == -90
    assert bound_to_180(-180) == -180
    assert bound_to_180(-270) == 90
    assert bound_to_180(181) == -179
    assert bound_to_180(-181) == 179


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)


def test_between_no_bounding():
    assert is_angle_between(0, 45, 90)
    assert not is_angle_between(45, 90, 270)
    assert not is_angle_between(-10, 100, 10)
    assert is_angle_between(-180, -170, -160)


def test_between_with_bounding():
    assert not is_angle_between(45, 90, 270)
    assert is_angle_between(45, -10, 270)
    assert not is_angle_between(170, -180, -170)
    assert is_angle_between(170, -175, 180)


def test_between_edge_cases():
    assert not is_angle_between(180, 0, -180)
    assert not is_angle_between(-180, 0, 180)
    assert is_angle_between(-180, -178, 179)
    assert not is_angle_between(-178, 179, 180)
