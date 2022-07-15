import pygame
from pygame.locals import *

class VideoService:

    def __init__(self):

        self._size = self._width, self._height = (1200, 800)

    def open_window(self):


        screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption("Alien Dodge")
        screen.fill((60, 220, 0))

        
        pygame.display.update()
        
        return screen

          

    def is_window_open(self):

        return True

    def close_window(self):

        pygame.quit()
