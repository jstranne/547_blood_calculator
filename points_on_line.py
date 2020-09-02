def calc_slope(point1, point2):
    dx = calc_dx(point1, point2)
    dy = calc_dy(point1, point2)
    if dx == 0:
        return None
    else:
        return dy/dx


def calc_dx(point1, point2):
    return point1[0]-point2[0]


def calc_dy(point1, point2):
    return point1[1]-point2[1]


def yvalue_on_line(point1, point2, xval):
    slope = calc_slope(point1, point2)
    if slope is None:
        print("No slope (vertical line)")
        return None
    return point1[1] + slope * (xval-point1[0])
