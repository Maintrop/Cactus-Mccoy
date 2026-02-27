from pygame import *

class Button:
    def __init__(self, x, y, width, height, color, font, text, text_color, border_radius, border_width=6):
        self.rect = Rect(x, y, width, height)
        self.color = color
        self.font = font
        self.text = text
        self.text_color = text_color
        self.hover_color = tuple(min(255, i + 40) for i in self.color)
        self.hover_text_color = tuple(min(255, i + 40) for i in self.text_color)
        self.border_color = tuple(max(1, i - 10) for i in self.color)
        self.border_radius = border_radius
        self.border_width = border_width

    def is_hovered(self):
        return self.rect.collidepoint(mouse.get_pos())

    def show(self, window):
        if self.is_hovered():
            draw.rect(window, self.hover_color, self.rect, border_radius=self.border_radius)
            text_btn = self.font.render(self.text, True, self.hover_text_color)
            text_rect = text_btn.get_rect(center=self.rect.center)
        else:
            draw.rect(window, self.color, self.rect, border_radius=self.border_radius)
            text_btn = self.font.render(self.text, True, self.text_color)
            text_rect = text_btn.get_rect(center=self.rect.center)

        window.blit(text_btn, text_rect)
        draw.rect(window, self.border_color, self.rect, self.border_width, border_radius=self.border_radius)

    def is_clicked(self, events):
        for event in events:
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered():
                return True
        return False
