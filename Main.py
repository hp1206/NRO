import pygame, sys

pygame.init()

x, y = 1050, 600
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Dragon Boy')

bg = pygame.image.load('assest/RES2/bg/b142.png')
bg = pygame.transform.scale(bg, (x, y))

St = False
Backgound_list = []
def Play():
    pause_button = pygame.image.load('assest/Assest Download/pause.png')
    sky = pygame.image.load('assest/RES2/bg/b73.png')
    fighting_place_on = pygame.image.load("assest/background/x4/ImgBG_176.png")
    fighting_place_under = pygame.image.load("assest/background/x4/ImgBG_175.png")
    
    sky_scale = pygame.transform.scale(sky, (x*3, y))
    sky = pygame.transform.scale(sky, (x, y))
    pause_button = pygame.transform.scale(pause_button, (pause_button.get_width()//10, pause_button.get_height()//10))
    fighting_place_on = pygame.transform.scale(fighting_place_on, (856, 96))
    fighting_place_under = pygame.transform.scale(fighting_place_under, (960, 117))
    fighting_place_on_right = pygame.transform.flip(fighting_place_on, True, False)
    fighting_place_under_right = pygame.transform.flip(fighting_place_under, True, False)
    screen.blit(sky, (0, 0))
    screen.blit(sky, (x, 0))
    screen.blit(sky, (-x, 0))
    screen.blit(sky_scale, (-x, -y))
    screen.blit(pause_button, (x//2- pause_button.get_width()//2, 10))
    screen.blit(fighting_place_on, (x//2-960+(960-856), y-117-96))
    screen.blit(fighting_place_under, (x//2-960, y-117))
    screen.blit(fighting_place_on_right, (x//2, y-117-96))
    screen.blit(fighting_place_under_right, (x//2, y-117))
    class MyMain(pygame.sprite.Sprite):
        def __init__(main_character):
            super().__init__()
            main_character.image = pygame.image.load("assest/RES2/bg/sun13.png")
            main_character.rect = main_character.image.get_rect()
            main_character.rect.center = (x // 4, y // 4)
            main_character.gravity = 7
            main_character.jump_power = - 17
            main_character.speed_x = 0
            main_character.speed_y = 0
            main_character.speed = 10
        def update(main_character, keys):
            if keys[pygame.K_w] and not main_character.is_jumping:
                main_character.is_jumping = True
                main_character.gravity = 0
                main_character.speed_y = main_character.jump_power
            if keys[pygame.K_a]:
                main_character.speed_x = - main_character.speed
            if keys[pygame.K_d]:
                main_character.speed_x = main_character.speed
            main_character.rect.y += main_character.gravity
            main_character.rect.x += main_character.speed_x
            main_character.rect.y += main_character.speed_y
            main_character.speed_x = 0

            if main_character.rect.bottom >= y - 117:
                main_character.rect.bottom = y - 117
                main_character.speed_y = 0
                main_character.is_jumping = False
            if main_character.rect.top <= 100:
                main_character.speed_y = 0
                main_character.gravity = 10

    my_main_character = MyMain()
    all_main = pygame.sprite.Group()
    all_main.add(my_main_character) 
    return my_main_character, all_main
    

Font_game = pygame.font.Font('assest/Font/thirteen_pixel_fonts.ttf', 112)
Start_font = pygame.image.load('assest/Assest Download/start.png')
quit_button = pygame.image.load('assest/Assest Download/QUIT.png')
quit_button = pygame.transform.scale(quit_button, (quit_button.get_width()//60, quit_button.get_height()//60))
Name_game = Font_game.render('NRO', True, (255, 165,0))
Start_button = pygame.transform.scale(Start_font, (Start_font.get_width()//1.5, Start_font.get_height()//1.5))
Start_x = x//2 - Start_button.get_width()//2 
Start_y = y//2 - Start_button.get_height()//2 + Start_button.get_height()//2
Name_game_x = x//2 - Name_game.get_width()//2
Name_game_y = y//2 - Name_game.get_height()//2 - Name_game.get_height()//2 
quit_x = x//2 - quit_button.get_width()//2
quit_y = y//2 - quit_button.get_height()//2 + quit_button.get_height()*2
Backgound_list.append((bg,(0, 0)))
Backgound_list.append((Name_game, (Name_game_x, Name_game_y)))
Backgound_list.append((Start_button, (Start_x, Start_y)))
Backgound_list.append((quit_button, (quit_x, quit_y)))
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
    Start_rect = pygame.Rect(rectangle_x, rectangle_y, rectangle_width, rectangle_height)
    quit_rect = pygame.Rect(quit_x, quit_y, quit_button.get_width(), quit_button.get_height())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if not St:
        screen.blits(Backgound_list)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if quit_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if Start_rect.collidepoint(pygame.mouse.get_pos()) and St == False:
            St = True
    if St == True: 
        Play()
        all_main.draw(screen)
    #print(pygame.mouse.get_pos())
            


    pygame.display.flip()

