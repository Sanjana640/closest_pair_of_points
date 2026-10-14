import matplotlib.pyplot as plt
import math


def visualize_divide_and_conquer(points):

    if len(points) < 2:
        print("At least two points are required.")
        return

    px = sorted(points, key=lambda p: (p[0], p[1]))
    py = sorted(points, key=lambda p: (p[1], p[0]))

    def closest(px, py, depth=0):

        n = len(px)

        if n <= 3:
            best = (None, None, float("inf"))

            for i in range(n):
                for j in range(i + 1, n):
                    d = math.dist(px[i], px[j])

                    if d < best[2]:
                        best = (px[i], px[j], d)

            return best

        mid = n // 2
        mid_x = px[mid][0]

        left_x = px[:mid]
        right_x = px[mid:]

        # Keep duplicate coordinates in the correct halves
        counts = {}
        for p in left_x:
            counts[p] = counts.get(p, 0) + 1

        left_y = []
        right_y = []

        for p in py:
            if counts.get(p, 0) > 0:
                left_y.append(p)
                counts[p] -= 1
            else:
                right_y.append(p)

        # Display the current recursive split
        if depth == 0:
            fig, ax = plt.subplots(figsize=(10, 7))

            ax.scatter(
                [p[0] for p in px],
                [p[1] for p in px],
                color="blue",
                label="Points"
            )

            ax.axvline(
                mid_x,
                color="purple",
                linestyle="--",
                label="Dividing Line"
            )

            for i, p in enumerate(px):
                ax.annotate(f"P{i + 1}", p, xytext=(4, 4),
                            textcoords="offset points")

        p1, q1, d1 = closest(left_x, left_y, depth + 1)
        p2, q2, d2 = closest(right_x, right_y, depth + 1)

        best = (p1, q1, d1) if d1 <= d2 else (p2, q2, d2)
        d = best[2]

        strip = [
            p for p in py
            if abs(p[0] - mid_x) < d
        ]

        # Draw the strip at the top-level division
        if depth == 0:
            ax.axvspan(
                mid_x - d,
                mid_x + d,
                color="yellow",
                alpha=0.25,
                label="Strip Region"
            )

        for i in range(len(strip)):
            j = i + 1

            while j < len(strip) and strip[j][1] - strip[i][1] < d:
                dist = math.dist(strip[i], strip[j])

                if dist < d:
                    best = (strip[i], strip[j], dist)
                    d = dist

                j += 1

        return best

    p1, p2, minimum = closest(px, py)

    fig = plt.gcf()
    ax = plt.gca()

    if p1 is not None:
        ax.plot(
            [p1[0], p2[0]],
            [p1[1], p2[1]],
            color="red",
            linewidth=2,
            label=f"Closest Pair (d={minimum:.2f})"
        )

    ax.set_title("Divide and Conquer: Splitting and Strip")
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1))
    ax.grid(True)

    fig.tight_layout()
    plt.show()

    print("Closest Pair:", p1, p2)
    print(f"Minimum Distance: {minimum:.6f}")
if __name__ == "__main__":
    points = [
        (2, 3), (5, 4), (8, 9),
        (4, 7), (6, 5), (10, 2),
        (3, 8), (7, 6)
    ]

    visualize_divide_and_conquer(points)