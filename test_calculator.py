import pytest


@pytest.mark.parametrize("number, expected",
                         [
                             (70, "Normal"),
                             (50, "Borderline Low"),
                             (20, "Low")
                         ]
                         )
def test_check_hdl_range(number, expected):
    from calculator import check_hdl_range

    result = check_hdl_range(number)
    assert (result == expected)
