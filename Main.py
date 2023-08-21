import pygame, sys

pygame.init()

x, y = 700, 400
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Dragon Boy')

bg = pygame.image.load('assest/RES2/bg/b142.png')
bg = pygame.transform.scale(bg, (x, y))

St = False
Backgound_list = []
def Play():
    sky = pygame.image.load('assest/RES2/bg/b73.png')
    fighting_place_on = pygame.image.load("assest/background/x4/ImgBG_176.png")
    fighting_place_under = pygame.image.load("assest/background/x4/ImgBG_175.png")
    
    sky_scale = pygame.transform.scale(sky, (x*3, y))
    sky = pygame.transform.scale(sky, (x, y))
    fighting_place_on = pygame.transform.scale(fighting_place_on, (856, 128))
    fighting_place_under = pygame.transform.scale(fighting_place_under, (960, 156))
    fighting_place_on_right = pygame.transform.flip(fighting_place_on, True, False)
    fighting_place_under_right = pygame.transform.flip(fighting_place_under, True, False)
    screen.blit(sky, (0, 0))
    screen.blit(sky, (700, 0))
    screen.blit(sky, (-700, 0))
    screen.blit(sky_scale, (-700, -400))
    screen.blit(fighting_place_on, (-496, 116))
    screen.blit(fighting_place_under, (-600, 244))
    screen.blit(fighting_place_on_right, (-496+856, 116))
    screen.blit(fighting_place_under_right, (-600+960, 244))
    class MyMain(pygame.sprite.Sprite):
        def __init__(main_character):
            super().__init__()
            main_character.image = pygame.image.load("assest/RES2/bg/sun13.png")
            main_character.rect = main_character.image.get_rect()
            main_character.rect.center = (x // 3, y // 4)
            main_character.gravity = 2
            main_character.jump_power = - 10
            main_character.speed_x = 0
            main_character.speed_y = 0
            main_character.speed = 5
        def update(main_character, keys):
            if keys[pygame.K_UP] and not main_character.is_jumping:
                main_character.is_jumping = True
                #main_character.gravity = 0
                main_character.speed_y = main_character.jump_power
            if keys[pygame.K_LEFT]:
                main_character.speed_x = - main_character.speed
            if keys[pygame.K_RIGHT]:
                main_character.speed_x = main_character.speed
            main_character.rect.y += main_character.gravity
            print(main_character.rect)
            main_character.rect.x += main_character.speed_x
            main_character.rect.y += main_character.speed_y
            main_character.speed_x = 0

            if main_character.rect.bottom >= y - 156:
                main_character.rect.bottom = y - 156
                main_character.speed_y = 0
                main_character.is_jumping = False
            if main_character.rect.top <= 0:
                main_character.speed_y = 0
    my_main_character = MyMain()
    all_main = pygame.sprite.Group()
    all_main.add(my_main_character) 
    return my_main_character, all_main
    

Font_game = pygame.font.Font('assest/Font/thirteen_pixel_fonts.ttf', 75)
Start_font = pygame.font.Font('assest/Font/Pixel Emulator.otf', 35)

Name_game = Font_game.render('NRO', True, (255, 165,0))
Start_button = Start_font.render('START', True, (255, 255, 255))

Start_x = 285
Start_y = 200
Backgound_list.append((bg,(0, 0)))
Backgound_list.append((Name_game, (x//2-100, y-300)))
Backgound_list.append((Start_button, (Start_x, Start_y)))
my_main_character, all_main = Play()
while True:
    keys = pygame.key.get_pressed()
    all_main.update(keys)
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
    if St == True: 
        Play()
        all_main.draw(screen)
            #print(pygame.mouse.get_pos())
            

    
    pygame.display.flip()
