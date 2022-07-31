import sys
import time
import pygame
import os
import random

main_folder = os.path.dirname(__file__)

fon_image = pygame.image.load(os.path.join(main_folder, "images/Fon1.png"))
no_image = pygame.image.load(os.path.join(main_folder, "images/no.png"))
yes_image = pygame.image.load(os.path.join(main_folder, "images/yes.png"))
exit_image = pygame.image.load(os.path.join(main_folder, "images/exit.jpg"))
poison_good = pygame.image.load(os.path.join(main_folder, "images/poison_+10.gif"))
poison_bad = pygame.image.load(os.path.join(main_folder, "images/poison_-10.gif"))
mushroom = pygame.image.load(os.path.join(main_folder, "images/mushroom.gif"))
key_x3 = pygame.image.load(os.path.join(main_folder, "images/keyx3.gif"))
key_x5 = pygame.image.load(os.path.join(main_folder, "images/keyx5.gif"))
key_x2 = pygame.image.load(os.path.join(main_folder, "images/keyx2.gif"))
strawberry = pygame.image.load(os.path.join(main_folder, "images/straw.gif"))
main_poze = pygame.image.load(os.path.join(main_folder, "images/main_poze.png"))
left_poze1 = pygame.image.load(os.path.join(main_folder, "images/left_poze1.png"))
left_poze2 = pygame.image.load(os.path.join(main_folder, "images/left_poze2.png"))
left_poze3 = pygame.image.load(os.path.join(main_folder, "images/left_poze3.png"))
right_poze1 = pygame.image.load(os.path.join(main_folder, "images/right_poze1.png"))
right_poze2 = pygame.image.load(os.path.join(main_folder, "images/right_poze2.png"))
right_poze3 = pygame.image.load(os.path.join(main_folder, "images/right_poze3.png"))
game_image = pygame.image.load(os.path.join(main_folder, "images/background.png"))
play_image = pygame.image.load(os.path.join(main_folder, "images/play_1.png"))
options_image = pygame.image.load(os.path.join(main_folder, "images/sett.jpg"))
options1_image = pygame.image.load(os.path.join(main_folder, "images/sett2.jpg"))
options3_image = pygame.image.load(os.path.join(main_folder, "images/setti3.jpg"))
play_2_image = pygame.image.load(os.path.join(main_folder, "images/play_2.png"))
play_3_image = pygame.image.load(os.path.join(main_folder, "images/play_3.png"))
back_image = pygame.image.load(os.path.join(main_folder, "images/back.png"))
game_over_image = pygame.image.load(os.path.join(main_folder, "images/game_over.gif"))
restart_image = pygame.image.load(os.path.join(main_folder, "images/restart.png"))
button_0 = pygame.image.load(os.path.join(main_folder, "images/0.png"))
button_1 = pygame.image.load(os.path.join(main_folder, "images/1.png"))
button_2 = pygame.image.load(os.path.join(main_folder, "images/2.png"))
button_3 = pygame.image.load(os.path.join(main_folder, "images/3.png"))
button_4 = pygame.image.load(os.path.join(main_folder, "images/4.png"))
button_5 = pygame.image.load(os.path.join(main_folder, "images/5.png"))
button_6 = pygame.image.load(os.path.join(main_folder, "images/6.png"))
button_7 = pygame.image.load(os.path.join(main_folder, "images/7.png"))
button_8 = pygame.image.load(os.path.join(main_folder, "images/8.png"))
button_9 = pygame.image.load(os.path.join(main_folder, "images/9.png"))
button_10 = pygame.image.load(os.path.join(main_folder, "images/10.png"))
button_30 = pygame.image.load(os.path.join(main_folder, "images/30.png"))
button_20 = pygame.image.load(os.path.join(main_folder, "images/20.png"))
button_40 = pygame.image.load(os.path.join(main_folder, "images/40.png"))
button_50 = pygame.image.load(os.path.join(main_folder, "images/50.png"))
button_60 = pygame.image.load(os.path.join(main_folder, "images/60.png"))
button_70 = pygame.image.load(os.path.join(main_folder, "images/70.png"))
button_80 = pygame.image.load(os.path.join(main_folder, "images/80.png"))
button_90 = pygame.image.load(os.path.join(main_folder, "images/90.png"))
button_100 = pygame.image.load(os.path.join(main_folder, "images/100.png"))
button_plus = pygame.image.load(os.path.join(main_folder, "images/+.png"))
button_minus = pygame.image.load(os.path.join(main_folder, "images/-.png"))
SHIRINA = 1920
VISOTA = 1040
volume_buttons = [button_0, button_10, button_20, button_30, button_40, button_50, button_60, button_70, button_80,
                  button_90, button_100]
