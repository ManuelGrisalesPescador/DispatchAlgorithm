class Button():
    def __init__(self, x, y, image, Screen, pygame):
        self.pygame = pygame
        self.Screen = Screen
        self.Pressed = False
        self.Action = False
        self.image = image
        Width = self.image.get_width()
        Height = self.image.get_height()
        self.image = pygame.transform.scale(image, (Width * 0.15, Height * 0.15))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def Draw(self, pos):
        if self.rect.collidepoint(pos):
            if self.pygame.mouse.get_pressed()[0] == 1:
                self.Pressed = True
            else:
                if self.Pressed == True:
                    self.Action = True
                    self.Pressed = False

        self.Screen.blit(self.image, (self.rect.x, self.rect.y))