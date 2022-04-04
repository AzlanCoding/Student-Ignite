class igniteGUI:
  def __init__ (self, *args, **kwargs):
    import pygame
    pygame.init()
    pygame.display.init()
    MainWindow = pygame.display.set_mode([800,600])