point_value = [button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]
player_points = 0


class Numbers(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.pos = pos

    def update_volume(self, image):
        self.image = image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos


class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.pos = pos

    def update(self, pic1, pic2):
        ran_color = random.randint(1, 2)
        if ran_color == 1:
            self.image = pic1
        if ran_color == 2:
            self.image = pic2
        time.sleep(0.2)

    def set_color(self, back_color):
        self.image.set_colorkey(back_color)


class Character(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.direction = 3
        self.points = 0
        self.speed = 20

    def set_bonus(self, bonuses):
        if self.points + bonuses[0] >= 0:
            self.points += bonuses[0]
        self.speed += bonuses[1]
        if self.speed >= 30:
            self.speed = 30
        if self.speed <= 10:
            self.speed = 10

    def update(self):
        if self.direction == 1:
            if self.image == right_poze3:
                self.image = main_poze
            elif self.image == right_poze2:
                self.image = main_poze
            elif self.image == right_poze1:
                self.image = main_poze
            elif self.image == main_poze:
                self.image = left_poze1
            elif self.image == left_poze1:
                self.image = left_poze2
            elif self.image == left_poze2:
                self.image = left_poze3
            elif self.image == left_poze3:
                self.image = left_poze2
            if self.image != main_poze:
                self.rect.x -= self.speed
        elif self.direction == 2:
            if self.image == left_poze1:
                self.image = main_poze
            elif self.image == left_poze2:
                self.image = main_poze
            elif self.image == left_poze3:
                self.image = main_poze
            elif self.image == main_poze:
                self.image = right_poze1
            elif self.image == right_poze1:
                self.image = right_poze2
            elif self.image == right_poze2:
                self.image = right_poze3
            elif self.image == right_poze3:
                self.image = right_poze2
            if self.image != main_poze:
                self.rect.x += self.speed
        else:
            self.image = main_poze
        if self.rect.left <= 0:
            self.image = main_poze
            self.rect.left = 0
        if self.rect.right >= SHIRINA:
            self.image = main_poze
            self.rect.right = SHIRINA

    def move(self, direction):
        self.direction = direction


class Drop_object(pygame.sprite.Sprite):
    def __init__(self, image, pos, speed, points, boosts, timing):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.falling = False
        self.speed = speed
        self.points = points
        self.boosts = boosts
        self.drop_time = time.time()
        self.timing = timing

    def is_falling(self):
        return self.falling

    def get_bonus(self):
        return (self.points, self.boosts)

    def object_caught(self):
        self.falling = False
        self.drop_time = time.time()
        self.rect.center = (-1000, -1000)

    def drop_need(self):
        if time.time() - self.drop_time >= self.timing:
            self.falling = True
            self.rect.bottom = 0
            self.rect.y = random.randint(100, 800) * (-1)
            self.rect.x = random.randint(100, 1820)

    def update(self):
        if self.falling:
            self.rect.y += self.speed
        else:
            self.rect.y = -1000
        if self.rect.y > VISOTA:
            self.falling = False
            self.drop_time = time.time()
            self.rect.y = -1000


def exit():
    exit_images = pygame.sprite.Group()
    yes_button = Button(yes_image, (SHIRINA / 2, VISOTA / 2))
    no_button = Button(no_image, (SHIRINA / 2, VISOTA / 2 + 200))
    exit_button = Button(exit_image, (SHIRINA / 2, VISOTA / 2 - 250))
    exit_images.add(yes_button, no_button, exit_button)
    running = True
    while running:
        screen.blit(fon_image, fon_image.get_rect())
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button.rect.collidepoint(mouse_pos):
                    sys.exit()
                if no_button.rect.collidepoint(mouse_pos):
                    running = False
        exit_images.draw(screen)
        pygame.display.flip()


def ending():
    lose_images = pygame.sprite.Group()
    global player_points
    game_over = Numbers(game_over_image, (SHIRINA / 2, VISOTA / 2 - 250))
    restart = Numbers(restart_image, (SHIRINA / 2, VISOTA / 2 + 400))
    hundreds = Numbers(button_0, (SHIRINA / 2 - 75, VISOTA / 2 - 75 + 300))
    dozens = Numbers(button_0, (SHIRINA / 2, VISOTA / 2 - 75 + 300))
    units = Numbers(button_0, (SHIRINA / 2 + 75, VISOTA / 2 - 75 + 300))
    lose_images.add(game_over, restart, hundreds, dozens, units)
    running = True
    hundred_value = int(player_points // 100)
    dozens_value = int(player_points % 100 // 10)
    units_value = int(player_points % 10)
    hundreds.update_volume(point_value[hundred_value])
    dozens.update_volume(point_value[dozens_value])
    units.update_volume(point_value[units_value])
    while running:
        screen.blit(fon_image, fon_image.get_rect())
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart.rect.collidepoint(mouse_pos):
                    running = False
                    player_points = 0
                    start_game()
        lose_images.draw(screen)
        pygame.display.flip()


def menu():
    buttons = pygame.sprite.Group()
    start_button = Button(play_image, (SHIRINA / 2, VISOTA / 2))
    options_button = Button(options_image, (SHIRINA / 2, VISOTA / 2 + 200))
    buttons.add(start_button, options_button)
    my_sound.play()
    my_sound.set_volume(0.1)
    while True:
        screen.blit(fon_image, fon_image.get_rect())
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(mouse_pos):
                    start_game()
                if options_button.rect.collidepoint(mouse_pos):
                    options()
        if start_button.rect.collidepoint(mouse_pos):
            start_button.update(play_2_image, play_3_image)
        if start_button.rect.collidepoint(mouse_pos) == False:
            start_button.image = play_image
        if options_button.rect.collidepoint(mouse_pos):
            options_button.update(options1_image, options3_image)
        if options_button.rect.collidepoint(mouse_pos) == False:
            options.image = options_image
        buttons.draw(screen)
        pygame.display.flip()


def options():
    options_buttons = pygame.sprite.Group()
    back = Button(back_image, (SHIRINA / 2, VISOTA / 2 - 200))
    volume = Numbers(button_50, (SHIRINA / 2, VISOTA / 2 + 200))
    plus = Button(button_plus, (SHIRINA / 2 + 150, VISOTA / 2 + 200))
    minus = Button(button_minus, (SHIRINA / 2 - 150, VISOTA / 2 + 200))
    plus.set_color((64, 62, 63))
    minus.set_color((64, 62, 63))
    options_buttons.add(back, plus, minus, volume)
    current_volume = 0.5
    options_process = True
    while options_process:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if plus.rect.collidepoint(mouse_pos):
                    if current_volume < 0.99:
                        current_volume += 0.1
                        my_sound.set_volume(current_volume)
                if minus.rect.collidepoint(mouse_pos):
                    if current_volume > 0.09:
                        current_volume -= 0.1
                        my_sound.set_volume(current_volume)
                volume_value = int(round(current_volume * 10))
                volume.update_volume(volume_buttons[volume_value])
                if back.rect.collidepoint(mouse_pos):
                    options_process = False
        screen.blit(fon_image, fon_image.get_rect())
        options_buttons.draw(screen)
        pygame.display.flip()
    for i in options_buttons:
        i.kill()


def start_game():
    sprite_group = pygame.sprite.Group()
    drop_objects = []
    time_start = int(time.time())
    player = Character(main_poze, (SHIRINA / 2, VISOTA / 2 + 250))
    hundreds = Numbers(button_0, (SHIRINA / 2 - 75, 100))
    dozens = Numbers(button_0, (SHIRINA / 2, 100))
    units = Numbers(button_0, (SHIRINA / 2 + 75, 100))
    seconds_dozens = Numbers(button_8, (SHIRINA / 2, 950))
    seconds_units = Numbers(button_0, (SHIRINA / 2 + 65, 950))
    seconds_hundreds = Numbers(button_1, (SHIRINA / 2 - 65, 950))
    drop_strawberry = Drop_object(strawberry, (SHIRINA / 2, 0), 10, 1, 0, 3)
    drop_mushroom = Drop_object(mushroom, (SHIRINA / 2, 0), 10, -3, 0, 3)
    drop_key_x2 = Drop_object(key_x2, (SHIRINA / 2, 0), 15, 2, 0, 5)
    drop_key_x3 = Drop_object(key_x3, (SHIRINA / 2, 0), 25, 3, 0, 5)
    drop_key_x5 = Drop_object(key_x5, (SHIRINA / 2, 0), 30, 5, 0, 9)
    drop_poison_good = Drop_object(poison_good, (SHIRINA / 2, 0), 20, -1, 10, 4)
    drop_poison_bad = Drop_object(poison_bad, (SHIRINA / 2, 0), 15, -5, -10, 6)
    pygame_clock = pygame.time.Clock()
    sprite_group.add(player, drop_strawberry, drop_poison_good, drop_mushroom, drop_poison_bad, drop_key_x2,
                     drop_key_x5, drop_key_x3, hundreds, dozens, units, seconds_dozens, seconds_units, seconds_hundreds)
    drop_objects.extend([drop_strawberry, drop_poison_good, drop_mushroom, drop_poison_bad, drop_key_x2,
                         drop_key_x5, drop_key_x3])
    running = True
    while running:
        current_time = int(time.time())
        pygame_clock.tick(30)
        screen.blit(game_image, game_image.get_rect())
        for i in drop_objects:
            if not i.is_falling():
                i.drop_need()
            if pygame.sprite.collide_rect(player, i):
                i.object_caught()
                player.set_bonus(i.get_bonus())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_a:
                    player.move(1)
                elif event.key == pygame.K_d:
                    player.move(2)
                elif event.key == pygame.K_s:
                    player.move(3)
        seconds_hundreds_value = int((180 - (current_time - time_start)) // 100)
        seconds_dozens_value = int((180 - (current_time - time_start)) % 100 // 10)
        seconds_units_value = int((180 - (current_time - time_start)) % 10)
        seconds_hundreds.update_volume(point_value[seconds_hundreds_value])
        seconds_dozens.update_volume(point_value[seconds_dozens_value])
        seconds_units.update_volume(point_value[seconds_units_value])
        hundred_value = int(player.points // 100)
        dozens_value = int(player.points % 100 // 10)
        units_value = int(player.points % 10)
        hundreds.update_volume(point_value[hundred_value])
        dozens.update_volume(point_value[dozens_value])
        units.update_volume(point_value[units_value])
        sprite_group.update()
        sprite_group.draw(screen)
        pygame.display.flip()
        if 15 - (current_time - time_start) <= 0:
            global player_points
            player_points = player.points
            running = False
            ending()


pygame.init()
pygame.mixer.init()
my_sound = pygame.mixer.Sound("music/223475.mp3")
screen = pygame.display.set_mode((SHIRINA, VISOTA))
pygame.display.set_caption("DropGame")
if __name__ == '__main__':
    menu()