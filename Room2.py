from room_template import *

def build_room_1():
    room2 = Room()

    walls = [Water(0,443, Water2),Wall(213,500,TreeImg), Wall(326,500,TreeImg),
             Rock(0,0,False,RockImg),Rock(-500,120,False,RockImg),Rock(-500,200,False,RockImg), Wall(439,500,TreeImg),Wall(551,500,TreeImg),
             Wall(750,0,TreeImg),Wall(750, 339,TreeImg),Wall(750,451,TreeImg),Wall(750,113,TreeImg),
              Wall(750,226,TreeImg)]
    mobs = [Mob(400,200,5,self),Mob(500,300,5,self),Mob(500,400,5,self)]
    self.keys = [Key(300,300)]

    room1.populate(room2.walls, "wall")
    room2.populate(room2.mobs, "mob")
    room1.populate(room2.keys, "key")
    return room2
