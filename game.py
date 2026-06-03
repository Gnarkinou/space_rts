import pygame
from levels.level0 import LevelMenu

class Game:
    def __init__(self):
        pygame.init()
        self.display_screen = pygame.display.set_mode((1920,1080))
        self.compute_screen_surface = pygame.Surface((1280,720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.Level = LevelMenu(self.compute_screen_surface)
        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.Level.update(self.mouse_pos)

    def render(self):
        self.compute_screen_surface.fill("purple")

    def display(self):
        pygame.transform.scale(self.compute_screen_surface, (1920, 1080), self.display_screen)
        pygame.display.flip()

    def main_loop(self):
        while self.running:
            self.get_adjusted_mouse_pos()
            self.handle_events()
            self.update()
            self.render()
            self.display()
            self.clock.tick(60)
        pygame.quit()

    def get_adjusted_mouse_pos(self):
        mouse_pos = pygame.mouse.get_pos()
        adjusted_x = int(mouse_pos[0] * (1280 / 1920))
        adjusted_y = int(mouse_pos[1] * (720 / 1080))
        self.mouse_pos = (adjusted_x, adjusted_y)
