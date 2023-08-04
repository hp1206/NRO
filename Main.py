import pygame, sys

pygame.init()

x, y = 700, 400
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Dragon Boy')

bg = pygame.image.load('assest/RES2/bg/b142.png')
bg = pygame.transform.scale(bg, (x, y))
bg_x=0

Font_game = pygame.font.Font('assest/Font/thirteen_pixel_fonts.ttf', 75)
Start_font = pygame.font.Font('assest/Font/Pixel Emulator.otf', 35)

Name_game = Font_game.render('NRO', True, (255, 165,0))
Start_button = Start_font.render('START', True, (255, 255, 255))

Start_rect = Start_button.get_rect()
Start_x = 285 
Start_y = 200 

rectangle_padding = 7
rectangle_width = Start_rect.width + rectangle_padding * 2
rectangle_height = Start_rect.height + rectangle_padding * 2
rectangle_x = Start_x - rectangle_padding
rectangle_y = Start_y - rectangle_padding

while True:
    bg_x-=0.09
    screen.blit(bg, (bg_x,0))
    screen.blit(bg,(bg_x+700,0))
    screen.blit(Name_game, (x//2-100, y-300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    if bg_x==-700:
        bg_x=0
    pygame.draw.rect(screen, (255, 255, 255), (rectangle_x, rectangle_y, rectangle_width, rectangle_height), 2)

    screen.blit(Start_button, (Start_x, Start_y))
    
    pygame.display.update()
