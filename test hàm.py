import pygame
import sys

pygame.init()

# Khởi tạo màn hình đồ họa
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Example")

# Định nghĩa lớp con kế thừa từ pygame.sprite.Sprite
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Màu đỏ
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
        self.speed_x = 0  # Tốc độ di chuyển ngang của sprite
        self.speed_y = 0  # Tốc độ di chuyển dọc của sprite
        self.gravity = 0.01  # Hệ số trọng lực
        self.jump_power = - 2

    def update(self, keys):
        if keys[pygame.K_UP] and not self.is_jumping:
            self.is_jumping = True
            self.speed_y = self.jump_power
        if keys[pygame.K_LEFT]:
            self.speed_x -= 0.005
        if keys[pygame.K_RIGHT]:
            self.speed_x += 0.005

        # Áp dụng trọng lực
        self.speed_y += self.gravity

        # Cập nhật vị trí sprite dựa trên tốc độ
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Giới hạn sprite trong màn hình
        self.rect.x = max(0, min(self.rect.x, width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, height - self.rect.height))

        # Kiểm tra va chạm với mặt đất
        if self.rect.bottom >= height - 50:
            self.rect.bottom = height - 50
            self.speed_y = 0
            self.is_jumping = False

# Tạo một đối tượng sprite từ lớp con đã định nghĩa
my_sprite = MySprite()

# Tạo một lớp vật cản
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((0, 0, 255))  # Màu xanh dương
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2 - 100)
        self.speed = 2

    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0 or self.rect.right > width:
            self.speed *= -1

# Tạo một lớp mặt đất
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((width, 50))
        self.image.fill((0, 255, 0))  # Màu xanh lá cây
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, height - 50)  # Vị trí bên dưới cùng

# Tạo một đối tượng vật cản và mặt đất
obstacle = Obstacle()
ground = Ground()

# Tạo một nhóm (group) chứa sprite, vật cản và mặt đất
all_sprites = pygame.sprite.Group()
all_sprites.add(my_sprite, ground)

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Lấy trạng thái các phím
    keys = pygame.key.get_pressed()

    # Cập nhật sprite dựa trên trạng thái phím
    my_sprite.update(keys)

    # Cập nhật vật cản
    obstacle.update()

    # Xóa màn hình
    screen.fill((255, 255, 255))

    # Hiển thị mặt đất
    all_sprites.draw(screen)

    # Cập nhật màn hình
    pygame.display.flip()
