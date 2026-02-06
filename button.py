import pygame

class Button:
    def __init__(self, x, y, width, height, font, color, text, text_color, border_color, border_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.color = color
        self.text = text
        self.text_color = text_color
        self.hover_color = tuple(min(255, i + 40) for i in self.color)
        self.text_hover_color = tuple(min(255, i + 40) for i in self.text_color)
        self.border_color = border_color
        self.border_size = border_size

    def show(self, window):
        # Мишка
        mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse):
            pygame.draw.rect(window, self.hover_color, self.rect, border_radius=self.border_size)
            text_btn = self.font.render(self.text, True, self.text_hover_color)
            text_rect = text_btn.get_rect(center=self.rect.center)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.draw.rect(window, self.color, self.rect, border_radius=self.border_size)
            text_btn = self.font.render(self.text, True, self.text_color)
            text_rect = text_btn.get_rect(center=self.rect.center)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        window.blit(text_btn, text_rect)
        pygame.draw.rect(window, self.border_color, self.rect, 4, border_radius=self.border_size)

    def is_clicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return True
                
        return False
