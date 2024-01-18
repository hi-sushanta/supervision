import pytest

from supervision.geometry.core import Point, Vector


@pytest.mark.parametrize(
    "vector, point, expected_result",
    [
        (Vector(start=Point(x=0, y=0), end=Point(x=5, y=5)), Point(x=-1, y=1), 10.0),
        (Vector(start=Point(x=0, y=0), end=Point(x=5, y=5)), Point(x=6, y=6), 0.0),
        (Vector(start=Point(x=0, y=0), end=Point(x=5, y=5)), Point(x=3, y=6), 15.0),
        (Vector(start=Point(x=5, y=5), end=Point(x=0, y=0)), Point(x=-1, y=1), -10.0),
        (Vector(start=Point(x=5, y=5), end=Point(x=0, y=0)), Point(x=6, y=6), 0.0),
        (Vector(start=Point(x=5, y=5), end=Point(x=0, y=0)), Point(x=3, y=6), -15.0),
        (Vector(start=Point(x=0, y=0), end=Point(x=1, y=0)), Point(x=0, y=0), 0.0),
        (Vector(start=Point(x=0, y=0), end=Point(x=1, y=0)), Point(x=0, y=-1), -1.0),
        (Vector(start=Point(x=0, y=0), end=Point(x=1, y=0)), Point(x=0, y=1), 1.0),
        (Vector(start=Point(x=1, y=0), end=Point(x=0, y=0)), Point(x=0, y=0), 0.0),
        (Vector(start=Point(x=1, y=0), end=Point(x=0, y=0)), Point(x=0, y=-1), 1.0),
        (Vector(start=Point(x=1, y=0), end=Point(x=0, y=0)), Point(x=0, y=1), -1.0),
        (Vector(start=Point(x=1, y=1), end=Point(x=1, y=3)), Point(x=0, y=0), 0.0),
        (Vector(start=Point(x=1, y=1), end=Point(x=1, y=3)), Point(x=1, y=4), -2.0),
        (Vector(start=Point(x=1, y=1), end=Point(x=1, y=3)), Point(x=2, y=4), -4.0),
        (Vector(start=Point(x=1, y=3), end=Point(x=1, y=1)), Point(x=0, y=0), 0.0),
        (Vector(start=Point(x=1, y=3), end=Point(x=1, y=1)), Point(x=1, y=4), 2.0),
        (Vector(start=Point(x=1, y=3), end=Point(x=1, y=1)), Point(x=2, y=4), 4.0),
    ],
)
def test_vector_cross_product(
    vector: Vector,
    point: Point,
    expected_result: float
) -> None:
    result = vector.cross_product(point=point)
    assert result == expected_result
