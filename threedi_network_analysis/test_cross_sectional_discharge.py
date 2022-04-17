from shapely.geometry import LineString, Point

from cross_sectional_discharge import intersected_segments, is_left_of_line

LINE_A = LineString([(5, 5), (6, -5), (7, 5)])
LINE_B = LineString([(0, 0), (10, 0)])
POINT_A = Point(5, 5)
POINT_B = Point(5, -5)
POINT_C = Point(5, 0)


def test_intersected_segments():
    assert([seg.wkt for seg in intersected_segments(LINE_A, LINE_B)]) == ['LINESTRING (5 5, 6 -5)', 'LINESTRING (6 -5, 7 5)']


def test_is_left_of_line():
    assert is_left_of_line(POINT_A, LINE_B)
    assert not is_left_of_line(POINT_B, LINE_B)
    print(is_left_of_line(POINT_C, LINE_B))


if __name__ == "__main__":
    test_intersected_segments()
    test_is_left_of_line()