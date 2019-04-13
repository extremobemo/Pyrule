from room_template import *

def build_room_1():
    room1 = Room()

    room1.walls = [Wall(0,0,TreeImg), Wall(256,0,TreeImg),Wall(500,0,TreeImg), Wall((900-256),0,TreeImg), Wall(-160,113,TreeImg),
             Wall(-160,226,TreeImg),Wall(-160,440,TreeImg), Wall(-160, 553,TreeImg),
             Wall((900-150),113,TreeImg),Wall((900-150),226,TreeImg), Water((800-216),443, Water1),Wall(700,0,TreeImg),
             Wall(75,553,TreeImg),Wall(200,553,TreeImg),Wall(330,553,TreeImg)]

    room1.doors = [Door(300,66)]
    room1.populate(room1.walls, "wall")
    print(room1.walls)
    room1.populate(room1.doors, "door")
    return room1
