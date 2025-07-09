import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.interpolate import interp1d

# Sample IR sensor data (distance in cm)
distance_data = [
    198.00, 198.00, 7.00, 198.00, 7.00, 198.00, 198.00, 198.00, 198.00,
    198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00,
    198.00, 198.00, 199.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00,
    198.00, 198.00, 198.00, 198.00, 199.00, 198.00, 198.00, 7.00, 198.00,
    199.00, 7.00, 7.00, 7.00, 198.00, 199.00, 198.00, 198.00, 198.00, 198.00,
    198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00,
    198.00, 198.00, 198.00, 198.00, 198.00, 7.00, 198.00, 198.00, 7.00, 198.00,
    198.00, 199.00, 7.00, 7.00, 198.00, 198.00, 7.00, 198.00, 198.00, 7.00,
    198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00,
    198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00,
    198.00, 198.00, 198.00, 7.00, 7.00, 7.00, 198.00, 198.00, 7.00, 7.00,
    7.00, 7.00, 7.00, 7.00, 7.00, 7.00, 198.00, 7.00, 7.00, 7.00, 7.00,
    7.00, 7.00, 7.00, 7.00, 7.00, 198.00, 198.00, 7.00, 7.00, 198.00, 198.00,
    198.00, 198.00, 7.00, 7.00, 7.00, 198.00, 198.00, 198.00, 7.00, 7.00,
    7.00, 7.00, 198.00, 7.00, 7.00, 7.00, 7.00, 198.00, 7.00, 7.00, 7.00,
    198.00, 198.00, 7.00, 7.00, 7.00, 198.00, 7.00, 7.00, 7.00, 7.00, 198.00,
    8.00, 7.00, 198.00, 198.00, 7.00, 7.00, 7.00, 198.00, 7.00, 7.00, 7.00,
    7.00, 198.00, 7.00, 7.00, 7.00, 198.00, 7.00, 7.00, 7.00, 7.00, 198.00,
    8.00, 7.00, 8.00, 7.00, 7.00, 8.00, 198.00, 7.00, 7.00, 198.00, 199.00,
    199.00, 199.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00,
    199.00, 198.00, 198.00, 7.00, 198.00, 198.00, 199.00, 7.00, 7.00, 198.00,
    198.00, 7.00, 7.00, 7.00, 7.00, 198.00, 199.00, 198.00, 199.00, 7.00,
    7.00, 7.00, 198.00, 198.00, 7.00, 7.00, 7.00, 198.00, 198.00, 198.00, 7.00,
    7.00, 198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 7.00, 198.00, 7.00,
    198.00, 198.00, 198.00, 198.00, 198.00, 198.00, 7.00
]

# Create x, y coordinates based on the index (or any logic you need)
x = np.arange(len(distance_data))
y = np.sin(x / 10) * 10  # Just an example to generate some variation in y

# Interpolation to fill gaps (e.g., for outliers like 7.00 cm)
# Replace values like 7.00 with NaN and interpolate missing values
distance_data_interpolated = np.array(distance_data, dtype=float)
distance_data_interpolated[distance_data_interpolated == 7.00] = np.nan

# Interpolate the missing data using linear interpolation
interp_func = interp1d(x[~np.isnan(distance_data_interpolated)], distance_data_interpolated[~np.isnan(distance_data_interpolated)], kind='linear', fill_value='extrapolate')
distance_data_filled = interp_func(x)

# Apply smoothing to the interpolated distance data
smoothed_distance = gaussian_filter1d(distance_data_filled, sigma=3)

# Create the 3D plot
fig = plt.figure(figsize=(12, 6))

# 3D plot
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(x, y, smoothed_distance, c=smoothed_distance, cmap='viridis')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Distance (cm)')
ax1.set_title('3D IR Sensor Distance Data (Smoothed and Interpolated)')

# 2D plot
ax2 = fig.add_subplot(122)
ax2.plot(x, smoothed_distance, label='Smoothed Distance', color='b')
ax2.set_xlabel('Index')
ax2.set_ylabel('Distance (cm)')
ax2.set_title('2D IR Sensor Distance Data (Smoothed)')
ax2.grid(True)

# Show the plots
plt.tight_layout()
plt.show()
