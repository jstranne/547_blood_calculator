import pytest


@pytest.mark.parametrize("point1, point2, xval, expected_y",
                         [
                             ((1, 1), (2, 2), 3, 3),
                             ((1, 1), (3, 2), 2, 1.5),
                             ((1, 1), (3, 2), 4, 2.5),
                             ((1, 1), (3, 2), 0, 0.5),
                             ((1, 1), (3, 2), -2, -0.5),
                             ((1, 0), (0, 3), 2, -3),
                             ((1, 0), (0, 3), 0, 3),
                             ((1, 0), (-6, 0), 4, 0),
                             ((1, 0), (1, 10), 4, None),
                             ((0, 0), (-6, -3), -3, -1.5),
                         ]
                         )
def test_yvalue_on_line(point1, point2, xval, expected_y):
    from points_on_line import yvalue_on_line

    result = yvalue_on_line(point1, point2, xval)
    assert (result == expected_y)


@pytest.mark.parametrize("point1, point2, expected",
                         [
                             ((1, 1), (2, 2), -1),
                             ((1, 0), (0, 3), 1),
                             ((1, 0), (-6, 0), 7),
                             ((1, 0), (1, 10), 0),
                         ]
                         )
def test_calc_dx(point1, point2, expected):
    from points_on_line import calc_dx

    result = calc_dx(point1, point2)
    assert (result == expected)


@pytest.mark.parametrize("point1, point2, expected",
                         [
                             ((1, 1), (2, 2), -1),
                             ((1, 0), (0, 3), -3),
                             ((1, 0), (-6, 0), 0),
                             ((1, 0), (1, -5), 5),
                         ]
                         )
def test_calc_dy(point1, point2, expected):
    from points_on_line import calc_dy

    result = calc_dy(point1, point2)
    assert (result == expected)


@pytest.mark.parametrize("point1, point2, expected",
                         [
                             ((1, 1), (2, 2), 1),
                             ((1, 0), (0, 3), -3),
                             ((1, 0), (-6, 0), 0),
                             ((0, 0), (12, 8), 2/3),
                             ((1, 0), (1, 10), None),
                         ]
                         )
def test_calc_slope(point1, point2, expected):
    from points_on_line import calc_slope

    result = calc_slope(point1, point2)
    assert (result == expected)
