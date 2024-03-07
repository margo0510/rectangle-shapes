import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([500, 500])


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

screen.fill(YELLOW)


class Rect:
    def __init__(self, color, dimensions):
        self.color = color
        self.dimensions = dimensions

    def draw(self):
        pygame.draw.rect(screen, self.color, self.dimensions)


rect1_dimensions = (50, 50, 100, 100)
rect2_dimensions = (200, 200, 150, 75)
rect3_dimensions = (350, 100, 80, 120)

red_rect = Rect(RED, rect1_dimensions)
green_rect = Rect(GREEN, rect2_dimensions)
blue_rect = Rect(BLUE, rect3_dimensions)

red_rect.draw()
green_rect.draw()
blue_rect.draw()



pygame.display.update()


