import numpy as np
import matplotlib.pyplot as plt

# Generate data for the sine wave
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a figure and plot the sine wave
plt.figure()
plt.plot(x, y)

# Save the figure as a PNG file
plt.savefig("sine_wave.png")