import time
import random
import matplotlib.pyplot as plt

from main import brute_force, divide_and_conquer, generate_points


def measure_performance():

    sizes = [100, 500, 1000, 2000, 5000, 10000]

    brute_times = []
    divide_times = []

    print("\nPERFORMANCE ANALYSIS")
    print("-" * 65)
    print(f"{'Points':<12}{'Brute Force (ms)':<22}"
          f"{'Divide & Conquer (ms)':<25}")
    print("-" * 65)

    for n in sizes:

        points = generate_points(n)

        # Measure Brute Force
        start = time.perf_counter()
        _, _, d1 = brute_force(points)
        brute_time = (time.perf_counter() - start) * 1000

        # Measure Divide and Conquer
        start = time.perf_counter()
        _, _, d2 = divide_and_conquer(points)
        divide_time = (time.perf_counter() - start) * 1000

        brute_times.append(brute_time)
        divide_times.append(divide_time)

        print(f"{n:<12}{brute_time:<22.3f}{divide_time:<25.3f}")

        # Verify correctness
        if abs(d1 - d2) > 1e-9:
            print(f"ERROR: Results differ for N = {n}!")
            return

    print("-" * 65)
    print("Verification: Both algorithms agree for every tested size!")

    # Plot performance graph
    plt.figure(figsize=(10, 6))

    plt.plot(
        sizes, brute_times,
        marker="o",
        label="Brute Force"
    )

    plt.plot(
        sizes, divide_times,
        marker="s",
        label="Divide and Conquer"
    )

    plt.title("Performance Comparison of Closest Pair Algorithms")
    plt.xlabel("Number of Points (N)")
    plt.ylabel("Execution Time (milliseconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    measure_performance()