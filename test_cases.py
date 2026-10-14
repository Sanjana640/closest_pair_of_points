import math

from main import brute_force, divide_and_conquer


test_cases = [
    {
        "name": "Duplicate points",
        "points": [(2, 3), (2, 3), (5, 7), (8, 9)],
        "expected": 0.0
    },
    {
        "name": "Collinear points",
        "points": [(1, 2), (2, 2), (3, 2), (4, 2)],
        "expected": 1.0
    },
    {
        "name": "Same x-coordinate",
        "points": [(3, 1), (3, 5), (3, 2), (3, 8)],
        "expected": 1.0
    },
    {
        "name": "Same y-coordinate",
        "points": [(1, 4), (5, 4), (2, 4), (9, 4)],
        "expected": 1.0
    },
    {
        "name": "Exactly two points",
        "points": [(0, 0), (3, 4)],
        "expected": 5.0
    },
    {
        "name": "Only one point",
        "points": [(5, 5)],
        "expected": None
    },
    {
        "name": "No points",
        "points": [],
        "expected": None
    },
    {
        "name": "Negative coordinates",
        "points": [(-5, -5), (-4, -5), (3, 8)],
        "expected": 1.0
    }
]


for case in test_cases:
    points = case["points"]

    _, _, d1 = brute_force(points)
    _, _, d2 = divide_and_conquer(points)

    expected = case["expected"]

    if expected is None:
        passed = math.isinf(d1) and math.isinf(d2)
    else:
        passed = (
            math.isclose(d1, expected, abs_tol=1e-9)
            and math.isclose(d2, expected, abs_tol=1e-9)
            and math.isclose(d1, d2, abs_tol=1e-9)
        )

    status = "PASS" if passed else "FAIL"

    print(f"{case['name']}: {status}")

    if not passed:
        print(f"  Expected: {expected}")
        print(f"  Brute Force: {d1}")
        print(f"  Divide and Conquer: {d2}")

print("\nTesting completed.")