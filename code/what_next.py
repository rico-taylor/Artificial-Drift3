#importing variables
import pyglet
import time
import random
from pyglet import sprite, image
from pyglet.window import key, mouse
from math import sin, cos, atan, acos, asin, radians, sqrt, tanh

#main window
window = pyglet.window.Window(resizable = False, caption="Artificial Drift")
window.set_fullscreen(True)

#showing what window is on
windowOn = [1,0]

#scaling so that all screen sizes can play
scale_factor = (window.width/1920)%1

#defining batches
lines = pyglet.graphics.Batch()
displays = pyglet.graphics.Batch()
entryDisplay = pyglet.graphics.Batch()
aiLines = pyglet.graphics.Batch()

#entry images
#logo
logo_img = image.load("images/logo_finished.png")
logo_img.anchor_x = logo_img.width//2
logo_img.anchor_y = logo_img.height//2
logo = sprite.Sprite(logo_img, x=window.width//2, y=window.height//2 +100, batch=entryDisplay)
logo.scale = scale_factor

#play button
play_img = image.load("images/text_play.png")
play_img.anchor_x = play_img.width//2
play_img.anchor_y = play_img.height//2
playButton = sprite.Sprite(play_img, x=window.width//2, y=window.height//2 -200, batch=entryDisplay)
playButton.scale = 0.5*scale_factor

#triangle decoration
triangle_img = image.load("images/triangle1_translucent.png")
triangle_img.anchor_x = triangle_img.width//2
triangle_img.anchor_y = triangle_img.height//2
triangle1 = sprite.Sprite(triangle_img, x=100, y=100, batch=entryDisplay)
triangle1.rotation = 30
triangle1.scale = 0.3*scale_factor

#AI specific code
lineLength = 100000000
reward_gate = False
wall_collision = False
new_gate_signal = False
oldCollisionPointsList = [(car_start_x,car_start_y),(car_start_x,car_start_y),(car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y)]


aiVisionList = []

#AI vision function - checks line overlaps
def aiVision():
    intersectList = []
    for line in viewingLineList:
        overlapList = []
        for barrier in barrierLineList:
            overlapPoint = find_intersection(line, barrier)
            if overlapPoint is not None:
                overlapList.append(overlapPoint)

        if overlapList:
            smallest = min(overlapList, key=lambda t: t[2])
            intersectList.append((smallest[0], smallest[1]))
    return intersectList
         
#function for displaying the number of laps completed
def lap_displays():
  global lap_list
  for x in lap_list:
    text = pyglet.text.Label("Lap " +str(lap_list.index(x)+1) + ": " +str(x), font_size=20, x=50, y=700-50*lap_list.index(x), batch=displays)
    text.draw()

#leader code
def highestGate(listt):
  loops = 0
  biggest = 0
  for x in listt:
    loops += 1
    if x == True:
      biggest = loops
  return biggest

old_leader = "Orange"
def leader():
  global old_leader
  if len(lap_list) > len(lap_list2):
    old_leader = "Orange"
    return "Orange"
  elif len(lap_list2) > len(lap_list):
    old_leader = "White"
    return "White"
  else:
    if highestGate(checkerList) > highestGate(checkerList2):
      old_leader = "Orange"
      return "Orange"
    elif highestGate(checkerList) < highestGate(checkerList2):
      old_leader = "White"
      return "White"
    else:
      return old_leader

#AI reward function
def reward():
  global reward_gate
  global wall_collision
  global new_gate_signal
  reward = 0
  if reward_gate == True and new_gate_signal == True:
    reward += 10
  if wall_collision == True:
    reward -= 15

  new_gate_signal = False
  reward_gate = False
  wall_collision = False

  return reward

#AI reset function
def reset(): #making this in a class will make it easy to reset both of the cars.
  global respawnLine
  global timerLineList

  #TOTAL VARIABLE RESET
  global forward, backward, aclockwise, clockwise, drift, backDict, collList, rounds, lapCompleted
  global velocity, max_velocity, friction, acceleration, rotation_speed, drift_time
  global going, start, current, elapsed, swap, started, lap_list, checkerList
  global reward_gate, wall_collision, new_gate_signal

  forward = False
  backward = False
  aclockwise = False
  clockwise = False
  drift = False
  backDict = {}
  collList = []
  rounds = 0

  lapCompleted = False

  #tunable variables 
  velocity = 0 *scale_factor
  max_velocity = 8 *scale_factor
  friction = 0.07 *scale_factor
  acceleration = 0.1 *scale_factor
  rotation_speed = 3
  drift_time = 8 *scale_factor

  #timer code
  going = False
  start = 0
  current= 0
  elapsed = 0
  swap = False
  started = False

  lap_list = []

  #AI specific code
  reward_gate = False
  wall_collision = False
  new_gate_signal = False

  #respawning the car at a random midpoint of a reward gate
  respawnLine = random.choice(timerLineList)
  car.x, car.y = midpoint(respawnLine)

  for x in range(timerLineList.index(respawnLine)):
    timerLineList.append(timerLineList[0])
    del timerLineList[0]

  for x in range(len(checkerList)):
    checkerList[x] = False
  
  #getting the car rotation for the respawn
  a,b = midpoint(respawnLine)
  c,d = midpoint(timerLineList[(timerLineList.index(respawnLine)+1)%len(timerLineList)])
  dist = distance_points((a,b), (c,d))
  vertical_height = d-b
  ang = (180/3.141)*asin(abs(vertical_height)/dist)
  if vertical_height > 0:
    if grad_points((a,b), (c,d)) > 0: #first quadrant (GOOD)
      car.rotation = 90 - ang
    else: #second quadrant (BAD)
      car.rotation = 270 + ang
  else:
    if grad_points((a,b), (c,d)) > 0: #third quadrant (GOOD)
      car.rotation = 270 - ang
    else: #fourth quadrant (BAD)
      car.rotation = 90 + ang



@window.event
def on_draw():
  window.clear()

  if windowOn[0] == 1:
    entryDisplay.draw()
  if windowOn[1] == 1:
    displays.draw()
    #lap_displays() this function is commented out since it was causing lag
    car.draw()
    car2.draw()
    lines.draw()
    aiLines.draw()
    
    circle.draw()
    circle1.draw()
    circle2.draw()
    circle3.draw()

    circle4.draw()
    circle5.draw()
    circle6.draw()
    circle7.draw()


@window.event   
def on_mouse_press(x,y,button, modifiers):
  global windowOn
  if button == mouse.LEFT:
    if windowOn == [1,0]:
      windowOn = [0,1]
    print(x,y)
    print(lap_list)
    print(lap_list2)
    reset()

def update(dt):
  #display code
  global timeTaken
  global laps
  global leaderText
  timeTaken = pyglet.text.Label("Time: " +"{:#.2f}".format(sum(lap_list) + float(stopwatch())), font_size=36, x=50, y=850, batch=displays)
  laps = pyglet.text.Label("Laps: " + str(len(lap_list)), font_size=36, x=50, y=800, batch=displays)
  leaderText = pyglet.text.Label("Leader: " +str(leader()), font_size=36, x=50, y=750, batch=displays)
  #lap_displays()     this function is commented out since it was causing lag
  
  #print("reward: ", reward())

  #PLAYER 1 ------------------
  #car code
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
    velocity = max_velocity
  if velocity < -(max_velocity-3):
    velocity = -(max_velocity-3)

  if forward == True and overlap_check(sprite_hitbox, line_list) != True:
    velocity += acceleration
  if backward == True and overlap_check(sprite_hitbox, line_list) != True:
    velocity -= acceleration/1.3

  if overlap_check(sprite_hitbox,line_list) == True:
    car.x, car.y = collList[int(-velocity//3)-2]
    drift = False
    velocity = 0
  
  new = (car.x, car.y)
  collList.append(new)
  if len(collList) > 13:
    del collList[0]

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

  #viewing lines for the AI ------------ (most of this code is purely for visuals, a large amount could be removed)
  global viewingLine1
  global viewingLine2
  global viewingLine3
  global viewingLine4
  global viewingLine5
  global viewingLine6
  global viewingLine7
  global viewingLine8
  global viewingLine9
  global viewingLine10
  global viewingLine11
  global viewingLine12
  global viewingLine13
  global viewingLine14
  global viewingLineList
  viewingLine1 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation)), y2=lineLength*cos(radians(car.rotation)), batch=aiLines)
  viewingLine2 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation) + radians(15)), y2=lineLength*cos(radians(car.rotation)+ radians(15)), batch=aiLines)
  viewingLine3 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation) + radians(30)), y2=lineLength*cos(radians(car.rotation) + radians(30)), batch=aiLines)
  viewingLine4 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation) + radians(45)), y2=lineLength*cos(radians(car.rotation) + radians(45)), batch=aiLines)
  viewingLine5 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation) + radians(60)), y2=lineLength*cos(radians(car.rotation) + radians(60)), batch=aiLines)
  viewingLine6 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation) + radians(90)), y2=lineLength*cos(radians(car.rotation) + radians(90)), batch=aiLines)
  viewingLine7 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation) + radians(135)), y2=lineLength*cos(radians(car.rotation) + radians(135)), batch=aiLines)
  viewingLine8 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation) + radians(180)), y2=lineLength*cos(radians(car.rotation) + radians(180)), batch=aiLines)
  viewingLine9 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation) + radians(225)), y2=lineLength*cos(radians(car.rotation) + radians(225)), batch=aiLines)
  viewingLine10 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation) + radians(270)), y2=lineLength*cos(radians(car.rotation) + radians(270)), batch=aiLines)
  viewingLine11 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation) + radians(300)), y2=lineLength*cos(radians(car.rotation) + radians(300)), batch=aiLines)
  viewingLine12 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation) + radians(315)), y2=lineLength*cos(radians(car.rotation) + radians(315)), batch=aiLines)
  viewingLine13 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation) + radians(330)), y2=lineLength*cos(radians(car.rotation) + radians(330)), batch=aiLines)
  viewingLine14 = pyglet.shapes.Line(x=car.x, y=car.y, x2=lineLength*sin(radians(car.rotation) + radians(345)), y2=lineLength*cos(radians(car.rotation) + radians(345)), batch=aiLines)

  viewingLineList = [viewingLine1, viewingLine2, viewingLine3, viewingLine4, viewingLine5, viewingLine6, viewingLine7, viewingLine8, viewingLine9, viewingLine10, viewingLine11, viewingLine12, viewingLine13, viewingLine14]

  global oldCollisionPointsList
  for x in viewingLineList:
    x.opacity = 100

  if len(aiVision()) < 14:
    collisionPointsList = oldCollisionPointsList
  else:
    collisionPointsList = aiVision()
    oldCollisionPointsList = collisionPointsList
  
  
  point1 = collisionPointsList[0]
  point2 = collisionPointsList[1]
  point3 = collisionPointsList[2]
  point4 = collisionPointsList[3]
  point5 = collisionPointsList[4]
  point6 = collisionPointsList[5]
  point7 = collisionPointsList[6]
  point8 = collisionPointsList[7]
  point9 = collisionPointsList[8]
  point10 = collisionPointsList[9]
  point11 = collisionPointsList[10]
  point12 = collisionPointsList[11]
  point13 = collisionPointsList[12]
  point14 = collisionPointsList[13]
  global circ1
  global circ2
  global circ3
  global circ4
  global circ5
  global circ6
  global circ7
  global circ8
  global circ9
  global circ10
  global circ11
  global circ12
  global circ13
  global circ14
  circ1 = pyglet.shapes.Circle(x=point1[0], y=point1[1], radius=5, color=(255,0,0), batch=aiLines)
  circ2 = pyglet.shapes.Circle(x=point2[0], y=point2[1], radius=5, color=(255,0,0), batch=aiLines)
  circ3 = pyglet.shapes.Circle(x=point3[0], y=point3[1], radius=5, color=(255,0,0), batch=aiLines)
  circ4 = pyglet.shapes.Circle(x=point4[0], y=point4[1], radius=5, color=(255,0,0), batch=aiLines)
  circ5 = pyglet.shapes.Circle(x=point5[0], y=point5[1], radius=5, color=(255,0,0), batch=aiLines)
  circ6 = pyglet.shapes.Circle(x=point6[0], y=point6[1], radius=5, color=(255,0,0), batch=aiLines)
  circ7 = pyglet.shapes.Circle(x=point7[0], y=point7[1], radius=5, color=(255,0,0), batch=aiLines)
  circ8 = pyglet.shapes.Circle(x=point8[0], y=point8[1], radius=5, color=(255,0,0), batch=aiLines)
  circ9 = pyglet.shapes.Circle(x=point9[0], y=point9[1], radius=5, color=(255,0,0), batch=aiLines)
  circ10 = pyglet.shapes.Circle(x=point10[0], y=point10[1], radius=5, color=(255,0,0), batch=aiLines)
  circ11 = pyglet.shapes.Circle(x=point11[0], y=point11[1], radius=5, color=(255,0,0), batch=aiLines)
  circ12 = pyglet.shapes.Circle(x=point12[0], y=point12[1], radius=5, color=(255,0,0), batch=aiLines)
  circ13 = pyglet.shapes.Circle(x=point13[0], y=point13[1], radius=5, color=(255,0,0), batch=aiLines)
  circ14 = pyglet.shapes.Circle(x=point14[0], y=point14[1], radius=5, color=(255,0,0), batch=aiLines)
  
  #updating aiVisionList, which is what the AI will see as part of its obersations from the environment
  global aiVisionList
  aiVisionList.clear()
  for x in range(len(collisionPointsList)):
    aiVisionList += collisionPointsList[x]
  observation_space = [car.x, car.y, car.rotation, velocity] + aiVisionList
  
  
pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()