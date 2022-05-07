# bouncing ball with pymunk and pygame

#  ____  _  __
# |  _ \| |/ /  Created by Ravindu Kalhara
# | |_) | ' /   Github - https://github.com/Ravindu-Kalhara
# |  _ <| . \
# |_| \_\_|\_\
#

import pygame
import pymunk
import pymunk.pygame_util
from pygame import Color

pygame.init()
WIDTH, HEIGHT = 400, 500 # define the surface width and height
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # create the surface
CLOCK = pygame.time.Clock()
DRAW_OPTIONS = pymunk.pygame_util.DrawOptions(WINDOW) 

SPACE = pymunk.Space() # create the pymunk space
SPACE.gravity = 0, 1000

# create the ball and define it's properties
inertia = pymunk.moment_for_circle(10, 0, 20, (0, 0))
ball_body = pymunk.Body(10, inertia)
ball_body.position = 30, 200
ball_body.velocity = 100, -500

ball = pymunk.Circle(ball_body, 20)
ball.elasticity = 0.95
ball.friction = 0.9
ball.color = Color(255, 0, 0)
SPACE.add(ball_body, ball)

# create the floor and define it's properies
thikness = 5
floor = pymunk.Segment(SPACE.static_body, (0.0, 500 - thikness), (400.0, 500 - thikness), thikness)
floor.elasticity = 0.8
floor.friction = 0.9
floor.color = Color(0, 255, 0)
SPACE.add(floor)

running = True
while running:
    WINDOW.fill(Color(0, 0, 0))
    CLOCK.tick(60) # set the frame rate
    SPACE.debug_draw(DRAW_OPTIONS)
    SPACE.step(1/60)

    for event in pygame.event.get():
        # close the programe if clicked on close button
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
