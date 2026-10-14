# Closest Pair of Points

## Project Overview

This project compares two algorithms for finding the closest pair
of points in a two-dimensional plane.

1. Brute Force Algorithm
2. Divide and Conquer Algorithm

## Features

- Generates random points.
- Finds the closest pair using both algorithms.
- Displays the minimum distance and closest points.
- Visualizes the closest pair using Matplotlib.
- Shows the dividing line and strip region.
- Compares algorithm execution times.
- Tests corner cases and randomized inputs.

## Technologies Used

- Python
- Matplotlib

## Time Complexity

| Algorithm | Time Complexity |
|---|---|
| Brute Force | O(N^2) |
| Divide and Conquer | O(N log N) |

## Installation

Install Python 3, then install the required library:

    pip install -r requirements.txt

## How to Run

Run the main program:

    python main.py

Run performance analysis:

    python performance.py

Run corner-case tests:

    python test_cases.py

Run randomized tests:

    python random_test.py

## Testing

The project includes eight corner-case tests and
1,000 randomized tests.

Both algorithms agreed on the minimum distance
for the tested inputs.