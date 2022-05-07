# Balls and Walls with pymunk and pygame

#  ____  _  __
# |  _ \| |/ /  Created by Ravindu Kalhara
# | |_) | ' /   Github - https://github.com/Ravindu-Kalhara
# |  _ <| . \
# |_| \_\_|\_\
#

import pygame
from pygame import Color
import pymunk
import pymunk.pygame_util as pgutil
from random import randint

def main():
    pygame.init()
    WIDTH, HEIGHT = 600, 600
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.Font(None, 20)

    SPACE = pymunk.Space()
    SPACE.gravity = 0, 900
    DRAW_OPTIONS = pgutil.DrawOptions(WINDOW)

    # define properties of balls
    mass = 10
    friction = 0.8
    radius = 10
    color = Color(255, 0, 0)
    inertia = pymunk.moment_for_circle(mass, 0, radius)
    
    balls = []
    def create_balls():
        """Create ball until pressing the mouse left button"""

        ball_body = pymunk.Body(mass, inertia)
        position = (pygame.mouse.get_pos()[0] + randint(1, 4), pygame.mouse.get_pos()[1])
        ball_body.position = position
        ball = pymunk.Circle(ball_body, radius)
        ball.color = color
        ball.friction = 0.6
        ball.elasticity = 0.9
        SPACE.add(ball_body, ball)
        balls.append(ball)

    def create_walls():
        """Create the walls"""

        walls = [
            pymunk.Segment(SPACE.static_body, (0, 50), (0, 250), 2),
            pymunk.Segment(SPACE.static_body, (0, 250), (300, 300), 2),
            pymunk.Segment(SPACE.static_body, (0, HEIGHT - 200), (0, HEIGHT), 2),
            pymunk.Segment(SPACE.static_body, (200, HEIGHT), (WIDTH, HEIGHT - 50), 2),
            pymunk.Segment(SPACE.static_body, (WIDTH, HEIGHT - 50), (WIDTH, HEIGHT - 250), 2)
        ]
        for wall in walls:
            wall.friction = 0.6
            wall.elasticity = 0.9
            wall.color = Color(0, 0, 255)
            SPACE.add(wall)

    def clear_junks():
        """Remove the balls when they are in outside of surface"""

        junk_balls = [ball for ball in balls if ball.body.position.y > HEIGHT]
        for ball in junk_balls:
            SPACE.remove(ball.body, ball)
            balls.remove(ball)

    def display_num_balls(num_balls):
        """Display number of ball on the Surface"""
        text = FONT.render(f"Number of Balls: {num_balls}", True, Color(0, 0, 0))
        WINDOW.blit(text, (5, 10))

    create_walls()

    running = True
    while running:
        WINDOW.fill(Color(255, 255, 255))
        CLOCK.tick(50)
        SPACE.step(1/60)
        SPACE.debug_draw(DRAW_OPTIONS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.mouse.get_pressed()[0]:
            create_balls()

        clear_junks()
        display_num_balls(len(balls))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
