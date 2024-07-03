#NOTE: 
#need to fix that if you drive backwards you go straight through the barrier
import pyglet
import time
from pyglet import sprite, image
from pyglet.window import key, mouse
from math import sin, cos, atan, radians, sqrt, tanh

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

#entry images
logo_img = image.load("images/logo_finished.png")
logo_img.anchor_x = logo_img.width//2
logo_img.anchor_y = logo_img.height//2
logo = sprite.Sprite(logo_img, x=window.width//2, y=window.height//2 +100, batch=entryDisplay)
logo.scale = scale_factor

play_img = image.load("images/text_play.png")
play_img.anchor_x = play_img.width//2
play_img.anchor_y = play_img.height//2
playButton = sprite.Sprite(play_img, x=window.width//2, y=window.height//2 -200, batch=entryDisplay)
playButton.scale = 0.5*scale_factor

triangle_img = image.load("images/triangle1_translucent.png")
triangle_img.anchor_x = triangle_img.width//2
triangle_img.anchor_y = triangle_img.height//2
triangle1 = sprite.Sprite(triangle_img, x=100, y=100, batch=entryDisplay)
triangle1.rotation = 30
triangle1.scale = 0.3*scale_factor

#track_image = image.load("images/track V4.png")
car_image = image.load("images/car.png")

car_image.anchor_x = car_image.width// 2
car_image.anchor_y = car_image.height // 2

#timer code
going = False
start = 0
current= 0
elapsed = 0
swap = False
started = False

checkerList = []

#timer lines
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
timer82 = pyglet.shapes.Line(x=1162/1920 *window.width, y=278/1080 *window.height, x2=1200/1920 *window.width, y2=140/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer83 = pyglet.shapes.Line(x=1108/1920 *window.width, y=270/1080 *window.height, x2=1148/1920 *window.width, y2=131/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer84 = pyglet.shapes.Line(x=1048/1920 *window.width, y=262/1080 *window.height, x2=1101/1920 *window.width, y2=125/1080 *window.height, width = 1, batch = lines, color=(225,165,0))
timer85 = pyglet.shapes.Line(x=1020/1920 *window.width, y=258/1080 *window.height, x2=1054/1920 *window.width, y2=117/1080 *window.height, width = 1, batch = lines, color=(225,165,0))



timerLineList = [timer1, timer2, timer3, timer4, timer5, timer6, timer7, timer8, timer9, timer10, timer11, timer12, timer13, timer14, timer15, timer16, timer17, timer18, timer19, timer20, timer21, timer22, timer23, timer24, timer25, timer26, timer27, timer28, timer29, timer30, timer31, timer32, timer33, timer34, timer35, timer36, timer37, timer38, timer39, timer40, timer41, timer42, timer43, timer44, timer45, timer46, timer47, timer48, timer49, timer50, timer51, timer52, timer53, timer54, timer55, timer56, timer57, timer58, timer59, timer60, timer61, timer62, timer63, timer64, timer65, timer66, timer67, timer68, timer69, timer70, timer71, timer72, timer73, timer74, timer75, timer76, timer77, timer78, timer79, timer80, timer81, timer82, timer83, timer84, timer85] 

#loading up checkerList based on number of timer lines.
for x in timerLineList:
  checkerList.append(False)
  x.opacity = 100

def stopwatch():
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

def timerLine(input_line):
  global timerLineList
  if input_line in timerLineList:
    return True

def lineChecks(input_line):
  global swap
  global checkerList
  global going
  global start
  global started
  global lapCompleted
  noStart = False
  noFinish = False
  if input_line == timer1:
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
      checkerList[timerLineList.index(input_line)] = True



#outside lines
line = pyglet.shapes.Line(x=472/1920 * window.width, y=23/1080 * window.height, x2=1723/1920 * window.width, y2=217/1080 * window.height, width = 1, batch = lines)
line1 = pyglet.shapes.Line(x=1723/1920 * window.width, y=217/1080 * window.height, x2=1777/1920 * window.width, y2=295/1080 * window.height, width = 1, batch = lines)
line2 = pyglet.shapes.Line(x=1777/1920 * window.width, y=295/1080 * window.height, x2=1764/1920 * window.width, y2=392/1080 * window.height, width = 1, batch = lines)
line3 = pyglet.shapes.Line(x=1764/1920 * window.width, y=392/1080 * window.height, x2=1704/1920 * window.width, y2=459/1080 * window.height, width = 1, batch = lines)
line4 = pyglet.shapes.Line(x=1704/1920 * window.width, y=459/1080 * window.height, x2=1580/1920 * window.width, y2=510/1080 * window.height, width = 1, batch = lines)
line5 = pyglet.shapes.Line(x=1580/1920 * window.width, y=510/1080 * window.height, x2=1562/1920 * window.width, y2=548/1080 * window.height, width = 1, batch = lines)
line6 = pyglet.shapes.Line(x=1562/1920 * window.width, y=548/1080 * window.height, x2=1571/1920 * window.width, y2=584/1080 * window.height, width = 1, batch = lines)
line7 = pyglet.shapes.Line(x=1571/1920 * window.width, y=584/1080 * window.height, x2=1707/1920 * window.width, y2=690/1080 * window.height, width = 1, batch = lines)
line8 = pyglet.shapes.Line(x=1707/1920 * window.width, y=690/1080 * window.height, x2=1765/1920 * window.width, y2=800/1080 * window.height, width = 1, batch = lines)
line9 = pyglet.shapes.Line(x=1765/1920 * window.width, y=800/1080 * window.height, x2=1760/1920 * window.width, y2=901/1080 * window.height, width = 1, batch = lines)
line10 = pyglet.shapes.Line(x=1760/1920 * window.width, y=901/1080 * window.height, x2=1696/1920 * window.width, y2=984/1080 * window.height, width = 1, batch = lines)
line11 = pyglet.shapes.Line(x=1696/1920 * window.width, y=984/1080 * window.height, x2=1632/1920 * window.width, y2=1021/1080 * window.height, width = 1, batch = lines)
line12 = pyglet.shapes.Line(x=1632/1920 * window.width, y=1021/1080 * window.height, x2=1462/1920 * window.width, y2=1022/1080 * window.height, width = 1, batch = lines)
line13 = pyglet.shapes.Line(x=1462/1920 * window.width, y=1022/1080 * window.height, x2=1193/1920 * window.width, y2=906/1080 * window.height, width = 1, batch = lines)
line14 = pyglet.shapes.Line(x=1193/1920 * window.width, y=906/1080 * window.height, x2=892/1920 * window.width, y2=771/1080 * window.height, width = 1, batch = lines)
line15 = pyglet.shapes.Line(x=892/1920 * window.width, y=771/1080 * window.height, x2=802/1920 * window.width, y2=777/1080 * window.height, width = 1, batch = lines)
line16 = pyglet.shapes.Line(x=802/1920 * window.width, y=777/1080 * window.height, x2=746/1920 * window.width, y2=883/1080 * window.height, width = 1, batch = lines)
line17 = pyglet.shapes.Line(x=746/1920 * window.width, y=883/1080 * window.height, x2=711/1920 * window.width, y2=995/1080 * window.height, width = 1, batch = lines)
line18 = pyglet.shapes.Line(x=711/1920 * window.width, y=995/1080 * window.height, x2=628/1920 * window.width, y2=1050/1080 * window.height, width = 1, batch = lines)
line19 = pyglet.shapes.Line(x=628/1920 * window.width, y=1050/1080 * window.height, x2=494/1920 * window.width, y2=1031/1080 * window.height, width = 1, batch = lines)
line20 = pyglet.shapes.Line(x=494/1920 * window.width, y=1031/1080 * window.height, x2=384/1920 * window.width, y2=964/1080 * window.height, width = 1, batch = lines)
line21 = pyglet.shapes.Line(x=384/1920 * window.width, y=964/1080 * window.height, x2=364/1920 * window.width, y2=832/1080 * window.height, width = 1, batch = lines)
line22 = pyglet.shapes.Line(x=364/1920 * window.width, y=832/1080 * window.height, x2=462/1920 * window.width, y2=624/1080 * window.height, width = 1, batch = lines)
line23 = pyglet.shapes.Line(x=462/1920 * window.width, y=624/1080 * window.height, x2=453/1920 * window.width, y2=555/1080 * window.height, width = 1, batch = lines)
line24 = pyglet.shapes.Line(x=453/1920 * window.width, y=555/1080 * window.height, x2=269/1920 * window.width, y2=478/1080 * window.height, width = 1, batch = lines)
line25 = pyglet.shapes.Line(x=269/1920 * window.width, y=478/1080 * window.height, x2=211/1920 * window.width, y2=370/1080 * window.height, width = 1, batch = lines)
line26 = pyglet.shapes.Line(x=211/1920 * window.width, y=370/1080 * window.height, x2=207/1920 * window.width, y2=245/1080 * window.height, width = 1, batch = lines)
line27 = pyglet.shapes.Line(x=207/1920 * window.width, y=245/1080 * window.height, x2=278/1920 * window.width, y2=98/1080 * window.height, width = 1, batch = lines)
line28 = pyglet.shapes.Line(x=278/1920 * window.width, y=98/1080 * window.height, x2=355/1920 * window.width, y2=36/1080 * window.height, width = 1, batch = lines)
line29 = pyglet.shapes.Line(x=355/1920 * window.width, y=36/1080 * window.height, x2=472/1920 * window.width, y2=23/1080 * window.height, width = 1, batch = lines)

#inside lines
line30 = pyglet.shapes.Line(x=470/1920 *window.width, y=181/1080 *window.height, x2=1525/1920 *window.width, y2=325/1080 *window.height, width = 1, batch = lines)
line31 = pyglet.shapes.Line(x=1525/1920 *window.width, y=325/1080 *window.height, x2=1526/1920 *window.width, y2=363/1080 *window.height, width = 1, batch = lines)
line32 = pyglet.shapes.Line(x=1526/1920 *window.width, y=363/1080 *window.height, x2=1383/1920 *window.width, y2=435/1080 *window.height, width = 1, batch = lines)
line33 = pyglet.shapes.Line(x=1383/1920 *window.width, y=435/1080 *window.height, x2=1354/1920 *window.width, y2=554/1080 *window.height, width = 1, batch = lines)
line34 = pyglet.shapes.Line(x=1354/1920 *window.width, y=554/1080 *window.height, x2=1414/1920 *window.width, y2=644/1080 *window.height, width = 1, batch = lines)
line35 = pyglet.shapes.Line(x=1414/1920 *window.width, y=644/1080 *window.height, x2=1569/1920 *window.width, y2=758/1080 *window.height, width = 1, batch = lines)
line36 = pyglet.shapes.Line(x=1569/1920 *window.width, y=758/1080 *window.height, x2=1596/1920 *window.width, y2=838/1080 *window.height, width = 1, batch = lines)
line37 = pyglet.shapes.Line(x=1596/1920 *window.width, y=838/1080 *window.height, x2=1545/1920 *window.width, y2=891/1080 *window.height, width = 1, batch = lines)
line38 = pyglet.shapes.Line(x=1545/1920 *window.width, y=891/1080 *window.height, x2=1457/1920 *window.width, y2=882/1080 *window.height, width = 1, batch = lines)
line39 = pyglet.shapes.Line(x=1457/1920 *window.width, y=882/1080 *window.height, x2=969/1920 *window.width, y2=639/1080 *window.height, width = 1, batch = lines)
line40 = pyglet.shapes.Line(x=969/1920 *window.width, y=639/1080 *window.height, x2=801/1920 *window.width, y2=629/1080 *window.height, width = 1, batch = lines)
line41 = pyglet.shapes.Line(x=801/1920 *window.width, y=629/1080 *window.height, x2=676/1920 *window.width, y2=676/1080 *window.height, width = 1, batch = lines)
line42 = pyglet.shapes.Line(x=676/1920 *window.width, y=676/1080 *window.height, x2=618/1920 *window.width, y2=739/1080 *window.height, width = 1, batch = lines)
line43 = pyglet.shapes.Line(x=618/1920 *window.width, y=739/1080 *window.height, x2=585/1920 *window.width, y2=793/1080 *window.height, width = 1, batch = lines)
line44 = pyglet.shapes.Line(x=585/1920 *window.width, y=793/1080 *window.height, x2=581/1920 *window.width, y2=848/1080 *window.height, width = 1, batch = lines)
line45 = pyglet.shapes.Line(x=581/1920 *window.width, y=848/1080 *window.height, x2=566/1920 *window.width, y2=864/1080 *window.height, width = 1, batch = lines)
line46 = pyglet.shapes.Line(x=566/1920 *window.width, y=864/1080 *window.height, x2=555/1920 *window.width, y2=854/1080 *window.height, width = 1, batch = lines)
line47 = pyglet.shapes.Line(x=555/1920 *window.width, y=854/1080 *window.height, x2=554/1920 *window.width, y2=840/1080 *window.height, width = 1, batch = lines)
line48 = pyglet.shapes.Line(x=554/1920 *window.width, y=840/1080 *window.height, x2=581/1920 *window.width, y2=785/1080 *window.height, width = 1, batch = lines)
line49 = pyglet.shapes.Line(x=581/1920 *window.width, y=785/1080 *window.height, x2=608/1920 *window.width, y2=697/1080 *window.height, width = 1, batch = lines)
line50 = pyglet.shapes.Line(x=608/1920 *window.width, y=697/1080 *window.height, x2=612/1920 *window.width, y2=548/1080 *window.height, width = 1, batch = lines)
line51 = pyglet.shapes.Line(x=612/1920 *window.width, y=548/1080 *window.height, x2=565/1920 *window.width, y2=452/1080 *window.height, width = 1, batch = lines)
line52 = pyglet.shapes.Line(x=565/1920 *window.width, y=452/1080 *window.height, x2=440/1920 *window.width, y2=399/1080 *window.height, width = 1, batch = lines)
line53 = pyglet.shapes.Line(x=440/1920 *window.width, y=399/1080 *window.height, x2=400/1920 *window.width, y2=364/1080 *window.height, width = 1, batch = lines)
line54 = pyglet.shapes.Line(x=400/1920 *window.width, y=364/1080 *window.height, x2=383/1920 *window.width, y2=277/1080 *window.height, width = 1, batch = lines)
line55 = pyglet.shapes.Line(x=383/1920 *window.width, y=277/1080 *window.height, x2=404/1920 *window.width, y2=217/1080 *window.height, width = 1, batch = lines)
line56 = pyglet.shapes.Line(x=404/1920 *window.width, y=217/1080 *window.height, x2=470/1920 *window.width, y2=181/1080 *window.height, width = 1, batch = lines)

line_list = [line, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15, line16, line17, line18, line19, line20, line21, line22, line23, line24, line25, line26, line27, line28, line29, line30, line31, line32, line33, line34, line35, line36, line37, line38, line39, line40, line41, line42, line43, line44, line45, line46, line47, line48, line49, line50, line51, line52, line53, line54, line55, line56, timer1, timer2, timer3, timer4, timer5, timer6, timer7, timer8, timer9, timer10, timer11, timer12, timer13, timer14, timer15, timer16, timer17, timer18, timer19, timer20, timer21, timer22, timer23, timer24, timer25, timer26, timer27, timer28, timer29, timer30, timer31, timer32, timer33, timer34, timer35, timer36, timer37, timer38, timer39, timer40, timer41, timer42, timer43, timer44, timer45, timer46, timer47, timer48, timer49, timer50, timer51, timer52, timer53, timer54, timer55, timer56, timer57, timer58, timer59, timer60, timer61, timer62, timer63, timer64, timer65, timer66, timer67, timer68, timer69, timer70, timer71, timer72, timer73, timer74, timer75, timer76, timer77, timer78, timer79, timer80, timer81, timer82, timer83, timer84, timer85]

lap_list = []

def overlap_check(car_hitbox, input_lines):
  global collide_x
  global collide_y
  for (x,y) in car_hitbox:
    for input_line in input_lines:
      if min(input_line.x, input_line.x2) < x < max(input_line.x, input_line.x2):
        if min(input_line.y, input_line.y2) < y < max(input_line.y, input_line.y2):  
            gradient = (input_line.y2-input_line.y)/(input_line.x2-input_line.x)
            if abs(gradient) > 12:
              new_velocity = (tanh(velocity)*2+1)**12
            elif abs(gradient) < 0.5:
              new_velocity = (tanh(velocity)*2+1)**((abs(gradient)+1)**2)
            else:
              new_velocity = (tanh(velocity)*2+1)
            if velocity > 0:
              if y - input_line.y -new_velocity < gradient*(x-input_line.x) < y - input_line.y + new_velocity:
                if timerLine(input_line) == True:
                  lineChecks(input_line)
                else:
                  return True
            #if velocity < 0:
              #if y - input_line.y -velocity > gradient*(x-input_line.x) > y - input_line.y + velocity:
                #return True
              
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


#track = sprite.Sprite(track_image, x=200, y=0)
car_start_x =  1020/1920 *window.width
car_start_y =  185/1080 *window.height
car = sprite.Sprite(car_image, car_start_x, car_start_y)
car.scale = 0.1*scale_factor
#track.scale = 2.6*scale_factor
car.rotation = 260

#these are constant values - having them as callable variables should make the update function faster
half_width_car = (car_image.width)*scale_factor // 20
half_height_car = (car_image.height)*scale_factor// 20
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

lapCompleted = False

#tunable variables 
velocity = 0 *scale_factor
max_velocity = 8 *scale_factor
friction = 0.07 *scale_factor
acceleration = 0.1 *scale_factor
rotation_speed = 3
drift_time = 8 *scale_factor

@window.event
def on_draw():
  window.clear()
  if windowOn[0] == 1:
    entryDisplay.draw()
  if windowOn[1] == 1:
    displays.draw()
    #lap_displays() this function is commented out since it was causing lag
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
      #max_velocity = 11 
      rotation_speed = 3.5
      rounds = 0

@window.event   
def on_mouse_press(x,y,button, modifiers):
  global windowOn
  if button == mouse.LEFT:
    if windowOn == [1,0]:
      windowOn = [0,1]
    print(x,y)
    print(lap_list)

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
    #max_velocity = 8

def update(dt):
  #display code
  global timeTaken
  global laps
  global leader
  timeTaken = pyglet.text.Label("Time: " +"{:#.2f}".format(sum(lap_list) + float(stopwatch())), font_size=36, x=50, y=850, batch=displays)
  laps = pyglet.text.Label("Laps: " + str(len(lap_list)), font_size=36, x=50, y=800, batch=displays)
  leader = pyglet.text.Label("Leader: Me", font_size=36, x=50, y=750, batch=displays)
  #lap_displays()     this function is commented out since it was causing lag

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