import pygame, sys

pygame.init()

x, y = 700, 400
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Dragon Boy')

bg = pygame.image.load('assest/RES2/bg/b142.png')
bg = pygame.transform.scale(bg, (x, y))
bg_fight = pygame.image.load('assest/RES2/bg/b13.png')
bg_fight = pygame.transform.scale(bg_fight, (x, y))
St = False
Backgound_list = []
def Play():
    screen.blit(bg_fight, (0, 0))


Font_game = pygame.font.Font('assest/Font/thirteen_pixel_fonts.ttf', 75)
Start_font = pygame.font.Font('assest/Font/Pixel Emulator.otf', 35)

Name_game = Font_game.render('NRO', True, (255, 165,0))
Start_button = Start_font.render('START', True, (255, 255, 255))

Start_x = 285
Start_y = 200
Backgound_list.append((bg,(0, 0)))
Backgound_list.append((Name_game, (x//2-100, y-300)))
Backgound_list.append((Start_button, (Start_x, Start_y)))
while True:
    Start_rect = Start_button.get_rect()
    rectangle_padding = 7
    rectangle_width = Start_rect.width + rectangle_padding * 2
    rectangle_height = Start_rect.height + rectangle_padding * 2
    rectangle_x = Start_x - rectangle_padding
    rectangle_y = Start_y - rectangle_padding
    '''pygame.draw.rect(screen, (255, 255, 255), (rectangle_x, rectangle_y, rectangle_width, rectangle_height), 2)'''
    Start_rect = pygame.Rect(rectangle_x, rectangle_y, rectangle_width, rectangle_height)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not St:
            for sf, pos in Backgound_list:
                screen.blit(sf, pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Start_rect.collidepoint(pygame.mouse.get_pos()) and St == False:
                St = True
                Play()
            #print(pygame.mouse.get_pos())

    
    pygame.display.flip()
