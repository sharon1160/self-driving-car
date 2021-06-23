import pygame
import random

pygame.init()
window = pygame.display.set_mode((890, 590))
track = pygame.image.load('nuevo.png')
car = pygame.image.load('tesla.png')
car2 = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
car2 = pygame.transform.scale(car2, (30, 60))

velocity = random.randint(6, 10)
car_x = 180
car_y = 180
cam_x_offset = 0
cam_y_offset = 0

velocity2 = random.randint(1, 3)
car2_x = 180
car2_y = 250
cam2_x_offset = 0
cam2_y_offset = 0

focal_dist = 25
direction = 'up'
direction2 = 'up'
drive = True
clock = pygame.time.Clock()

print(velocity)
print(velocity2)
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)

    # ------------------------- CAR #1 ---------------------------

    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15
    up_px = window.get_at((cam_x, cam_y - focal_dist))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dist))[0]
    right_px = window.get_at((cam_x + focal_dist, cam_y))[0]
    left_px = window.get_at((cam_x - focal_dist, cam_y))[0]

    # show the direction
    #print(direction)

    # change direction (take turn)
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and down_px == 255 and (right_px != 255 and right_px != 254):
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'left' and left_px != 255 and left_px != 254 and up_px == 255 and down_px != 255:
        direction = 'up'
        car = pygame.transform.rotate(car, -90)
    elif direction == 'left' and left_px != 255 and left_px != 254 and (down_px == 255 or down_px == 219):
        direction = 'down'
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, 90)
    elif direction == 'down' and down_px != 255 and down_px != 219 and down_px != 223 and (right_px == 255 or right_px == 254):
        direction = 'right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'down' and down_px != 255 and down_px != 183 and (left_px == 255 or left_px == 254):
        direction = 'left'
        car_y = car_y + 30
        cam_x_offset = 0
        cam_y_offset = 0
        car = pygame.transform.rotate(car, -90)

    # drive
    if direction == 'up' and up_px == 255:
        car_y = car_y - velocity
    elif direction == 'right' and (right_px == 255 or right_px == 254):
        car_x = car_x + velocity
    elif direction == 'left' and (left_px == 255 or left_px == 254):
        car_x = car_x - velocity
    elif direction == 'down' and (down_px == 255 or down_px == 219):
        car_y = car_y + velocity

    # ------------------------- CAR #2 ---------------------------

    cam2_x = car2_x + cam2_x_offset + 15
    cam2_y = car2_y + cam2_y_offset + 15
    up2_px = window.get_at((cam2_x, cam2_y - focal_dist))[0]
    down2_px = window.get_at((cam2_x, cam2_y + focal_dist))[0]
    right2_px = window.get_at((cam2_x + focal_dist, cam2_y))[0]
    left2_px = window.get_at((cam2_x - focal_dist, cam2_y))[0]

    # show the direction
    print(direction2)
    print(down2_px, right2_px)

    # change direction (take turn)
    if direction2 == 'up' and up2_px != 255 and right2_px == 255:
        direction2 = 'right'
        cam2_x_offset = 30
        car2 = pygame.transform.rotate(car2, -90)
    elif direction2 == 'right' and down2_px == 255 and (right2_px != 255 and right2_px != 254):
        direction2 = 'down'
        car2_x = car2_x + 30
        cam2_x_offset = 0
        cam2_y_offset = 30
        car2 = pygame.transform.rotate(car2, -90)
    elif direction2 == 'left' and left2_px != 255 and left2_px != 254 and up2_px == 255 and down2_px != 255:
        direction2 = 'up'
        car2 = pygame.transform.rotate(car2, -90)
    elif direction2 == 'left' and left2_px != 255 and left2_px != 254 and (down2_px == 255 or down2_px == 219):
        direction2 = 'down'
        cam2_x_offset = 0
        cam2_y_offset = 30
        car2 = pygame.transform.rotate(car2, 90)
    elif direction2 == 'down' and down2_px != 255 and down2_px != 219 and down2_px != 223 and (right2_px == 255 or right2_px == 254):
        direction2 = 'right'
        car2_y = car2_y + 30
        cam2_x_offset = 30
        cam2_y_offset = 0
        car2 = pygame.transform.rotate(car2, 90)
    elif direction2 == 'down' and down2_px != 255 and down2_px != 183 and (left2_px == 255 or left2_px == 254):
        direction2 = 'left'
        car2_y = car2_y + 30
        cam2_x_offset = 0
        cam2_y_offset = 0
        car2 = pygame.transform.rotate(car2, -90)

    # drive
    if direction2 == 'up' and up2_px == 255:
        car2_y = car2_y - velocity2
    elif direction2 == 'right' and (right2_px == 255 or right2_px == 254):
        car2_x = car2_x + velocity2
    elif direction2 == 'left' and (left2_px == 255 or left2_px == 254):
        car2_x = car2_x - velocity2
    elif direction2 == 'down' and (down2_px == 255 or down2_px == 219):
        car2_y = car2_y + velocity2

    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    window.blit(car2, (car2_x, car2_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.draw.circle(window, (0, 255, 0), (cam2_x, cam2_y), 5, 5)
    pygame.display.update()
