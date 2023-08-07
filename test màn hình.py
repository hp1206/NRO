import pygame
import sys
import random

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
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
class SquareObstacle(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((80, 80)) 
        self.image.fill((0, 255, 0)) 
class RectangularObstacle(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((120, 80))  
        self.image.fill((0, 0, 255)) 
class CircularObstacle(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((70, 70), pygame.SRCALPHA)  
        pygame.draw.circle(self.image, (255, 255, 0, 255), (35, 35), 35)
#Tạo một list Obstacles để lưu trữ 
obstacles_list = []
# Tạo một sprite
sprite = SimpleSprite()

# Tạo nhóm sprite
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite)

#Tạo một biến frame để lưu trữ khung hình mỗi khi random
frame = 0
# Tạo hàm để tạo mới vật cản random
def create_obstacles():
    obstacles_list.clear()
    for _ in range(3):
        x = random.randint(0, screen_width - 100)
        y = random.randint(0, screen_height - 100)
        obstacle_type = random.choice([SquareObstacle, RectangularObstacle, CircularObstacle])
        obstacle = obstacle_type(x, y)
        obstacles_list.append(obstacle)
# Tạo 3 vật cản random ban đầu
create_obstacles()

WHITE = (255, 255, 255)

sprite_speed = 2

# Hàm hiển thị Game Over
def show_game_over():
    game_over_font = pygame.font.Font(None, 64)
    try_again_font = pygame.font.Font(None, 32)
    game_over_text = game_over_font.render("Game Over", True, (0, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
    try_again_text = try_again_font.render("Try Again (Press Enter)", True, (0, 0, 0))
    try_again_rect = try_again_text.get_rect(center=(screen_width // 2 , screen_height // 2 + 50))
    screen.fill(WHITE)
    screen.blit(try_again_text, try_again_rect)
    screen.blit(game_over_text, game_over_rect)
    pygame.display.flip()


game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and game_over:
                # Thiết lập lại trạng thái ban đầu khi người chơi chọn chơi lại
                sprite.rect.center = (screen_width // 2 , screen_height // 2)
                game_over = False
                create_obstacles()

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
        for obstacle in obstacles_list:
            if sprite.rect.colliderect(obstacle.rect):
                game_over = True
        #all_sprites.update()
        screen.fill(WHITE)
        for obstacle in obstacles_list:
            screen.blit(obstacle.image, obstacle.rect)
        screen.blit(sprite.image, sprite.rect)

        all_sprites.draw(screen)

        # Nếu Game Over được kích hoạt, hiển thị thông báo và không cập nhật màn hình
        if game_over:
            show_game_over()

        pygame.display.flip()
        #Tăng frame cho mỗi lần lặp
        frame += 1

