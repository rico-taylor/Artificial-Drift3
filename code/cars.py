import pyglet
from pyglet import sprite, image
from pyglet.window import key, mouse

from math import sin, cos, atan, radians, sqrt

window = pyglet.window.Window(caption="Images")
window.set_fullscreen(True)

lines = pyglet.graphics.Batch()

track_image = image.load("images/track V4.png")
car_image = image.load("images/car.png")

car_image.anchor_x = car_image.width // 2
car_image.anchor_y = car_image.height // 2

line = pyglet.shapes.Line(x=472, y=23, x2=1723, y2=217, width = 1, batch = lines)
line1 = pyglet.shapes.Line(x=1723, y=217, x2=1777, y2=295, width = 1, batch = lines)
line2 = pyglet.shapes.Line(x=1777, y=295, x2=1764, y2=392, width = 1, batch = lines)
line3 = pyglet.shapes.Line(x=1764, y=392, x2=1704, y2=459, width = 1, batch = lines)
line4 = pyglet.shapes.Line(x=1704, y=459, x2=1580, y2=510, width = 1, batch = lines)
line5 = pyglet.shapes.Line(x=1580, y=510, x2=1562, y2=548, width = 1, batch = lines)
line6 = pyglet.shapes.Line(x=1562, y=548, x2=1571, y2=584, width = 1, batch = lines)
line7 = pyglet.shapes.Line(x=1571, y=584, x2=1707, y2=690, width = 1, batch = lines)
line8 = pyglet.shapes.Line(x=1707, y=690, x2=1765, y2=800, width = 1, batch = lines)
line9 = pyglet.shapes.Line(x=1765, y=800, x2=1760, y2=901, width = 1, batch = lines)
line10 = pyglet.shapes.Line(x=1760, y=901, x2=1696, y2=984, width = 1, batch = lines)
line11 = pyglet.shapes.Line(x=1696, y=984, x2=1632, y2=1021, width = 1, batch = lines)
line12 = pyglet.shapes.Line(x=1632, y=1021, x2=1462, y2=1022, width = 1, batch = lines)
line13 = pyglet.shapes.Line(x=1462, y=1022, x2=1193, y2=906, width = 1, batch = lines)
line14 = pyglet.shapes.Line(x=1193, y=906, x2=892, y2=771, width = 1, batch = lines)
line15 = pyglet.shapes.Line(x=892, y=771, x2=802, y2=777, width = 1, batch = lines)
line16 = pyglet.shapes.Line(x=802, y=777, x2=746, y2=883, width = 1, batch = lines)
line17 = pyglet.shapes.Line(x=746, y=883, x2=711, y2=995, width = 1, batch = lines)
line18 = pyglet.shapes.Line(x=711, y=995, x2=628, y2=1050, width = 1, batch = lines)
line19 = pyglet.shapes.Line(x=628, y=1050, x2=494, y2=1031, width = 1, batch = lines)
line20 = pyglet.shapes.Line(x=494, y=1031, x2=384, y2=964, width = 1, batch = lines)
line21 = pyglet.shapes.Line(x=384, y=964, x2=364, y2=832, width = 1, batch = lines)
line22 = pyglet.shapes.Line(x=364, y=832, x2=462, y2=624, width = 1, batch = lines)
line23 = pyglet.shapes.Line(x=462, y=624, x2=453, y2=555, width = 1, batch = lines)
line24 = pyglet.shapes.Line(x=453, y=555, x2=269, y2=478, width = 1, batch = lines)

line_list = [line, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15, line16, line17, line18, line19, line20, line21, line22, line23, line24]

def overlap_check(car_hitbox, input_lines):
  global collide_x
  global collide_y
  for (x,y) in car_hitbox:
    for input_line in input_lines:
      if min(input_line.x, input_line.x2) < x < max(input_line.x, input_line.x2):
        if min(input_line.y, input_line.y2) < y < max(input_line.y, input_line.y2):
            gradient = (input_line.y2-input_line.y)/(input_line.x2-input_line.x)
            if y - input_line.y -velocity < gradient*(x-input_line.x) < y - input_line.y + velocity:
              return True
              
  

track = sprite.Sprite(track_image, x=200, y=0)
car = sprite.Sprite(car_image, x=40, y=900)
car.scale = 0.1
track.scale = 2.6
car.rotation = 1

#these are constant values - having them as callable variables should make the update function faster
half_width_car = car_image.width // 20
half_height_car = car_image.height // 20
h = sqrt(half_width_car**2 + half_height_car**2)
angle = atan(half_width_car/half_height_car) - radians(car.rotation)

#defining variables, lists, and dictionaries
sprite_hitbox = [(0,0),(0,0),(0,0),(0,0)]
forward = False
backward = False
aclockwise = False
clockwise = False
drift = False
backDict = {}
collList = []
rounds = 0

#tunable variables 
velocity = 0
max_velocity = 8
friction = 0.07
acceleration = 0.1
rotation_speed = 3
drift_time = 8


