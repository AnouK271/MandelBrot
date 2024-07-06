from matplotlib import pyplot as plt
from numpy import zeros


def calculate_orbit_count(c):
    z = 0.0
    count = 0
    while count < 200 and z.real ** 2 + z.imag ** 2 <= 4:
        count += 1
        z = z ** 2 + c
    return count


def generate_orbit_counts():
    resolution = 500
    delta = 3.2 / resolution
    orbit_counts = zeros((resolution, resolution))
    for x in range(resolution):
        for y in range(resolution):
            c = complex(-2.5 + x * delta, 1.6 - y * delta)
            orbit_counts[y, x] = calculate_orbit_count(c)
    return orbit_counts


counts = generate_orbit_counts()
plt.figure(figsize=(6, 6))
plt.imshow(counts, extent=[-2.5, 2.5, -2.5, 2.5], cmap='plasma')
plt.colorbar()
plt.title("Mandelbrot Set Visualization")
plt.show()
