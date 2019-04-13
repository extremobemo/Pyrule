import pygame,random,math
from pygame.locals import *


TreeImg = pygame.image.load("assets/overworld/trees.png")
TreeImg2 = pygame.image.load("assets/overworld/single_trees.png")
TreeImg3 = pygame.image.load("assets/overworld/single_tree.png")
RockImg = pygame.image.load("assets/overworld/rocks.png")
DestRock = pygame.image.load("assets/overworld/explodable_rocks.png")
Oldie = pygame.image.load("assets/misc/old_man.png")
dungeon_rock = pygame.image.load("assets/overworld/dungeon_rocks.png")
Water1 = pygame.image.load("assets/overworld/water.png")
Water2 = pygame.image.load("assets/overworld/water_right.png")
Water3 = pygame.image.load("assets/overworld/water_right_inverse.png")


class Room(object):
    wall_list = None
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.mob_list = pygame.sprite.Group()
        self.arrows = pygame.sprite.Group()
        self.item_list = pygame.sprite.Group()
        self.door_list = pygame.sprite.Group()
        self.door_list2 = pygame.sprite.Group()
        self.door_list3 = pygame.sprite.Group()
        self.key_list = pygame.sprite.Group()
        self.lock_list = pygame.sprite.Group()
        self.bombs_items_list = pygame.sprite.Group()
        self.dungeon = False
    def populate(self, lst, type):
        if type == "wall":
            self.wall_list = pygame.sprite.Group(lst)
        if type == "door":
            self.door_list = pygame.sprite.Group(lst)
        if type == "key":
            self.key_list = pygame.sprite.Group(lst)
        if type == "mob":
            self.mob_list = pygame.sprite.Group(lst)



