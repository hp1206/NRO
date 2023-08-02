import pygame

pygame.init()
screen = pygame.display.set_mode((300,300))
font = pygame.font.Font(None, 28)
text = font.render("Hello, world!", True, (255, 255, 255))
text_rect = text.get_rect()
while True:
    screen.blit(text,(30,30))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    '''print(text_rect.x)      # Tọa độ x của góc trái trên của hình chữ nhật chứa dòng chữ
    print(text_rect.y)      # Tọa độ y của góc trái trên của hình chữ nhật chứa dòng chữ
    print(text_rect.width)  # Chiều rộng của hình chữ nhật chứa dòng chữ
    print(text_rect.height) # Chiều cao của hình chữ nhật chứa dòng chữ'''

