import random
import matplotlib.pyplot as plt

def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    circle_points_x = []
    circle_points_y = []
    square_points_x = []
    square_points_y = []

    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance_to_center = x ** 2 + y ** 2
        if distance_to_center <= 1:
            num_point_circle += 1
            circle_points_x.append(x)
            circle_points_y.append(y)
        else:
            square_points_x.append(x)
            square_points_y.append(y)
        num_point_total += 1

    pi_estimate = 4 * num_point_circle / num_point_total
    return pi_estimate, circle_points_x, circle_points_y, square_points_x, square_points_y

# Example usage
n = 1000
pi_estimate, circle_points_x, circle_points_y, square_points_x, square_points_y = estimate_pi(n)

# Plotting
plt.figure(figsize=(6, 6))
plt.scatter(square_points_x, square_points_y, color='blue', s=5, label='Outside Circle')
plt.scatter(circle_points_x, circle_points_y, color='red', s=5, label='Inside Circle')
plt.axis('equal')
plt.legend()
plt.title(f'Estimating Pi with {n} points, Estimated Pi = {pi_estimate:.5f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()