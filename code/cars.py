import pyglet
from pyglet import sprite, image
from pyglet.window import key

from math import sin, cos, atan, radians, sqrt

window = pyglet.window.Window(width=2280, height=1580, caption="Images")

logo_image = image.load("images/track V4.png")
car_image = image.load("images/car.png")

car_image.anchor_x = car_image.width // 2
car_image.anchor_y = car_image.height // 2

line = pyglet.shapes.Line(x=200, y=900, x2=300, y2=800, width = 1)
line1 = pyglet.shapes.Line(x=300, y=800, x2=400, y2=600, width = 1)
line2 = pyglet.shapes.Line(x=400, y=600, x2=700, y2=1000, width = 1)
line3 = pyglet.shapes.Line(x=700, y=1000, x2=100, y2=800, width = 1)

line_list = [line, line1, line2, line3]

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
              
  

logo = sprite.Sprite(logo_image, x=1, y=1)
car = sprite.Sprite(car_image, x=40, y=900)
car.scale = 0.1
logo.scale = 3
car.rotation = 1

#these are constant values - having them as callable variables should make the update function faster
half_width_car = car_image.width // 20
half_height_car = car_image.height // 20
h = sqrt(half_width_car**2 + half_height_car**2)
angle = atan(half_width_car/half_height_car) - radians(car.rotation)

sprite_hitbox = [(0,0),(0,0),(0,0),(0,0)]

forward = False
backward = False
aclockwise = False
clockwise = False

drift = False
backDict = {}
collList = []

velocity = 0
max_velocity = 8
friction = 0.07
acceleration = 0.1
rotation_speed = 3

drift_time = 8
rounds = 0

@window.event
def on_draw():
  window.clear()
  logo.draw()
  car.draw()
  line.draw()
  line1.draw()
  line2.draw()
  line3.draw()
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