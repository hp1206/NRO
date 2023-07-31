import pygame, sys

pygame.init()

x, y = 700, 400
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Dragonboy')

bg = pygame.image.load('assest/RES2/bg/b142.png')
bg = pygame.transform.scale(bg, (x, y))

Font_game = pygame.font.Font('assest/Font/thirteen_pixel_fonts.ttf', 75)
Start_font = pygame.font.Font('assest/Font/Pixel Emulator.otf', 35)

Name_game = Font_game.render('NRO', True, (255, 165,0))
Start_button = Start_font.render('START', True, (255, 255, 255))
Start_button_rect = pygame.Rect(250, )

while True:
    screen.blit(bg, (0,0))
    screen.blit(Name_game, (x//2-100, y-300))
    screen.blit(Start_button, (285 ,190))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()