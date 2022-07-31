from recourses import *
import random
import time


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