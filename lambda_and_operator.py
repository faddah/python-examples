"""Performance benchmark comparing lambda vs operator module for sorting.

Measures the speed difference between using inline lambda functions and the
operator module's itemgetter/attrgetter for sort keys, across two scenarios:

1. Sorting a list of tuples by second element — lambda vs operator.itemgetter
2. Sorting a list of dataclass instances by attribute — lambda vs operator.attrgetter

Each benchmark sorts 1,000,000 items repeated 10 times using timeit.
"""

import timeit
import operator
from dataclasses import dataclass

data = [(i, i * 2) for i in range(1_000_000)]

t = timeit.timeit(lambda: sorted(
    data,
    key=lambda x: x[1]),
    number=10)

print(f"Lambda: {t:.4f} seconds")

t2 = timeit.timeit(lambda: sorted(
    data,
    key=operator.itemgetter(1)),
    number=10)

print(f"Lambda w/ operator.itemgetter[1]: {t2:.4f} seconds")


@dataclass
class Point:
    """A 2D point with integer coordinates, used to benchmark attribute-based sorting.

    Attributes:
        x: The horizontal coordinate.
        y: The vertical coordinate.
    """
    x: int
    y: int

points = [Point(i, i * 2) for i in range(1_000_000)]

t3 = timeit.timeit(lambda: sorted(
    points,
    key=lambda p: p.y),
    number=10)

print(f"Class Lambda: {t3:.4f} seconds")

t4 = timeit.timeit(lambda: sorted(
    points,
    key=operator.attrgetter("y")),
    number=10)

print(f"Class Lambda w/ operator.attrgetter('y'): {t4:.4f} seconds")
