import random
import math

from main import brute_force, divide_and_conquer


def run_random_tests():

    total_tests = 1000

    print("Running randomized tests...")

    for test in range(1, total_tests + 1):

        # Generate between 2 and 100 points
        n = random.randint(2, 100)

        points = [
            (
                random.randint(-100, 100),
                random.randint(-100, 100)
            )
            for _ in range(n)
        ]

        # Run both algorithms
        _, _, d1 = brute_force(points)
        _, _, d2 = divide_and_conquer(points)

        # Compare the minimum distances
        if not math.isclose(
            d1, d2,
            rel_tol=1e-12,
            abs_tol=1e-12
        ):
            print(f"\nTest {test} FAILED!")
            print("Points:", points)
            print("Brute Force Distance:", d1)
            print("Divide and Conquer Distance:", d2)
            return

    print(f"\nAll {total_tests} randomized tests passed!")
    print("Both algorithms consistently returned the same minimum distance.")


if __name__ == "__main__":
    run_random_tests()