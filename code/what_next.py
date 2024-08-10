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
    if grad_points((a,b), (c,d)) > 0: #first quadrant
      car.rotation = 90 - ang
    else: #second quadrant
      car.rotation = 270 + ang
  else:
    if grad_points((a,b), (c,d)) > 0: #third quadrant
      car.rotation = 270 - ang
    else: #fourth quadrant
      car.rotation = 90 + ang


def update(dt):
  #display code
  global timeTaken
  global laps
  global leaderText
  timeTaken = pyglet.text.Label("Time: " +"{:#.2f}".format(sum(lap_list) + float(stopwatch())), font_size=36, x=50, y=850, batch=displays)
  laps = pyglet.text.Label("Laps: " + str(len(lap_list)), font_size=36, x=50, y=800, batch=displays)
  leaderText = pyglet.text.Label("Leader: " +str(leader()), font_size=36, x=50, y=750, batch=displays)
  #lap_displays()     this function is commented out since it was causing lag


  
pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()