@window.event
def on_draw():
  window.clear()
  track.draw()
  car.draw()
  lines.draw()
  circle.draw()
  circle1.draw()
  circle2.draw()
  circle3.draw()

@window.event
def on_key_press(symbol, modifiers):
  global forward
  global backward
  global clockwise
  global aclockwise
  global drift
  global rounds
  global rotation_speed
  global max_velocity
  global velocity

  if symbol == key.UP:
    forward = True
  if symbol == key.DOWN:
    backward = True

  if symbol == key.LEFT:
    aclockwise = True
  if symbol == key.RIGHT:
    clockwise = True

  if symbol == key.LSHIFT or symbol == key.RSHIFT:
    drift = True
    max_velocity = 12
    rotation_speed = 3
    rounds = 0

@window.event   
def on_mouse_press(x,y,button, modifiers):
  if button == mouse.LEFT:
    print(x,y)

@window.event
def on_key_release(symbol, modifiers):
  global forward
  global backward
  global clockwise
  global aclockwise
  global drift
  global rotation_speed
  global max_velocity

  if symbol == key.UP:
    forward = False
  if symbol == key.DOWN:
    backward = False
  if symbol == key.LEFT:
    aclockwise = False
  if symbol == key.RIGHT:
    clockwise = False
  if symbol == key.LSHIFT or symbol == key.RSHIFT:
    drift = False
    rotation_speed = 3
    max_velocity = 8

def update(dt):
  global velocity
  global rounds
  global sprite_hitbox
  global circle
  global circle1
  global circle2
  global circle3
  global drift


  if velocity > 0:
    velocity -= friction
  if velocity < 0:
    velocity += friction
  if velocity > max_velocity:
    velocity = max_velocity #maybe remvoe this for drift or find some way without
  if velocity < -max_velocity:
    velocity = -max_velocity

  if forward == True and overlap_check(sprite_hitbox, line_list) != True:
    velocity += acceleration
  if backward == True and overlap_check(sprite_hitbox, line_list) != True:
    velocity -= acceleration

  new = (car.x, car.y)
  collList.append(new)
  if len(collList) > 13:
    del collList[0]

  if overlap_check(sprite_hitbox,line_list) == True:
    car.x, car.y = collList[int(-velocity//3)-2]
    drift = False
    velocity = 0
  
  dy = velocity * cos(radians(car.rotation))
  dx = velocity * sin(radians(car.rotation))
  
  new = {dy:dx}
  backDict.update(new)
  if len(backDict) > drift_time:
    backDict.pop(list(backDict)[0])
  
  circle = pyglet.shapes.Circle(x=h*cos(1.57 +atan(half_width_car/half_height_car) - radians(car.rotation)) + car.x, y=h*sin(1.57 +atan(half_width_car/half_height_car) - radians(car.rotation)) + car.y, radius=1, color=(255,255,255))
  circle1 = pyglet.shapes.Circle(x=h*cos(1.57 -atan(half_width_car/half_height_car) - radians(car.rotation)) + car.x, y=h*sin(1.57 -atan(half_width_car/half_height_car) - radians(car.rotation)) + car.y, radius=1, color=(255,255,255))
  circle2 = pyglet.shapes.Circle(x=h*cos(4.71 -atan(half_width_car/half_height_car) - radians(car.rotation)) + car.x, y=h*sin(4.71 -atan(half_width_car/half_height_car) - radians(car.rotation)) + car.y, radius=1, color=(255,255,255))
  circle3 = pyglet.shapes.Circle(x=h*cos(-1.57 +atan(half_width_car/half_height_car) - radians(car.rotation)) + car.x, y=h*sin(-1.57 +atan(half_width_car/half_height_car) - radians(car.rotation)) + car.y, radius=1, color=(255,255,255))
  
  sprite_top_left = (h*cos(1.57 +angle) + car.x, h*sin(1.57 +angle) + car.y)
  sprite_top_right = (h*cos(1.57 - angle) + car.x, h*sin(1.57 - angle) + car.y)
  sprite_bottom_left = (h*cos(4.71 -angle) + car.x, h*sin(4.71 -angle) + car.y)
  sprite_bottom_right = (h*cos(-1.57 + angle) + car.x, h*sin(-1.57 + angle) + car.y)

  sprite_hitbox = [sprite_top_left,sprite_top_right,sprite_bottom_left,sprite_bottom_right ]
  
  rounds += 1
  if drift == True:
    if rounds >= drift_time:
      car.y += list(backDict)[0]
      car.x += backDict[list(backDict)[1]]
    else:
      car.y += dy
      car.x += dx
  else:
    car.y += dy
    car.x += dx
  
  if forward == True or backward == True or velocity > friction or velocity < -friction:
    if aclockwise == True:
      car.rotation -= rotation_speed
    if clockwise == True:
      car.rotation += rotation_speed
  
  

pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()