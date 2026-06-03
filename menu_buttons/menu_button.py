import pygame

class MenuButton:
    def __init__(self, x, y, width, height, text="Click me!", button_type="default", background_color=None, text_color="white", text_size=16, text_size_big=32):
        self.rect = pygame.Rect(x, y, width, height)
        self.button_type = button_type
        self.background_color = background_color
        self.text_color = text_color
        self.text = text
        self.text_size, self.text_size_small, self.text_size_big = text_size, text_size, text_size_big
        self.init_font()
        self.is_hovered, self.is_clicked = False, False

    def init_font(self):
        self.font = pygame.font.SysFont("Arial", self.text_size)
        self.text_render = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_render.get_rect(center=self.rect.center)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if not self.is_hovered:
                self.text_size = self.text_size_big
                self.init_font()
            self.is_hovered = True
        else:
            if self.is_hovered:
                self.text_size = self.text_size_small
                self.init_font()
            self.is_hovered = False

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                return True
        return False

    def draw(self, screen):
        if self.background_color is not None:
            pygame.draw.rect(screen, self.background_color, self.rect)
        screen.blit(self.text_render, self.text_rect)
