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
        t = i / total_points
        angle = 2 * math.pi * num_coils * t
        x = center_x - length/2 + t * length
        y = center_y + cylinder_radius * math.cos(angle)
        z = cylinder_radius * math.sin(angle)
        points.append((x, y, z))
    return points

spiral_points = generate_spiral_points()
cylinder_points = generate_cylinder_points()

# Main loop
clock = pygame.time.Clock()
angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Clear screen
    screen.fill(BACKGROUND)
    
    # Update rotation angle
    angle += 0.01
    
    # Draw the cylindrical outline with gradient
    for i in range(total_points - 1):
        t = i / total_points
        color = (
            int(TURQUOISE[0] * (1-t) + PINK[0] * t),
            int(TURQUOISE[1] * (1-t) + PINK[1] * t),
            int(TURQUOISE[2] * (1-t) + PINK[2] * t)
        )
        
        # Apply 3D rotation
        x1, y1, z1 = cylinder_points[i]
        x2, y2, z2 = cylinder_points[i+1]
        
        # Rotate around Y axis
        rotated_y1 = (y1 - center_y) * math.cos(angle) - z1 * math.sin(angle) + center_y
        rotated_z1 = (y1 - center_y) * math.sin(angle) + z1 * math.cos(angle)
        
        rotated_y2 = (y2 - center_y) * math.cos(angle) - z2 * math.sin(angle) + center_y
        rotated_z2 = (y2 - center_y) * math.sin(angle) + z2 * math.cos(angle)
        
        # Perspective projection
        scale1 = 500 / (500 + rotated_z1)
        scale2 = 500 / (500 + rotated_z2)
        
        proj_x1 = center_x + (x1 - center_x) * scale1
        proj_y1 = center_y + (rotated_y1 - center_y) * scale1
        
        proj_x2 = center_x + (x2 - center_x) * scale2
        proj_y2 = center_y + (rotated_y2 - center_y) * scale2
        
        # Draw cylinder outline
        pygame.draw.line(screen, color, (proj_x1, proj_y1), (proj_x2, proj_y2), 2)
    
    # Draw the spiral with gradient
    for i in range(total_points - 1):
        t = i / total_points
        color = (
            int(TURQUOISE[0] * (1-t) + PURPLE[0] * t),
            int(TURQUOISE[1] * (1-t) + PURPLE[1] * t),
            int(TURQUOISE[2] * (1-t) + PURPLE[2] * t)
        )
        
        # Apply 3D rotation
        x1, y1, z1 = spiral_points[i]
        x2, y2, z2 = spiral_points[i+1]
        
        # Rotate around Y axis
        rotated_y1 = (y1 - center_y) * math.cos(angle) - z1 * math.sin(angle) + center_y
        rotated_z1 = (y1 - center_y) * math.sin(angle) + z1 * math.cos(angle)
        
        rotated_y2 = (y2 - center_y) * math.cos(angle) - z2 * math.sin(angle) + center_y
        rotated_z2 = (y2 - center_y) * math.sin(angle) + z2 * math.cos(angle)
        
        # Perspective projection
        scale1 = 500 / (500 + rotated_z1)
        scale2 = 500 / (500 + rotated_z2)
        
        proj_x1 = center_x + (x1 - center_x) * scale1
        proj_y1 = center_y + (rotated_y1 - center_y) * scale1
        
        proj_x2 = center_x + (x2 - center_x) * scale2
        proj_y2 = center_y + (rotated_y2 - center_y) * scale2
        
        # Draw spiral
        pygame.draw.line(screen, color, (proj_x1, proj_y1), (proj_x2, proj_y2), 4)
    
    # Add some glowing particles for effect
    for i in range(20):
        t = (pygame.time.get_ticks() / 1000 + i/5) % 1
        particle_x = center_x - length/2 + t * length
        particle_angle = 2 * math.pi * num_coils * t + angle
        particle_y = center_y + radius * math.cos(particle_angle)
        particle_z = radius * math.sin(particle_angle)
        
        # Rotate and project
        rotated_y = (particle_y - center_y) * math.cos(angle) - particle_z * math.sin(angle) + center_y
        rotated_z = (particle_y - center_y) * math.sin(angle) + particle_z * math.cos(angle)
        
        scale = 500 / (500 + rotated_z)
        proj_x = center_x + (particle_x - center_x) * scale
        proj_y = center_y + (rotated_y - center_y) * scale
        
        # Draw glowing particle
        glow_size = 5 + 2 * math.sin(pygame.time.get_ticks() / 200 + i)
        pygame.draw.circle(screen, (255, 255, 255), (int(proj_x), int(proj_y)), int(glow_size))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
