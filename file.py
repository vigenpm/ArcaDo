import os
import pygame
import random


def load_image(name):
    fullname = os.path.join(name)
    return pygame.image.load(fullname).convert()


def load_image2(name):
    fullname = os.path.join(name)
    return pygame.image.load(fullname).convert_alpha()


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(ball_group, all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, (72, 1, 255), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)

    def update(self):
        self.rect = self.rect.move(0, -3)
        if pygame.sprite.spritecollideany(self, enemy_group):
            pygame.sprite.spritecollideany(self, enemy_group).health -= 10
            self.kill()
        if self.rect.y <= 0:
            self.kill()


class NextLevel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('nextLevel.png')
        self.rect = (0, 0)


class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('gameOver.png')
        self.rect = (0, 0)


class YouWon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('youWon.png')
        self.rect = (0, 0)


class GameStart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('gameStart.png')
        self.rect = (0, 0)


class Quit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image2('quit.png')
        self.rect = (10, 450)


class Level(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image2('level.png')
        self.rect = (10, 55)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = load_image('player.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)

    def update(self):
        if pygame.sprite.spritecollideany(self, enemy_group):
            pygame.sprite.spritecollideany(self, enemy_group).health -= 10


class Heart(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(hearts_group)
        self.image = load_image2('heart.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)


class EnemyLight(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(enemy_light_group, enemy_group, all_sprites)
        self.image = load_image('enemyLight.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.health = 20

    def update(self):
        global enemy_kol_killed
        self.image.set_alpha(255 * (self.health / 20))
        if self.health <= 0:
            enemy_kol_killed += 1
            self.kill()
        if self.rect.y >= 450:
            global hearts_kol
            hearts_kol -= 1
            enemy_kol_killed += 1
            self.kill()
        self.rect = self.rect.move(0, 1)


class EnemyMiddle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(enemy_middle_group, enemy_group, all_sprites)
        self.image = load_image('enemyMiddle.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.health = 30

    def update(self):
        global enemy_kol_killed
        self.image.set_alpha(255 * (self.health / 30))
        if self.health <= 0:
            enemy_kol_killed += 1
            self.kill()
        if self.rect.y >= 450:
            global hearts_kol
            hearts_kol -= 1
            enemy_kol_killed += 1
            self.kill()
        self.rect = self.rect.move(0, 1)


class EnemyHard(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(enemy_hard_group, enemy_group, all_sprites)
        self.image = load_image('enemyHard.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.health = 50

    def update(self):
        global enemy_kol_killed
        self.image.set_alpha(255 * (self.health / 50))
        if self.health <= 0:
            enemy_kol_killed += 1
            self.kill()
        if self.rect.y >= 450:
            global hearts_kol
            hearts_kol -= 1
            enemy_kol_killed += 1
            self.kill()
        self.rect = self.rect.move(0, 1)


def init():
    global all_sprites
    all_sprites = pygame.sprite.Group()
    global player_group
    player_group = pygame.sprite.Group()
    global ball_group
    ball_group = pygame.sprite.Group()
    global hearts_group
    hearts_group = pygame.sprite.Group()
    global enemy_group
    enemy_group = pygame.sprite.Group()
    global enemy_light_group
    enemy_light_group = pygame.sprite.Group()
    global enemy_middle_group
    enemy_middle_group = pygame.sprite.Group()
    global enemy_hard_group
    enemy_hard_group = pygame.sprite.Group()
    global player
    player = Player(230, 460)
    global f1
    f1 = 0
    global f2
    f2 = 0
    global f2_tick
    f2_tick = 0
    global enemy_tick
    enemy_tick = 0
    global hearts_kol
    hearts_kol = 3
    global level
    level = 1
    global enemy_kol
    enemy_kol = 0
    global enemy_kol_killed
    enemy_kol_killed = 0
    global first_time_game_start
    first_time_game_start = 0


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('ArcaDo')
pygame.display.set_icon(pygame.image.load('logo5.png'))
clock = pygame.time.Clock()
running = True
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()
hearts_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemy_light_group = pygame.sprite.Group()
enemy_middle_group = pygame.sprite.Group()
enemy_hard_group = pygame.sprite.Group()
player = Player(230, 460)
st = 1
f1 = 0
f2 = 0
f2_tick = 0
enemy_tick = 0
hearts_kol = 3
level = 1
enemy_kol = 0
enemy_kol_killed = 0
first_time_game_start = 0

while running:
    if st == 3:
        all_sprites.empty()
        screen.fill((0, 0, 0))
        GameOver()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 360 > event.pos[0] > 130 and 400 > event.pos[1] > 350:
                    init()
                    st = 1
        all_sprites.draw(screen)
    elif st == 5:
        all_sprites.empty()
        screen.fill((0, 0, 0))
        YouWon()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 360 > event.pos[0] > 130 and 400 > event.pos[1] > 350:
                    init()
                    st = 1
        all_sprites.draw(screen)
    elif st == 1:
        all_sprites.empty()
        screen.fill((0, 0, 0))
        GameStart()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 > event.pos[0] > 200 and 400 > event.pos[1] > 350:
                    st = 2
                    init()
                    first_time_game_start = 1
        all_sprites.draw(screen)
    elif st == 4:
        all_sprites.empty()
        screen.fill((0, 0, 0))
        NextLevel()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 350 > event.pos[0] > 150 and 400 > event.pos[1] > 350:
                    lvl = level
                    init()
                    level = lvl
                    st = 2
                    first_time_game_start = 1
        all_sprites.draw(screen)
    else:
        player.update()
        enemy_tick += 1
        for i in ball_group:
            i.update()
        for i in enemy_group:
            i.update()
        # print(level)
        # print(enemy_kol_killed)
        if hearts_kol <= 0:
            st = 3
        if level == 1:
            if enemy_kol >= 40 and enemy_kol_killed >= 40:
                level = 2
                st = 4
            if enemy_tick % 60 == 0 and enemy_kol < 40:
                enemy = EnemyLight(random.randrange(110, 450), 10)
                if pygame.sprite.spritecollideany(enemy, enemy_group) \
                        and pygame.sprite.spritecollideany(enemy, enemy_group) is not enemy:
                    enemy.kill()
                else:
                    enemy_kol += 1
        elif level == 2:
            if enemy_kol >= 60 and enemy_kol_killed >= 60:
                level = 3
                st = 4
            if enemy_tick % 50 == 0 and enemy_kol < 60:
                enemy = EnemyLight(random.randrange(110, 450), 10)
                if pygame.sprite.spritecollideany(enemy, enemy_group) \
                        and pygame.sprite.spritecollideany(enemy, enemy_group) is not enemy:
                    enemy.kill()
                else:
                    enemy_kol += 1
            if enemy_tick % 150 == 0 and enemy_kol < 60:
                enemy = EnemyMiddle(random.randrange(110, 450), 10)
                if pygame.sprite.spritecollideany(enemy, enemy_group) \
                        and pygame.sprite.spritecollideany(enemy, enemy_group) is not enemy:
                    enemy.kill()
                else:
                    enemy_kol += 1
        elif level == 3:
            if enemy_kol >= 90 and enemy_kol_killed >= 90:
                level = 4
                st = 4
            if enemy_tick % 45 == 0 and enemy_kol < 90:
                enemy = EnemyLight(random.randrange(110, 450), 10)
                if pygame.sprite.spritecollideany(enemy, enemy_group) \
                        and pygame.sprite.spritecollideany(enemy, enemy_group) is not enemy:
                    enemy.kill()
                else:
                    enemy_kol += 1
            if enemy_tick % 120 == 0 and enemy_kol < 90:
                enemy = EnemyMiddle(random.randrange(110, 450), 10)
                if pygame.sprite.spritecollideany(enemy, enemy_group) \
                        and pygame.sprite.spritecollideany(enemy, enemy_group) is not enemy:
                    enemy.kill()
                else:
                    enemy_kol += 1
        elif level == 4:
            if enemy_kol >= 120 and enemy_kol_killed >= 120:
                level = 5
                st = 4
            if enemy_tick % 45 == 0 and enemy_kol < 120:
                enemy = EnemyLight(random.randrange(110, 450), 10)
                if pygame.sprite.spritecollideany(enemy, enemy_group) \
                        and pygame.sprite.spritecollideany(enemy, enemy_group) is not enemy:
                    enemy.kill()
                else:
                    enemy_kol += 1
            if enemy_tick % 110 == 0 and enemy_kol < 120:
                enemy = EnemyMiddle(random.randrange(110, 450), 10)
                if pygame.sprite.spritecollideany(enemy, enemy_group) \
                        and pygame.sprite.spritecollideany(enemy, enemy_group) is not enemy:
                    enemy.kill()
                else:
                    enemy_kol += 1
            if enemy_tick % 170 == 0 and enemy_kol < 120:
                enemy = EnemyHard(random.randrange(110, 450), 10)
                if pygame.sprite.spritecollideany(enemy, enemy_group) \
                        and pygame.sprite.spritecollideany(enemy, enemy_group) is not enemy:
                    enemy.kill()
                else:
                    enemy_kol += 1
        elif level == 5:
            if enemy_kol >= 150 and enemy_kol_killed >= 150:
                st = 5
            if enemy_tick % 40 == 0 and enemy_kol < 150:
                enemy = EnemyLight(random.randrange(110, 450), 10)
                if pygame.sprite.spritecollideany(enemy, enemy_group) \
                        and pygame.sprite.spritecollideany(enemy, enemy_group) is not enemy:
                    enemy.kill()
                else:
                    enemy_kol += 1
            if enemy_tick % 100 == 0 and enemy_kol < 150:
                enemy = EnemyMiddle(random.randrange(110, 450), 10)
                if pygame.sprite.spritecollideany(enemy, enemy_group) \
                        and pygame.sprite.spritecollideany(enemy, enemy_group) is not enemy:
                    enemy.kill()
                else:
                    enemy_kol += 1
            if enemy_tick % 150 == 0 and enemy_kol < 150:
                enemy = EnemyHard(random.randrange(110, 450), 10)
                if pygame.sprite.spritecollideany(enemy, enemy_group) \
                        and pygame.sprite.spritecollideany(enemy, enemy_group) is not enemy:
                    enemy.kill()
                else:
                    enemy_kol += 1
        if f1 == 1 and player.rect.x > 110:
            player.rect.x -= 5
        elif f1 == 2 and player.rect.x < 460:
            player.rect.x += 5
        if f2 == 1:
            f2_tick += 1
        if f2_tick != 0 and f2_tick % 8 == 0:
            ball = Ball(5, player.rect.x + 10, player.rect.y)
            if pygame.sprite.spritecollideany(ball, ball_group) \
                    and pygame.sprite.spritecollideany(ball, ball_group) is not ball:
                ball.kill()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    f1 = 2
                if event.key == pygame.K_LEFT:
                    f1 = 1
                if event.key == pygame.K_SPACE:
                    f2 = 1
                    Ball(5, player.rect.x + 10, player.rect.y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    f1 = 0
                if event.key == pygame.K_SPACE:
                    f2 = 0
                    f2_tick = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 90 > event.pos[0] > 10 and 500 > event.pos[1] > 450:
                    st = 1
        screen.fill((0, 0, 0))
        if first_time_game_start == 1:
            all_sprites.add(Quit())
            all_sprites.add(Level())
            first_time_game_start = 0
        pygame.draw.rect(screen, (50, 50, 50), (0, 0, 110, 500))
        pygame.draw.line(screen, (255, 255, 255), (10, 50), (100, 50))
        font = pygame.font.SysFont('comicsansms', 28)
        text = font.render(str(level), 1, (255, 255, 255))
        text_x = 55 - text.get_width() // 2
        screen.blit(text, (text_x, 105))
        hearts_group.empty()
        hearts_margin = (90 - hearts_kol * 30) // (hearts_kol + 1)
        for i in range(1, hearts_kol + 1):
            Heart(hearts_margin * i + 30 * i - 20, 10)
        hearts_group.draw(screen)
        all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
