import math

x_coords = (3, 2, 3)
y_coords = (8, 6, 4)

distances = []

for i in range(len(x_coords)):
    for j in range(i + 1, len(x_coords)):
        dist = math.sqrt((x_coords[j] - x_coords[i])**2 + (y_coords[j] - y_coords[i])**2)
        distances.append(dist)

print(distances)
