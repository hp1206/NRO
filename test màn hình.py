import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Sprite và vật cản")

class SimpleSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assest/RES2/bg/sun1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)

# Tạo một sprite
sprite = SimpleSprite()

# Tạo nhóm sprite
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite)

obstacles = [
    pygame.Rect(100, 200, 200, 20),
    pygame.Rect(400, 100, 100, 50),
    pygame.Rect(600, 100, 50, 150),
]

WHITE = (255, 255, 255)

sprite_speed = 2

# Hàm hiển thị Game Over
def show_game_over():
    game_over_font = pygame.font.Font(None, 64)
    game_over_text = game_over_font.render("Game Over", True, (0, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.fill(WHITE)
    screen.blit(game_over_text, game_over_rect)
    pygame.display.flip()

# Vòng lặp chính của trò chơi
game_over = False
while True:
    # Xử lý các sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            sprite.rect.x -= sprite_speed
        if keys[pygame.K_RIGHT]:
            sprite.rect.x += sprite_speed
        if keys[pygame.K_UP]:
            sprite.rect.y -= sprite_speed
        if keys[pygame.K_DOWN]:
            sprite.rect.y += sprite_speed

        # Kiểm tra va chạm với vật cản
        for obstacle in obstacles:
            if sprite.rect.colliderect(obstacle):
                game_over = True

        # Cập nhật màn hình
        all_sprites.update()

        screen.fill(WHITE)

        # Vẽ các vật cản lên màn hình
        for obstacle in obstacles:
            pygame.draw.rect(screen, (0, 0, 0), obstacle)

        all_sprites.draw(screen)

        # Nếu Game Over được kích hoạt, hiển thị thông báo và không cập nhật màn hình
        if game_over:
            show_game_over()

        pygame.display.flip()

