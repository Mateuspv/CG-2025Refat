import sys
import pygame
from dvd import MoveTexto
from dvd import Vertical
from dvd import Horizontal
from dvd import Quica
from config import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    FPS,
    PRETO,
    VERMELHO,
    BRANCO,
    VERDE,
    AZUL,
)


class Game:
    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("DVD")
        self.clock = pygame.time.Clock()
        self.running = True

        
        self.text = Quica("Rafael", 50, BRANCO, SCREEN_WIDTH, SCREEN_HEIGHT)
       
        
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.text.update()

    def draw(self):
        self.screen.fill(PRETO)
        self.text.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
