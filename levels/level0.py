import pygame
from ..menu_buttons.menu_button import MenuButton

class LevelMenu:
    def __init__(self, screen):
        self.list_menu_object= []
        self.list_menu = ["Rapid Test", "New Game", "Continue", "Option", "Quit"]
        width_screen = screen.get_width()
        height_screen = screen.get_height()
        width, height = 250, 50
        x = int((width_screen - width)/2)
        nominaly = int(height_screen / (len(self.list_menu)+1))
        y = nominaly
        for menu in self.list_menu:
            button = MenuButton(x, y, width, height, text=menu)
            self.list_menu_object.append(button)
            y += nominaly

    def events(self, events, mouse_pos):
        for button in self.list_menu_object:
            if button.handle_event(events):
                print(f"Menu clicked {button.text}")
                return button.text
        return None

    def update(self, mouse_pos):
        for button in self.list_menu_object:
            button.update(mouse_pos)

    def draw(self, screen):
        for button in self.list_menu_object:
            button.draw(screen)
