import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
font = pygame.font.Font(None, 28)  # Tạo font chữ

text = font.render("Hello, world!", True, (255, 255, 255))  # Tạo dòng chữ
screen.blit(text, (30,30))  # Vẽ dòng chữ
text.get

text_rect = text.get_rect()  # Lấy kích thước rect của dòng chữ
padding = 10  # Khoảng cách từ dòng chữ đến viền của hình chữ nhật

rect_width = text_rect.width + padding * 2
rect_height = text_rect.height + padding * 2

rect = pygame.Rect(text_rect.left - padding, text_rect.top - padding, rect_width, rect_height)  # Tạo rect

pygame.draw.rect(screen, (0, 0, 255), rect)  # Vẽ hình chữ nhật màu xanh lá cây

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
