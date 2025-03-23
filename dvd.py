import pygame 
import random
from config import (
    SPEED,
    RANDOMCOLOR
)

class MoveTexto:
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        self.font = pygame.font.SysFont(None, font_size)
        self.color = initial_color
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(
            center=(screen_width / 2, screen_height / 2)
        )

        self.speed_x = SPEED
        self.speed_y = SPEED

        self.screen_width = screen_width
        self.screen_height = screen_height

    def _change_color(self):

        self.color_random = (
            random.randint(10, 255),
            random.randint(10, 255),
            random.randint(10, 255),
        )
        self.color = self.color_random
        self.text_surf = self.font.render(self.text, True, self.color)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0:
            self.speed_x = random.randint(0, 1)
            self.speed_y = random.randint(-1, 1)
            self._change_color()

        if self.rect.right >= self.screen_width:
            self.speed_x = random.randint(-1, 0)
            self.speed_y = random.randint(1, 1)
            self._change_color()

        if self.rect.top <= 0:
            self.speed_x = random.randint(-1, 1)
            self.speed_y = random.randint(0, 1)
            self._change_color()

        if self.rect.bottom >= self.screen_height:
            self.speed_x = random.randint(-1, 1)
            self.speed_y = random.randint(-1, 0)
            self._change_color()

    def draw(self, screen):
        screen.blit(self.text_surf, self.rect)


class Quica(MoveTexto):
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        super().__init__(text, font_size, initial_color, screen_width, screen_height)

        self.time_elapsed = 0
        self.last_change_time = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0:
            self.speed_x = random.randint(0, 1)
            self.speed_y = random.randint(-1, 1)
            self._change_color()

        if self.rect.right >= self.screen_width:
            self.speed_x = random.randint(-1, 0)
            self.speed_y = random.randint(1, 1)
            self._change_color()

        if self.rect.top <= 0:
            self.speed_x = random.randint(-1, 1)
            self.speed_y = random.randint(0, 1)
            self._change_color()

        if self.rect.bottom >= self.screen_height:
            self.speed_x = random.randint(-1, 1)
            self.speed_y = random.randint(-1, 0)
            self._change_color()
        
        current_time = pygame.time.get_ticks()
        time_since_last_change = current_time - self.last_change_time
        
        if time_since_last_change >= 5000:
            self.last_change_time = current_time
            

    def draw(self, screen):
        screen.blit(self.text_surf, self.rect) 
class Vertical(MoveTexto):
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        super().__init__(text, font_size, initial_color, screen_width, screen_height)
        
    def update(self):
        self.rect.x += self.speed_x

        if self.rect.left <= 0:
            self.speed_x = random.randint(0, 1)
            self._change_color()

        if self.rect.right >= self.screen_width:
            self.speed_x = random.randint(-1, 0)
            self._change_color()

class Horizontal(MoveTexto):
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        super().__init__(text, font_size, initial_color, screen_width, screen_height)
        
    def update(self):
        self.rect.y += self.speed_y

        if self.rect.top <= 0:
            self.speed_x = random.randint(-1, 1)
            self.speed_y = random.randint(0, 1)
            self._change_color()

        if self.rect.bottom >= self.screen_height:
            self.speed_x = random.randint(-1, 1)
            self.speed_y = random.randint(-1, 0)
            self._change_color()
