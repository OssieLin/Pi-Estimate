# Given
import random

def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance_to_center = x**2 + y**2
        if distance_to_center <= 1:
            num_point_circle += 1
        num_point_total += 1
    return 4 * num_point_circle / num_point_total

print(estimate_pi(100))