import pytest

@pytest.mark.parametrize("point1, point2, xval, expected_y",
    [
        ((1,1), (2,2), 3, 3),
        ((1,1), (3,2), 2, 1.5),
        ((1,1), (3,2), 4, 2.5),
        ((1,1), (3,2), 0, 0.5),
        ((1,1), (3,2), -2, -0.5),
        ((1,0), (0,3), 2, -3),
        ((1,0), (0,3), 0, 3),
        ((1,0), (-6,0), 4, 0),
    ]
)
def test_yvalue_on_line(point1, point2, xval, expected_y):
    from points_on_line import yvalue_on_line

    result = yvalue_on_line(point1, point2, xval)
    assert (result == expected_y)