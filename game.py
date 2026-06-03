import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.display_screen = pygame.display.set_mode((1920,1080))
        self.compute_screen_surface = pygame.Surface((1280,720))

        ### This is incredible full screen performance
        #self.display_screen = pygame.display.set_mode((1280, 720), pygame.SCALED | pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.main_loop()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def render(self):
        self.compute_screen_surface.fill("purple")

    def display(self):
        pygame.transform.scale(self.compute_screen_surface, (1920, 1080), self.display_screen)
        pygame.display.flip()

    def main_loop(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.display()
            self.clock.tick(60)
        pygame.quit()
