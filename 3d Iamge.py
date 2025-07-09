import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting


# Provided distance data (in cm)
distance_data = [
  198, 198, 7, 198, 7, 198, 198, 198, 198, 198, 198, 198,
    198, 198, 198, 198, 198, 198, 198, 198, 199, 198, 198,
    198, 198, 198, 198, 198, 198, 198, 199, 198, 198, 7,
    198, 199, 150, 7, 80, 198, 199, 198, 198, 198, 198, 198,
    198, 198, 198, 198, 198, 198, 198, 198, 198, 198, 198,
    7, 198, 198, 7, 198, 198, 199, 80, 7, 198, 198, 7, 198,
    198, 7, 198, 198, 198, 198, 198, 198, 198, 198, 198,
    198, 198, 198, 198, 198, 198, 198, 198, 198, 7, 7, 7,
    198, 198,7, 198, 7, 198, 198, 80, 7, 198, 198, 198, 198,7,
    198, 198, 198, 7, 198,  7, 198, 198, 7,
    7, 7, 198, 7, 7, 7, 198, 198, 7, 150, 7, 198, 199, 7, 7,
    7, 198, 8, 7, 198, 198, 7,  198, 7, 150, 7, 80, 198,
    7, 70, 170, 198, 80, 7, 150, 80, 198, 8, 7, 8, 7, 120, 8, 198,
    7, 7, 198, 199, 199, 199, 198, 198, 198, 198, 198, 198,
    199, 198, 198, 7, 198, 198, 199, 7, 7, 198, 198, 7, 120,
    7, 7, 198, 199, 198, 199, 7, 7, 7, 150,150,80,150,80,150,198, 198, 80, 150, 7,
    198, 198, 198, 70, 7, 198, 198, 198, 198, 198, 198, 7,
    198, 7, 198, 198, 198, 198, 198, 198, 198, 7

]

# Reshape distance data into a 2D grid (e.g., 15x15 grid)
grid_size = 15
Z = np.array(distance_data[:grid_size**2]).reshape(grid_size, grid_size)

# Create X, Y grid
X, Y = np.meshgrid(range(grid_size), range(grid_size))

# Plot the 3D surface
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='jet', edgecolor='none')

# Add labels and color bar
ax.set_xlabel('X-Axis (Sensor Position)')
ax.set_ylabel('Y-Axis (Sensor Sweep)')
ax.set_zlabel('Z-Axis (Distance in cm)')
ax.set_title('3D Model from IR Sensor Data')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# Show the plot
plt.show()