class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.destructible = False
class Rock(pygame.sprite.Sprite):
    def __init__(self,x,y,destructible,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = RockImg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.destructible = destructible
        self.image = image

    def __str__(self):
        return "I am a rock", self.destructible
class DungeonRock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = dungeon_rock
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.destructible = False

class Water(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.destructible = False

class Door(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/link/walk_right1.png")
        self.rect = self.image.get_rect()
        self.image.fill(Color("Black"))
        self.rect.x = x
        self.rect.y = y
        self.destructible = False
class Sword(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("0.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class BombCollectable(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/Bombs/bombs.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Text(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/Alone.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Key(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/misc/key.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Lock(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/misc/lock.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Mob(pygame.sprite.Sprite):
    def __init__(self,x,y,hitpoint,game):
        self.left1 = pygame.image.load("assets/meanie/0.png")
        self.left2 = pygame.image.load("assets/meanie/1.png")
        self.down1 = pygame.image.load("assets/meanie/2.png")
        self.down2 = pygame.image.load("assets/meanie/3.png")
        self.right1 = pygame.image.load("assets/meanie/4.png")
        self.right2 = pygame.image.load("assets/meanie/5.png")
        self.up1 = pygame.image.load("assets/meanie/6.png")
        self.up2 = pygame.image.load("assets/meanie/7.png")
        self.left_walk = [self.left1,self.left2]
        self.right_walk = [self.right1, self.right2]
        self.up_walk = [self.up1, self.up2]
        self.down_walk = [self.down1, self.down2]
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect(0,0,48,48)
        self.image = pygame.image.load("assets/meanie/0.png")
        self.rect.x = x
        self.rect.y = y
        self.one = pygame.image.load("assets/misc/0.png")
        self.two = pygame.image.load("assets/misc/1.png")
        self.three= pygame.image.load("assets/misc/2.png")
        self.die = [self.one,self.two,self.three]
        self.ticker = 0
        self.current_frame = 0
        self.walk_anim_frame = 0
        self.hitpoint = hitpoint
        self.x_change = 1
        self.t = 0
        self.timer = random.randint(60,180)
        self.arrow_timer = random.randint(0,120)
        self.arrow_t = 0
        self.randomDirections = ["up", "down","left","right"]
        self.randomnumber = random.randint(0,3)
        self.direction = self.randomDirections[self.randomnumber]
        self.walls = None
        self.doors = None
        self.x_change = 1
        self.y_change = 1
        self.anim_ticker = 0
        self.game = game
        self.effect = pygame.mixer.Sound("LoZ_Sounds/LOZ_Kill.wav")
        self.effect.set_volume(.4)
        self.has_bomb = True

    def update(self):
        if self.direction == "right":
            self.image = self.right_walk[self.walk_anim_frame]
            self.rect.x += self.x_change
            wall_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for wall in wall_hit_list:
                self.rect.right = wall.rect.left
                self.direction = self.randomDirections[2]
            self.t += 1
            if self.arrow_t >= self.arrow_timer:
                self.game.arrows.add(Mob_Arrow(self.rect.x, self.rect.y, self.direction))
                self.arrow_t = 0
                self.arrow_timer = random.randint(60,240)
            self.arrow_t += 1
            if self.t == self.timer:
              self.direction = self.randomDirections[random.randint(0,3)]
              self.t = 0

        elif self.direction == "left":
            self.image = self.left_walk[self.walk_anim_frame]
            self.rect.x -= self.x_change
            wall_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for wall in wall_hit_list:
                self.rect.left = wall.rect.right
                self.direction = self.randomDirections[3]
            self.t += 1
            self.arrow_t += 1
            if self.arrow_t >= self.arrow_timer:
                self.game.arrows.add(Mob_Arrow(self.rect.x, self.rect.y, self.direction))
                self.arrow_t = 0
                self.arrow_timer = random.randint(60,240)
            if self.t == self.timer:
                self.direction = self.randomDirections[random.randint(0,3)]
                self.t = 0
        elif self.direction == "up":
            self.image = self.up_walk[self.walk_anim_frame]
            self.rect.y -= self.y_change
            wall_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for wall in wall_hit_list:
                self.rect.top = wall.rect.bottom
                self.direction = self.randomDirections[1]

            self.t += 1
            self.arrow_t += 1
            if self.arrow_t >= self.arrow_timer:
                self.game.arrows.add(Mob_Arrow(self.rect.x, self.rect.y, self.direction))
                self.arrow_t = 0
                self.arrow_timer = random.randint(60,240)
            if self.t == self.timer:
                self.direction = self.randomDirections[random.randint(0,3)]
                self.t = 0

        elif self.direction == "down":
            self.image = self.down_walk[self.walk_anim_frame]
            self.rect.y += self.y_change
            wall_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for wall in wall_hit_list:

                self.rect.bottom = wall.rect.top
                self.direction = self.randomDirections[0]
            self.t += 1
            self.arrow_t += 1
            if self.arrow_t >= self.arrow_timer:
                self.game.arrows.add(Mob_Arrow(self.rect.x, self.rect.y, self.direction))
                self.arrow_t = 0
                self.arrow_timer = random.randint(60,240)
            if self.t == self.timer:
                self.direction = self.randomDirections[random.randint(0,3)]
                self.t = 0


        if self.hitpoint <= 0:
            self.arrow_t = -1
            self.x_change = 0
            self.y_change = 0
            self.rect.y = self.rect.y
            self.image = self.die[self.current_frame]
            self.ticker += 1
            if self.ticker % 15 == 0:
                self.current_frame = (self.current_frame + 1) % 3
            if self.image == self.die[2]:
                self.kill()
                self.effect.play()

        self.anim_ticker += 1
        if self.anim_ticker % 10 == 0:
            self.walk_anim_frame = (self.walk_anim_frame + 1) % 2



class Mob_Arrow(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        if self.direction == "right":
            self.image = pygame.image.load("assets/meanie/arrow/2.png")
        elif self.direction == "left":
            self.image = pygame.image.load("assets/meanie/arrow/0.png")
        elif self.direction == "up":
            self.image = pygame.image.load("assets/meanie/arrow/3.png")
        elif self.direction == "down":
            self.image = pygame.image.load("assets/meanie/arrow/1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.direction == "right":
            self.rect.x += 6
        elif self.direction == "left":
            self.rect.x -= 6
        elif self.direction == "up":
            self.rect.y -= 6
        elif self.direction == "down":
            self.rect.y += 6
