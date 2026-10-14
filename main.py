from advanced_visualization import visualize_divide_and_conquer
from visualization import visualize_points
import random
import time
import math


# Generate random points
def generate_points(n):
    return [
        (random.randint(0, 1000), random.randint(0, 1000))
        for _ in range(n)
    ]



# Calculate Euclidean distance
def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])



# Brute Force Algorithm
def brute_force(points):
    n = len(points)

    if n < 2:
        return None, None, float("inf")

    min_dist = float("inf")
    best_pair = None

    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])

            if d < min_dist:
                min_dist = d
                best_pair = (points[i], points[j])

    return best_pair[0], best_pair[1], min_dist

# Divide and Conquer Algorithm
def divide_and_conquer(points):

    if len(points) < 2:
        return None, None, float("inf")

    # Sort points by x-coordinate
    px = sorted(points, key=lambda p: (p[0], p[1]))

    # Sort points by y-coordinate
    py = sorted(points, key=lambda p: (p[1], p[0]))

    def closest(px, py):

        n = len(px)

        # Base case: use Brute Force for small groups
        if n <= 3:
            return brute_force(px)

        mid = n // 2
        midpoint = px[mid][0]

        left_x = px[:mid]
        right_x = px[mid:]

        # Keep track of points in the left half
        left_counts = {}

        for p in left_x:
            left_counts[p] = left_counts.get(p, 0) + 1

        left_y = []
        right_y = []

        # Preserve duplicate points correctly
        for p in py:
            if left_counts.get(p, 0) > 0:
                left_y.append(p)
                left_counts[p] -= 1
            else:
                right_y.append(p)

        p1, q1, d1 = closest(left_x, left_y)
        p2, q2, d2 = closest(right_x, right_y)

        if d1 <= d2:
            best = (p1, q1, d1)
        else:
            best = (p2, q2, d2)

        best_dist = best[2]

        # Points close to the dividing line
        strip = [
            p for p in py
            if abs(p[0] - midpoint) < best_dist
        ]

        # Check nearby points in y-coordinate order
        for i in range(len(strip)):
            j = i + 1

            while (
                j < len(strip)
                and strip[j][1] - strip[i][1] < best_dist
            ):
                d = distance(strip[i], strip[j])

                if d < best_dist:
                    best = (strip[i], strip[j], d)
                    best_dist = d

                j += 1

        return best

    return closest(px, py)


# Main Program
if __name__ == "__main__":

    n = int(input("Enter the number of points: "))

    points = generate_points(n)

    print("\nGenerated Points:")
    for p in points:
        print(p)

    # Brute Force
    start = time.perf_counter()
    b1, b2, d1 = brute_force(points)
    brute_time = (time.perf_counter() - start) * 1000

    # Divide and Conquer
    start = time.perf_counter()
    p1, p2, d2 = divide_and_conquer(points)
    divide_time = (time.perf_counter() - start) * 1000

    if n < 2:
        print("\nAt least two points are required.")
    else:
        print("\nBrute Force:")
        print(f"Minimum Distance: {d1:.6f}")
        print(f"Closest Pair: {b1} and {b2}")

        print("\nDivide and Conquer:")
        print(f"Minimum Distance: {d2:.6f}")
        print(f"Closest Pair: {p1} and {p2}")

        print("\nExecution Time:")
        print(f"Brute Force: {brute_time:.6f} ms")
        print(f"Divide and Conquer: {divide_time:.6f} ms")

        if math.isclose(d1, d2, rel_tol=1e-12, abs_tol=1e-12):
            print("\nVerification: Both algorithms agree!")
        else:
            print("\nVerification: Results do not match!")

        if n >= 2:
            visualize_points(
                points,
                (b1, b2),
                (p1, p2)
            )
            visualize_divide_and_conquer(points)