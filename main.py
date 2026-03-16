
from math import sqrt, isclose


def radius_sum(r1, r2):
    """Vrátí součet poloměrů."""
    return r1 + r2


def euclid_distance(x1, y1, x2, y2):
    """Vrátí Euklidovskou vzdálenost mezi dvěma body."""
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def has_intersection(circle_1, circle_2):
    """Zjistí, jestli se kružnice protínají a kolik mají průniků."""

    x1, y1, r1 = circle_1["x"], circle_1["y"], circle_1["r"]
    x2, y2, r2 = circle_2["x"], circle_2["y"], circle_2["r"]

    d = euclid_distance(x1, y1, x2, y2)
    r_sum = radius_sum(r1, r2)
    r_diff = abs(r1 - r2)

    if d > r_sum:
        return {"is_intersection": False, "intersections_count": 0}

    elif isclose(d, r_sum):
        return {"is_intersection": True, "intersections_count": 1}

    elif r_diff < d < r_sum:
        return {"is_intersection": True, "intersections_count": 2}

    elif isclose(d, r_diff):
        return {"is_intersection": True, "intersections_count": 1}

    else:
        return {"is_intersection": False, "intersections_count": 0}


from circle_stats import has_intersection
from circles_intersection_draw import draw_data


circle_1 = {"x": 0, "y": 0, "r": 2}
circle_2 = {"x": 3, "y": 0, "r": 1}


result = has_intersection(circle_1, circle_2)

if result["is_intersection"]:
    print(f"Kružnice se protínají a mají {result['intersections_count']} průniky.")
else:
    print("Kružnice se neprotínají.")


draw_data(circle_1, circle_2)

from circle_stats import has_intersection

circle_1 = {"x": 0, "y": 0, "r": 2}
circle_2 = {"x": 3, "y": 0, "r": 1}

result = has_intersection(circle_1, circle_2)

print(result)