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

#defining variables, lists, and dictionaries - PLAYER 1 ---------------
sprite_hitbox = [(0,0),(0,0),(0,0),(0,0)]
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
checkerList = []

#AI specific code
lineLength = 100000000
reward_gate = False
wall_collision = False
new_gate_signal = False
oldCollisionPointsList = [(car_start_x,car_start_y),(car_start_x,car_start_y),(car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y), (car_start_x,car_start_y)]

#defining variables, lists, and dictionaries - PLAYER 2 ---------------
sprite_hitbox2 = [(0,0),(0,0),(0,0),(0,0)]
forward2 = False
backward2 = False
aclockwise2 = False
clockwise2 = False
drift2 = False
backDict2 = {}
collList2 = []
rounds2 = 0

lapCompleted2 = False

#tunable variables 
velocity2 = 0 *scale_factor
max_velocity2 = 8 *scale_factor
friction2 = 0.07 *scale_factor
acceleration2 = 0.1 *scale_factor
rotation_speed2 = 3
drift_time2 = 8 *scale_factor

#timer code
going2 = False
start2 = 0
current2 = 0
elapsed2 = 0
swap2 = False
started2 = False
checkerList2 = []

#timer lines (reward gates)
timer1 = pyglet.shapes.Line(x=995/1920 *window.width, y=100/1080 *window.height, x2=985/1920 *window.width, y2=250/1080 *window.height, width = 1, batch = lines, color=(255,165,0))
timer2 = pyglet.shapes.Line(x=939/1920 *window.width, y=246/1080 *window.height, x2=947/1920 *window.width, y2=98/1080 *window.height, width = 1, batch = lines, color=(255,165,0))
timer3 = pyglet.shapes.Line(x=889/1920 *window.width, y=239/1080 *window.height, x2=898/1920 *window.width, y2=91/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer4 = pyglet.shapes.Line(x=838/1920 *window.width, y=233/1080 *window.height, x2=844/1920 *window.width, y2=82/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer5 = pyglet.shapes.Line(x=789/1920 *window.width, y=225/1080 *window.height, x2=793/1920 *window.width, y2=75/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer6 = pyglet.shapes.Line(x=733/1920 *window.width, y=218/1080 *window.height, x2=742/1920 *window.width, y2=66/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer7 = pyglet.shapes.Line(x=682/1920 *window.width, y=210/1080 *window.height, x2=690/1920 *window.width, y2=58/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer8 = pyglet.shapes.Line(x=631/1920 *window.width, y=204/1080 *window.height, x2=637/1920 *window.width, y2=50/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer9 = pyglet.shapes.Line(x=584/1920 *window.width, y=198/1080 *window.height, x2=590/1920 *window.width, y2=43/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer10 = pyglet.shapes.Line(x=532/1920 *window.width, y=191/1080 *window.height, x2=542/1920 *window.width, y2=34/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer11 = pyglet.shapes.Line(x=476/1920 *window.width, y=183/1080 *window.height, x2=479/1920 *window.width, y2=26/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer12 = pyglet.shapes.Line(x=437/1920 *window.width, y=198/1080 *window.height, x2=381/1920 *window.width, y2=34/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer13 = pyglet.shapes.Line(x=402/1920 *window.width, y=217/1080 *window.height, x2=308/1920 *window.width, y2=74/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer14 = pyglet.shapes.Line(x=397/1920 *window.width, y=234/1080 *window.height, x2=253/1920 *window.width, y2=147/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer15 = pyglet.shapes.Line(x=386/1920 *window.width, y=268/1080 *window.height, x2=213/1920 *window.width, y2=229/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer16 = pyglet.shapes.Line(x=198/1920 *window.width, y=300/1080 *window.height, x2=390/1920 *window.width, y2=314/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer17 = pyglet.shapes.Line(x=393/1920 *window.width, y=338/1080 *window.height, x2=210/1920 *window.width, y2=371/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer18 = pyglet.shapes.Line(x=401/1920 *window.width, y=365/1080 *window.height, x2=243/1920 *window.width, y2=430/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer19 = pyglet.shapes.Line(x=422/1920 *window.width, y=384/1080 *window.height, x2=270/1920 *window.width, y2=480/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer20 = pyglet.shapes.Line(x=442/1920 *window.width, y=400/1080 *window.height, x2=337/1920 *window.width, y2=508/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer21 = pyglet.shapes.Line(x=467/1920 *window.width, y=412/1080 *window.height, x2=394/1920 *window.width, y2=529/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer22 = pyglet.shapes.Line(x=421/1920 *window.width, y=542/1080 *window.height, x2=500/1920 *window.width, y2=428/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer23 = pyglet.shapes.Line(x=565/1920 *window.width, y=454/1080 *window.height, x2=451/1920 *window.width, y2=554/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer24 = pyglet.shapes.Line(x=455/1920 *window.width, y=577/1080 *window.height, x2=591/1920 *window.width, y2=508/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer25 = pyglet.shapes.Line(x=611/1920 *window.width, y=565/1080 *window.height, x2=458/1920 *window.width, y2=597/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer26 = pyglet.shapes.Line(x=462/1920 *window.width, y=624/1080 *window.height, x2=608/1920 *window.width, y2=626/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer27 = pyglet.shapes.Line(x=447/1920 *window.width, y=658/1080 *window.height, x2=607/1920 *window.width, y2=697/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer28 = pyglet.shapes.Line(x=425/1920 *window.width, y=705/1080 *window.height, x2=589/1920 *window.width, y2=760/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer29 = pyglet.shapes.Line(x=401/1920 *window.width, y=752/1080 *window.height, x2=565/1920 *window.width, y2=815/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer30 = pyglet.shapes.Line(x=555/1920 *window.width, y=838/1080 *window.height, x2=364/1920 *window.width, y2=833/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer31 = pyglet.shapes.Line(x=555/1920 *window.width, y=855/1080 *window.height, x2=384/1920 *window.width, y2=964/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer32 = pyglet.shapes.Line(x=565/1920 *window.width, y=863/1080 *window.height, x2=495/1920 *window.width, y2=1032/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer33 = pyglet.shapes.Line(x=627/1920 *window.width, y=1049/1080 *window.height, x2=571/1920 *window.width, y2=859/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer34 = pyglet.shapes.Line(x=710/1920 *window.width, y=993/1080 *window.height, x2=579/1920 *window.width, y2=850/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer35 = pyglet.shapes.Line(x=733/1920 *window.width, y=921/1080 *window.height, x2=582/1920 *window.width, y2=839/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer36 = pyglet.shapes.Line(x=584/1920 *window.width, y=798/1080 *window.height, x2=751/1920 *window.width, y2=872/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer37 = pyglet.shapes.Line(x=617/1920 *window.width, y=742/1080 *window.height, x2=771/1920 *window.width, y2=842/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer38 = pyglet.shapes.Line(x=790/1920 *window.width, y=798/1080 *window.height, x2=654/1920 *window.width, y2=700/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer39 = pyglet.shapes.Line(x=801/1920 *window.width, y=778/1080 *window.height, x2=724/1920 *window.width, y2=660/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer40 = pyglet.shapes.Line(x=834/1920 *window.width, y=774/1080 *window.height, x2=802/1920 *window.width, y2=629/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer41 = pyglet.shapes.Line(x=874/1920 *window.width, y=774/1080 *window.height, x2=863/1920 *window.width, y2=635/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer42 = pyglet.shapes.Line(x=897/1920 *window.width, y=772/1080 *window.height, x2=944/1920 *window.width, y2=639/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer43 = pyglet.shapes.Line(x=937/1920 *window.width, y=793/1080 *window.height, x2=998/1920 *window.width, y2=655/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer44 = pyglet.shapes.Line(x=972/1920 *window.width, y=808/1080 *window.height, x2=1043/1920 *window.width, y2=677/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer45 = pyglet.shapes.Line(x=1011/1920 *window.width, y=826/1080 *window.height, x2=1083/1920 *window.width, y2=699/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer46 = pyglet.shapes.Line(x=1049/1920 *window.width, y=841/1080 *window.height, x2=1125/1920 *window.width, y2=720/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer47 = pyglet.shapes.Line(x=1094/1920 *window.width, y=863/1080 *window.height, x2=1173/1920 *window.width, y2=744/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer48 = pyglet.shapes.Line(x=1227/1920 *window.width, y=770/1080 *window.height, x2=1145/1920 *window.width, y2=886/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer49 = pyglet.shapes.Line(x=1198/1920 *window.width, y=909/1080 *window.height, x2=1281/1920 *window.width, y2=798/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer50 = pyglet.shapes.Line(x=1277/1920 *window.width, y=942/1080 *window.height, x2=1346/1920 *window.width, y2=831/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer51 = pyglet.shapes.Line(x=1341/1920 *window.width, y=970/1080 *window.height, x2=1398/1920 *window.width, y2=857/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer52 = pyglet.shapes.Line(x=1384/1920 *window.width, y=990/1080 *window.height, x2=1442/1920 *window.width, y2=877/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer53 = pyglet.shapes.Line(x=1467/1920 *window.width, y=884/1080 *window.height, x2=1431/1920 *window.width, y2=1009/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer54 = pyglet.shapes.Line(x=1486/1920 *window.width, y=1023/1080 *window.height, x2=1496/1920 *window.width, y2=888/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer55 = pyglet.shapes.Line(x=1536/1920 *window.width, y=893/1080 *window.height, x2=1537/1920 *window.width, y2=1023/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer56 = pyglet.shapes.Line(x=1555/1920 *window.width, y=882/1080 *window.height, x2=1631/1920 *window.width, y2=1022/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer57 = pyglet.shapes.Line(x=1697/1920 *window.width, y=983/1080 *window.height, x2=1563/1920 *window.width, y2=873/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer58 = pyglet.shapes.Line(x=1758/1920 *window.width, y=904/1080 *window.height, x2=1576/1920 *window.width, y2=857/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer59 = pyglet.shapes.Line(x=1594/1920 *window.width, y=837/1080 *window.height, x2=1763/1920 *window.width, y2=848/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer60 = pyglet.shapes.Line(x=1761/1920 *window.width, y=793/1080 *window.height, x2=1586/1920 *window.width, y2=810/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer61 = pyglet.shapes.Line(x=1576/1920 *window.width, y=776/1080 *window.height, x2=1726/1920 *window.width, y2=729/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer62 = pyglet.shapes.Line(x=1555/1920 *window.width, y=749/1080 *window.height, x2=1688/1920 *window.width, y2=675/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer63 = pyglet.shapes.Line(x=1633/1920 *window.width, y=635/1080 *window.height, x2=1516/1920 *window.width, y2=720/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer64 = pyglet.shapes.Line(x=1470/1920 *window.width, y=685/1080 *window.height, x2=1596/1920 *window.width, y2=607/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer65 = pyglet.shapes.Line(x=1573/1920 *window.width, y=587/1080 *window.height, x2=1415/1920 *window.width, y2=649/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer66 = pyglet.shapes.Line(x=1563/1920 *window.width, y=549/1080 *window.height, x2=1385/1920 *window.width, y2=601/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer67 = pyglet.shapes.Line(x=1580/1920 *window.width, y=513/1080 *window.height, x2=1356/1920 *window.width, y2=545/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer68 = pyglet.shapes.Line(x=1376/1920 *window.width, y=462/1080 *window.height, x2=1595/1920 *window.width, y2=504/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer69 = pyglet.shapes.Line(x=1434/1920 *window.width, y=412/1080 *window.height, x2=1601/1920 *window.width, y2=504/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer70 = pyglet.shapes.Line(x=1639/1920 *window.width, y=486/1080 *window.height, x2=1502/1920 *window.width, y2=377/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer71 = pyglet.shapes.Line(x=1524/1920 *window.width, y=365/1080 *window.height, x2=1709/1920 *window.width, y2=451/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer72 = pyglet.shapes.Line(x=1525/1920 *window.width, y=347/1080 *window.height, x2=1764/1920 *window.width, y2=391/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer73 = pyglet.shapes.Line(x=1776/1920 *window.width, y=296/1080 *window.height, x2=1526/1920 *window.width, y2=326/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer74 = pyglet.shapes.Line(x=1721/1920 *window.width, y=219/1080 *window.height, x2=1526/1920 *window.width, y2=326/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer75 = pyglet.shapes.Line(x=1516/1920 *window.width, y=324/1080 *window.height, x2=1618/1920 *window.width, y2=203/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer76 = pyglet.shapes.Line(x=1475/1920 *window.width, y=322/1080 *window.height, x2=1546/1920 *window.width, y2=192/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer77 = pyglet.shapes.Line(x=1438/1920 *window.width, y=317/1080 *window.height, x2=1493/1920 *window.width, y2=183/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer78 = pyglet.shapes.Line(x=1389/1920 *window.width, y=309/1080 *window.height, x2=1433/1920 *window.width, y2=175/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer79 = pyglet.shapes.Line(x=1350/1920 *window.width, y=302/1080 *window.height, x2=1367/1920 *window.width, y2=166/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer80 = pyglet.shapes.Line(x=1283/1920 *window.width, y=296/1080 *window.height, x2=1315/1920 *window.width, y2=156/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer81 = pyglet.shapes.Line(x=1208/1920 *window.width, y=286/1080 *window.height, x2=1256/1920 *window.width, y2=149/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer82 = pyglet.shapes.Line(x=1108/1920 *window.width, y=270/1080 *window.height, x2=1148/1920 *window.width, y2=131/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer83 = pyglet.shapes.Line(x=1020/1920 *window.width, y=258/1080 *window.height, x2=1054/1920 *window.width, y2=117/1080 *window.height, width = 1, batch = lines, color=(225,165,0))

timerLineList = [timer1, timer2, timer3, timer4, timer5, timer6, timer7, timer8, timer9, timer10, timer11, timer12, timer13, timer14, timer15, timer16, timer17, timer18, timer19, timer20, timer21, timer22, timer23, timer24, timer25, timer26, timer27, timer28, timer29, timer30, timer31, timer32, timer33, timer34, timer35, timer36, timer37, timer38, timer39, timer40, timer41, timer42, timer43, timer44, timer45, timer46, timer47, timer48, timer49, timer50, timer51, timer52, timer53, timer54, timer55, timer56, timer57, timer58, timer59, timer60, timer61, timer62, timer63, timer64, timer65, timer66, timer67, timer68, timer69, timer70, timer71, timer72, timer73, timer74, timer75, timer76, timer77, timer78, timer79, timer80, timer81, timer82, timer83] 

#loading up checkerList based on number of timer lines.tyimer
for x in timerLineList:
  checkerList.append(False)
  checkerList2.append(False)
  x.opacity = 100

#function that records the time for each lap
def stopwatch():
  #PLAYER 1 --------
  global going
  global start
  global current
  global elapsed
  global swap
  global lapCompleted

  if lapCompleted == True:
    lap_list.append(float("{:#.2f}".format(elapsed)))
    lapCompleted = False

  current = time.time()
  if going == True:
    if swap == True:
      start = time.time()
  elif going == False:
    current = start
  elapsed = current - start
  swap = False

  return "{:#.2f}".format(elapsed)
def stopwatch2():
  #PLAYER 2 --------
  global going2
  global start2
  global current2
  global elapsed2
  global swap2
  global lapCompleted2

  if lapCompleted2 == True:
    lap_list2.append(float("{:#.2f}".format(elapsed2)))
    lapCompleted2 = False

  current2 = time.time()
  if going2 == True:
    if swap2 == True:
      start2 = time.time()
  elif going2 == False:
    current2 = start2
  elapsed2 = current2 - start2
  swap2 = False

  return "{:#.2f}".format(elapsed2)

def timerLine(input_line):
  global timerLineList
  if input_line in timerLineList:
    return True

def lineChecks(input_line):
    global new_gate_signal
    global swap
    global checkerList
    global going
    global start
    global started
    global lapCompleted
    noStart = False
    if input_line == timerLineList[0]:
      for x in checkerList:
        if x != False:
          noStart = True
          break
      if noStart == False:
        if started == False:
          started = True
          checkerList[0] = True
          swap = True
          going = True
      
      if checkerList[timerLineList.index(input_line)-1] == True or checkerList[timerLineList.index(input_line)-2] == True or checkerList[timerLineList.index(input_line)-3] == True or checkerList[timerLineList.index(input_line)-4] == True or checkerList[timerLineList.index(input_line)-5] == True or checkerList[timerLineList.index(input_line)-6] == True:
        swap = True
        started = False
        for x in range(1,len(checkerList)+1):
          checkerList[x-1] = False
        
        for line in timerLineList:
          line.color = (255,165,0)
        
        
        lapCompleted = True
        if going == False:
          going = True
        else:
          going = False
    
    else:
      if checkerList[timerLineList.index(input_line)-1] == True or checkerList[timerLineList.index(input_line)-2] == True or checkerList[timerLineList.index(input_line)-3] == True or checkerList[timerLineList.index(input_line)-4] == True or checkerList[timerLineList.index(input_line)-5] == True or checkerList[timerLineList.index(input_line)-6] == True:
        input_line.color = (255,255,255)
        if checkerList[timerLineList.index(input_line)] == False:
          new_gate_signal = True
        checkerList[timerLineList.index(input_line)] = True

lap_list = []
lap_list2 = []

aiVisionList = []

#line overlap function
def find_intersection(line1, line2):
    x1, y1, x2, y2 = line1.x, line1.y, line1.x2, line1.y2
    x3, y3, x4, y4 = line2.x, line2.y, line2.x2, line2.y2
    #first line equation
    a1 = y2 - y1
    b1 = x1 - x2
    c1 = a1 * x1 + b1 * y1
    #second line equation
    a2 = y4 - y3
    b2 = x3 - x4
    c2 = a2 * x3 + b2 * y3
    
    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        # Lines are parallel
        return None
    else:
        xi = (b2 * c1 - b1 * c2) / determinant
        yi = (a1 * c2 - a2 * c1) / determinant
        # Check if the intersection point is within both line segments
        if (min(x1, x2) <= xi <= max(x1, x2) and min(y1, y2) <= yi <= max(y1, y2) and
            min(x3, x4) <= xi <= max(x3, x4) and min(y3, y4) <= yi <= max(y3, y4)):
            dist = distance_points((car.x, car.y), (xi,yi))
            return (xi, yi, dist)
        else:
            return None

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

#collision detection system
def overlap_check(car_hitbox, input_lines):
  global reward_gate
  global wall_collision

  hitbox_lines = []
  for x in range(len(car_hitbox)):
    a,b = car_hitbox[x%4]
    c,d = car_hitbox[(x+1)%4]
    hitbox_lines.append(pyglet.shapes.Line(x=a, y=b, x2=c, y2=d, width=1))

  for wall in input_lines:
    for car_side in hitbox_lines:
      #if min(wall.x, wall.x2) < min(car_side.x, car_side.y) < max(wall.x, wall.x2)
      if find_intersection(car_side, wall) != None:
        if timerLine(wall) == True:
          reward_gate = True
          lineChecks(wall, car_hitbox)
        else:
          wall_collision = True
          return True
  
              
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
def on_key_press(symbol, modifiers):
  #PLAYER 1 code -----
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

  if symbol == key.RSHIFT:
    if len(backDict) > drift_time:
      drift = True
      #max_velocity = 11 
      rotation_speed = 3.5
      rounds = 0
  
  #PLAYER 1 code -----
  global forward2
  global backward2
  global clockwise2
  global aclockwise2
  global drift2
  global rounds2
  global rotation_speed2
  global max_velocity2
  global velocity2

  if symbol == key.W:
    forward2 = True
  if symbol == key.S:
    backward2 = True

  if symbol == key.A:
    aclockwise2 = True
  if symbol == key.D:
    clockwise2 = True

  if symbol == key.LSHIFT:
    if len(backDict2) > drift_time2:
      drift2 = True
      #max_velocity2 = 11 
      rotation_speed2 = 3.5
      rounds2 = 0

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

@window.event
def on_key_release(symbol, modifiers):
  #PLAYER 1 code ---------
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
  if symbol == key.RSHIFT:
    drift = False
    rotation_speed = 3
    #max_velocity = 8
  
  #PLAYER 2 code ---------
  global forward2
  global backward2
  global clockwise2
  global aclockwise2
  global drift2
  global rotation_speed2
  global max_velocity2

  if symbol == key.W:
    forward2 = False
  if symbol == key.S:
    backward2 = False
  if symbol == key.A:
    aclockwise2 = False
  if symbol == key.D:
    clockwise2 = False
  if symbol == key.LSHIFT:
    drift2 = False
    rotation_speed2 = 3
    #max_velocity2 = 8

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
  #PLAYER 2 ------------------
  stopwatch2()
  #car code
  global velocity2
  global rounds2
  global sprite_hitbox2
  global circle4
  global circle5
  global circle6
  global circle7
  global drift2

  if velocity2 > 0:
    velocity2 -= friction2
  if velocity2 < 0:
    velocity2 += friction2
  if velocity2 > max_velocity2:
    velocity2 = max_velocity2
  if velocity2 < -(max_velocity2-3):
    velocity2 = -(max_velocity2-3)

  if forward2 == True and overlap_check(sprite_hitbox2, line_list) != True:
    velocity2 += acceleration2
  if backward2 == True and overlap_check(sprite_hitbox2, line_list) != True:
    velocity2 -= acceleration2/1.3

  new = (car2.x, car2.y)
  collList2.append(new)
  if len(collList2) > 13:
    del collList2[0]

  if overlap_check(sprite_hitbox2,line_list) == True:
    car2.x, car2.y = collList2[int(-velocity2//3)-2]
    drift2 = False
    velocity2 = 0
  
  dy2 = velocity2 * cos(radians(car2.rotation))
  dx2 = velocity2 * sin(radians(car2.rotation))
  
  new = {dy2:dx2}
  backDict2.update(new)
  if len(backDict2) > drift_time2:
    backDict2.pop(list(backDict2)[0])
  
  circle4 = pyglet.shapes.Circle(x=h*cos(1.57 +atan(half_width_car/half_height_car) - radians(car2.rotation)) + car2.x, y=h*sin(1.57 +atan(half_width_car/half_height_car) - radians(car2.rotation)) + car2.y, radius=1, color=(255,255,255))
  circle5 = pyglet.shapes.Circle(x=h*cos(1.57 -atan(half_width_car/half_height_car) - radians(car2.rotation)) + car2.x, y=h*sin(1.57 -atan(half_width_car/half_height_car) - radians(car2.rotation)) + car2.y, radius=1, color=(255,255,255))
  circle6 = pyglet.shapes.Circle(x=h*cos(4.71 -atan(half_width_car/half_height_car) - radians(car2.rotation)) + car2.x, y=h*sin(4.71 -atan(half_width_car/half_height_car) - radians(car2.rotation)) + car2.y, radius=1, color=(255,255,255))
  circle7 = pyglet.shapes.Circle(x=h*cos(-1.57 +atan(half_width_car/half_height_car) - radians(car2.rotation)) + car2.x, y=h*sin(-1.57 +atan(half_width_car/half_height_car) - radians(car2.rotation)) + car2.y, radius=1, color=(255,255,255))
  
  sprite_top_left2 = (h*cos(1.57 +angle) + car2.x, h*sin(1.57 +angle) + car2.y)
  sprite_top_right2 = (h*cos(1.57 - angle) + car2.x, h*sin(1.57 - angle) + car2.y)
  sprite_bottom_left2 = (h*cos(4.71 -angle) + car2.x, h*sin(4.71 -angle) + car2.y)
  sprite_bottom_right2 = (h*cos(-1.57 + angle) + car2.x, h*sin(-1.57 + angle) + car2.y)

  sprite_hitbox2 = [sprite_top_left2,sprite_top_right2,sprite_bottom_left2,sprite_bottom_right2]
  
  rounds2 += 1
  if drift2 == True:
    if rounds2 >= drift_time2:
      car2.y += list(backDict2)[0]
      car2.x += backDict2[list(backDict2)[1]]
    else:
      car2.y += dy2
      car2.x += dx2
  else:
    car2.y += dy2
    car2.x += dx2
  
  if forward2 == True or backward2 == True or velocity2 > friction2 or velocity2 < -friction2:
    if aclockwise2 == True:
      car2.rotation -= rotation_speed2
    if clockwise2 == True:
      car2.rotation += rotation_speed2
  
pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()