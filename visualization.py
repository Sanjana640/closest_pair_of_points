import matplotlib.pyplot as plt


def visualize_points(points, brute_pair, divide_pair):

    fig, ax = plt.subplots(figsize=(11, 7))

    # Plot all points
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    ax.scatter(x, y, color="blue", s=50, label="All Points")

    # Label each point
    for i, point in enumerate(points):
        ax.annotate(
            f"P{i + 1}",
            point,
            xytext=(5, 5),
            textcoords="offset points"
        )

    # Closest pair from Brute Force
    if brute_pair:
        p1, p2 = brute_pair

        ax.plot(
            [p1[0], p2[0]],
            [p1[1], p2[1]],
            color="red",
            linewidth=2,
            label="Brute Force Closest Pair"
        )

    # Closest pair from Divide and Conquer
    if divide_pair:
        p1, p2 = divide_pair

        ax.plot(
            [p1[0], p2[0]],
            [p1[1], p2[1]],
            color="green",
            linestyle="--",
            linewidth=2,
            label="Divide and Conquer Closest Pair"
        )

        # Calculate the dividing line
        sorted_x = sorted(p[0] for p in points)
        middle_x = sorted_x[len(sorted_x) // 2]

        # Calculate the minimum distance
        distance = (
            (p1[0] - p2[0]) ** 2
            + (p1[1] - p2[1]) ** 2
        ) ** 0.5

        # Draw the dividing line
        ax.axvline(
            x=middle_x,
            color="purple",
            linestyle=":",
            linewidth=2,
            label="Dividing Line"
        )

        # Shade the strip region
        ax.axvspan(
            middle_x - distance,
            middle_x + distance,
            color="yellow",
            alpha=0.2,
            label="Strip Region (width 2d)"
        )

    ax.set_title("Closest Pair of Points Visualization")
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")

    ax.legend(
    loc="upper left",
    bbox_to_anchor=(1.02, 1),
    fontsize=9
    )

    ax.grid(True)

    fig.tight_layout(rect=[0, 0, 0.78, 1])

    plt.show()