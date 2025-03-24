import sys
import pygame
from dvd import (MoveTexto, Vertical, Horizontal, Quica, handle_music_events,)
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
    """
    Classe principal do jogo que gerencia a execução do loop principal,
    captura eventos, atualiza estados e desenha elementos na tela.
    """
    def __init__(self):
        """
        Inicializa o jogo, configurando a tela, relógio e estado inicial.
        """

        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("DVD")
        self.clock = pygame.time.Clock()
        self.running = True

        # Inicializa o texto em movimento
        self.text = MoveTexto("Mateus", 50, BRANCO, SCREEN_WIDTH, SCREEN_HEIGHT) 

    def events(self):
        """
        Captura e processa eventos do teclado e do mouse.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            handle_music_events(event, self.text)

    def update(self):
        """
        Atualiza os objetos na tela, como a posição do texto em movimento.
        """
        self.text.update()

    def draw(self):
        """
        Renderiza os elementos gráficos na tela. 
        """
        self.screen.fill(PRETO)
        self.text.draw(self.screen)
        pygame.display.flip()

    def run(self):
        """
        Executa o loop principal do jogo, chamando os métodos de eventos,
        atualização e desenho em cada iteração.
        """
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()