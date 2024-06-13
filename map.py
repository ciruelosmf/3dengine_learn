import numpy as np
import pygame
import sys

# Define the Sphere class
class Sphere:
    def __init__(self, center, radius, color):
        self.center = np.array(center)
        self.radius = radius
        self.color = color

    def intersect(self, ray_origin, ray_direction):
        # Calculate the intersection of the ray with the sphere
        L = self.center - ray_origin
        tca = np.dot(L, ray_direction)
        d2 = np.dot(L, L) - tca * tca
        if d2 > self.radius**2:
            return None
        thc = np.sqrt(self.radius**2 - d2)
        t0 = tca - thc
        t1 = tca + thc
        if t0 > 0 and t1 > 0:
            return min(t0, t1)
        return None

# Initialize the scene with some spheres
objects = [
    Sphere([0, 0, 20], 5, (255, 0, 0)),
    Sphere([5, -1, 15], 2, (0, 255, 0)),
    Sphere([-5, 0, 25], 3, (0, 0, 255))
]

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Raycaster')

# Render function
def render():
    aspect_ratio = width / height
    fov = np.pi / 12  # Field of view

    for y in range(height):
        for x in range(width):
            # Normalize screen coordinates
            px = (2 * (x + 0.5) / width - 1) * np.tan(fov / 2) * aspect_ratio
            py = (1 - 2 * (y + 0.5) / height) * np.tan(fov / 2)
            ray_direction = np.array([px, py, -1]).astype(np.float32)
            ray_direction /= np.linalg.norm(ray_direction)  # Normalize the direction

            color = (0, 0, 0)
            min_distance = np.inf
            for obj in objects:
                distance = obj.intersect(np.array([0, 0, 0]), ray_direction)
                if distance and distance < min_distance:
                    min_distance = distance
                    color = obj.color
            screen.set_at((x, y), color)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    render()
    pygame.display.flip()
