import pygame 
import random
from config import (
    SPEED,
    RANDOMCOLORINICIAL,
    RANDOMCOLORFINAL,
    SOUNDEFFECT, 
    MUSICTRACKS
)

class MoveTexto:
    """
    Classe responsável por mover um texto na tela, mudando de cor ao colidir com as bordas.
    Também gerencia efeitos sonoros e reprodução de música.
    """
    
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        """
        Inicializa o texto, sua posição, velocidade, cor e sons.
        """
        pygame.mixer.init()  # Inicializa o mixer antes de carregar sons
        
        self.font = pygame.font.SysFont(None, font_size)
        self.color = initial_color
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(center=(screen_width / 2, screen_height / 2))

        self.speed_x = SPEED
        self.speed_y = SPEED
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Carrega o efeito sonoro de colisão
        self.sound_effect = pygame.mixer.Sound(SOUNDEFFECT)
        self.sound_effect.set_volume(0.6)
        
        # Carrega e gerencia a música
        self.tracks = MUSICTRACKS
        self.current_track = 0
        pygame.mixer.music.load(self.tracks[self.current_track])
        pygame.mixer.music.play(-1)  # Loop infinito
        self.is_paused = False
    
    def toggle_pause(self):
        """Alterna entre pausar e retomar a música."""
        if self.is_paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        self.is_paused = not self.is_paused
    
    def next_track(self):
        """Troca para a próxima música na lista."""
        self.current_track = (self.current_track + 1) % len(self.tracks)
        pygame.mixer.music.load(self.tracks[self.current_track])
        pygame.mixer.music.play(-1)
            
    def _change_color(self):
        """Muda a cor do texto aleatoriamente ao colidir com as bordas."""
        self.color = (
            random.randint(RANDOMCOLORINICIAL, RANDOMCOLORFINAL),
            random.randint(RANDOMCOLORINICIAL, RANDOMCOLORFINAL),
            random.randint(RANDOMCOLORINICIAL, RANDOMCOLORFINAL),
        )
        self.text_surf = self.font.render(self.text, True, self.color)

    def update(self):
        """Atualiza a posição do texto e verifica colisões com as bordas."""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        hit_x = self.rect.left <= 0 or self.rect.right >= self.screen_width
        hit_y = self.rect.top <= 0 or self.rect.bottom >= self.screen_height
        
        self.speed_x *= 1 - 2 * hit_x 
        self.speed_y *= 1 - 2 * hit_y  

        if hit_x or hit_y:
            self._change_color()
            self.sound_effect.play()

    def draw(self, screen):
        """Desenha o texto na tela."""
        screen.blit(self.text_surf, self.rect)   


def handle_music_events(event, text_obj):
    """Gerencia eventos de teclado relacionados à música."""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            text_obj.toggle_pause()
        elif event.key == pygame.K_s:
            text_obj.next_track()   


class Quica(MoveTexto):
    """
    Variante de MoveTexto que quica a cada 2 segundo.
    """
    
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        """Inicializa o objeto com as propriedades básicas e controle de tempo."""
        super().__init__(text, font_size, initial_color, screen_width, screen_height)
        self.time_elapsed = 0
        self.last_change_time = pygame.time.get_ticks()

    def update(self):
        """Atualiza a posição e altera a direção vertical a cada 2 segundos."""
        super().update()
        
        current_time = pygame.time.get_ticks()
        if current_time - self.last_change_time >= 2000:
            self.last_change_time = current_time
            self.speed_y *= -1
    

class Horizontal(MoveTexto):
    """
    Variante de MoveTexto que se move apenas horizontalmente.
    """
    
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        """Inicializa o objeto sem modificar as configurações do movimento."""
        super().__init__(text, font_size, initial_color, screen_width, screen_height)
        
    def update(self):
        """Atualiza a posição horizontalmente e verifica colisões."""
        
        self.rect.x += self.speed_x
        hit_x = self.rect.left <= 0 or self.rect.right >= self.screen_width
        self.speed_x *= 1 - 2 * hit_x 
        
        if hit_x:
            self._change_color()
            self.sound_effect.play()


class Vertical(MoveTexto):
    """
    Variante de MoveTexto que se move apenas verticalmente.
    """
    
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        """Inicializa o objeto sem modificar as configurações do movimento."""
        super().__init__(text, font_size, initial_color, screen_width, screen_height)
        
    def update(self):
        """Atualiza a posição verticalmente e verifica colisões."""
        self.rect.y += self.speed_y
        hit_y = self.rect.top <= 0 or self.rect.bottom >= self.screen_height
        self.speed_y *= 1 - 2 * hit_y
        
        if hit_y:
            self._change_color()
            self.sound_effect.play()
