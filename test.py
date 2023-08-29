import pygame

pygame.init()
x, y = 900, 500
screen = pygame.display.set_mode((x, y))
def test():
    class MySf(pygame.sprite.Sprite):
        def __init__(surface):
            super().__init__()
            surface.image = pygame.image.load('assest/RES2/bg/sun13.png')
            surface.rect = surface.image.get_rect()
            surface.rect.center = ((x // 3, y // 2))
        
        def update(surface, keys):
            if keys[pygame.K_RIGHT]:
                surface.rect.x += 1
            if keys[pygame.K_LEFT]:
                surface.rect.x += -1
        
    
    Surface = MySf()
    Gr = pygame.sprite.Group()
    Gr.add(Surface)
    return Surface,Gr
Surface, Gr = test()
while True:
    keys = pygame.key.get_pressed()
    Surface.update(keys)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if True:
            screen.fill((0, 0, 0))
            Gr.draw(screen)
            
    pygame.display.flip()