import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Cylindrical Spiral")

# Colors
BACKGROUND = (10, 10, 20)
TURQUOISE = (64, 224, 208)
PINK = (255, 105, 180)
PURPLE = (147, 112, 219)

# Spiral parameters
num_coils = 8
points_per_coil = 100
total_points = num_coils * points_per_coil
radius = 80
cylinder_radius = 150
length = 800
center_x = WIDTH // 2
center_y = HEIGHT // 2

# Generate spiral points
def generate_spiral_points():
    points = []
    for i in range(total_points):
        t = i / total_points
        angle = 2 * math.pi * num_coils * t
        x = center_x - length/2 + t * length
        y = center_y + radius * math.cos(angle)
        z = radius * math.sin(angle)
        points.append((x, y, z))
    return points

# Generate cylinder points
def generate_cylinder_points():
    points = []
    for i in range(total_points):
