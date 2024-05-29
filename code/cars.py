#NOTE: 
#need to fix that if you drive backwards you go straight through the barrier
import pyglet
from pyglet import sprite, image
from pyglet.window import key, mouse
from math import sin, cos, atan, radians, sqrt, tanh

window = pyglet.window.Window(caption="Images")
window.set_fullscreen(True)

lines = pyglet.graphics.Batch()

#track_image = image.load("images/track V4.png")
car_image = image.load("images/car.png")

car_image.anchor_x = car_image.width // 2
car_image.anchor_y = car_image.height // 2

#outside lines
line = pyglet.shapes.Line(x=472, y=23, x2=1723, y2=217, width = 1, batch = lines)
line1 = pyglet.shapes.Line(x=1723, y=217, x2=1777, y2=295, width = 1, batch = lines)
line2 = pyglet.shapes.Line(x=1777, y=295, x2=1764, y2=392, width = 1, batch = lines, color = (255,0,255))
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
line25 = pyglet.shapes.Line(x=269, y=478, x2=211, y2=370, width = 1, batch = lines)
line26 = pyglet.shapes.Line(x=211, y=370, x2=207, y2=245, width = 1, batch = lines, color = (255,0,255))
line27 = pyglet.shapes.Line(x=207, y=245, x2=278, y2=98, width = 1, batch = lines)
line28 = pyglet.shapes.Line(x=278, y=98, x2=355, y2=36, width = 1, batch = lines)
line29 = pyglet.shapes.Line(x=355, y=36, x2=472, y2=23, width = 1, batch = lines)

#inside lines
line30 = pyglet.shapes.Line(x=470, y=181, x2=1525, y2=325, width = 1, batch = lines)
line31 = pyglet.shapes.Line(x=1525, y=325, x2=1526, y2=363, width = 1, batch = lines, color = (255,0,255))
line32 = pyglet.shapes.Line(x=1526, y=363, x2=1383, y2=435, width = 1, batch = lines)
line33 = pyglet.shapes.Line(x=1383, y=435, x2=1354, y2=554, width = 1, batch = lines)
line34 = pyglet.shapes.Line(x=1354, y=554, x2=1414, y2=644, width = 1, batch = lines)
line35 = pyglet.shapes.Line(x=1414, y=644, x2=1569, y2=758, width = 1, batch = lines)
line36 = pyglet.shapes.Line(x=1569, y=758, x2=1596, y2=838, width = 1, batch = lines)
line37 = pyglet.shapes.Line(x=1596, y=838, x2=1545, y2=891, width = 1, batch = lines)
line38 = pyglet.shapes.Line(x=1545, y=891, x2=1457, y2=882, width = 1, batch = lines)
line39 = pyglet.shapes.Line(x=1457, y=882, x2=969, y2=639, width = 1, batch = lines)
line40 = pyglet.shapes.Line(x=969, y=639, x2=801, y2=629, width = 1, batch = lines)
line41 = pyglet.shapes.Line(x=801, y=629, x2=676, y2=676, width = 1, batch = lines)
line42 = pyglet.shapes.Line(x=676, y=676, x2=618, y2=739, width = 1, batch = lines)
line43 = pyglet.shapes.Line(x=618, y=739, x2=585, y2=793, width = 1, batch = lines)
line44 = pyglet.shapes.Line(x=585, y=793, x2=581, y2=848, width = 1, batch = lines)
line45 = pyglet.shapes.Line(x=581, y=848, x2=566, y2=864, width = 1, batch = lines)
line46 = pyglet.shapes.Line(x=566, y=864, x2=555, y2=854, width = 1, batch = lines)
line47 = pyglet.shapes.Line(x=555, y=854, x2=554, y2=840, width = 1, batch = lines)
line48 = pyglet.shapes.Line(x=554, y=840, x2=581, y2=785, width = 1, batch = lines)
line49 = pyglet.shapes.Line(x=581, y=785, x2=608, y2=697, width = 1, batch = lines)
line50 = pyglet.shapes.Line(x=608, y=697, x2=612, y2=548, width = 1, batch = lines)
line51 = pyglet.shapes.Line(x=612, y=548, x2=565, y2=452, width = 1, batch = lines)
line52 = pyglet.shapes.Line(x=565, y=452, x2=440, y2=399, width = 1, batch = lines)
line53 = pyglet.shapes.Line(x=440, y=399, x2=400, y2=364, width = 1, batch = lines)
line54 = pyglet.shapes.Line(x=400, y=364, x2=383, y2=277, width = 1, batch = lines, color = (255,0,255))
line55 = pyglet.shapes.Line(x=383, y=277, x2=404, y2=217, width = 1, batch = lines)
line56 = pyglet.shapes.Line(x=404, y=217, x2=470, y2=181, width = 1, batch = lines)

line_list = [line, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15, line16, line17, line18, line19, line20, line21, line22, line23, line24, line25, line26, line27, line28, line29, line30, line31, line32, line33, line34, line35, line36, line37, line38, line39, line40, line41, line42, line43, line44, line45, line46, line47, line48, line49, line50, line51, line52, line53, line54, line55, line56]

def overlap_check(car_hitbox, input_lines):
  global collide_x
  global collide_y
  for (x,y) in car_hitbox:
    for input_line in input_lines:
      if min(input_line.x, input_line.x2) < x < max(input_line.x, input_line.x2):
        if min(input_line.y, input_line.y2) < y < max(input_line.y, input_line.y2):
            
            gradient = (input_line.y2-input_line.y)/(input_line.x2-input_line.x)
            input_line.color = (0,255,255)
            if abs(gradient) > 12:
              new_velocity = (tanh(velocity)*2+1)**12
            elif abs(gradient) < 1:
              new_velocity = (tanh(velocity)*2+1)**((abs(gradient)+1)**2)
            else:
              new_velocity = (tanh(velocity)*2+1)**abs(gradient)
            if velocity > 0:
              if y - input_line.y -new_velocity < gradient*(x-input_line.x) < y - input_line.y + new_velocity:
                return True
            #if velocity < 0:
              #if y - input_line.y -velocity > gradient*(x-input_line.x) > y - input_line.y + velocity:
                #return True
              

#track = sprite.Sprite(track_image, x=200, y=0)
car = sprite.Sprite(car_image, x=1020, y=185)
car.scale = 0.1
#track.scale = 2.6
car.rotation = 260

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
  #track.draw()
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
    if len(backDict) > drift_time:
      drift = True
      max_velocity = 11
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