#NOTE: 
#need to fix that if you drive backwards you go straight through the barrier
import pyglet
import time
from pyglet import sprite, image
from pyglet.window import key, mouse
from math import sin, cos, atan, radians, sqrt, tanh

window = pyglet.window.Window(resizable = False, caption="Artificial Drift")
window.set_fullscreen(True)

lines = pyglet.graphics.Batch()
displays = pyglet.graphics.Batch()

#track_image = image.load("images/track V4.png")
car_image = image.load("images/car.png")

car_image.anchor_x = car_image.width // 2
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
timer1 = pyglet.shapes.Line(x=995, y=100, x2=985, y2=250, width = 1, batch = lines, color=(255,165,0))
timer2 = pyglet.shapes.Line(x=939, y=246, x2=947, y2=98, width = 1, batch = lines, color=(255,165,0))
timer3 = pyglet.shapes.Line(x=889, y=239, x2=898, y2=91, width = 1, batch = lines, color=(225,165,0))
timer4 = pyglet.shapes.Line(x=838, y=233, x2=844, y2=82, width = 1, batch = lines, color=(225,165,0))
timer5 = pyglet.shapes.Line(x=789, y=225, x2=793, y2=75, width = 1, batch = lines, color=(225,165,0))
timer6 = pyglet.shapes.Line(x=733, y=218, x2=742, y2=66, width = 1, batch = lines, color=(225,165,0))
timer7 = pyglet.shapes.Line(x=682, y=210, x2=690, y2=58, width = 1, batch = lines, color=(225,165,0))
timer8 = pyglet.shapes.Line(x=631, y=204, x2=637, y2=50, width = 1, batch = lines, color=(225,165,0))
timer9 = pyglet.shapes.Line(x=584, y=198, x2=590, y2=43, width = 1, batch = lines, color=(225,165,0))
timer10 = pyglet.shapes.Line(x=532, y=191, x2=542, y2=34, width = 1, batch = lines, color=(225,165,0))
timer11 = pyglet.shapes.Line(x=476, y=183, x2=479, y2=26, width = 1, batch = lines, color=(225,165,0))
timer12 = pyglet.shapes.Line(x=437, y=198, x2=381, y2=34, width = 1, batch = lines, color=(225,165,0))
timer13 = pyglet.shapes.Line(x=402, y=217, x2=308, y2=74, width = 1, batch = lines, color=(225,165,0))
timer14 = pyglet.shapes.Line(x=397, y=234, x2=253, y2=147, width = 1, batch = lines, color=(225,165,0))
timer15 = pyglet.shapes.Line(x=386, y=268, x2=213, y2=229, width = 1, batch = lines, color=(225,165,0))
timer16 = pyglet.shapes.Line(x=198, y=300, x2=390, y2=314, width = 1, batch = lines, color=(225,165,0))
timer17 = pyglet.shapes.Line(x=393, y=338, x2=210, y2=371, width = 1, batch = lines, color=(225,165,0))
timer18 = pyglet.shapes.Line(x=401, y=365, x2=243, y2=430, width = 1, batch = lines, color=(225,165,0))
timer19 = pyglet.shapes.Line(x=422, y=384, x2=270, y2=480, width = 1, batch = lines, color=(225,165,0))
timer20 = pyglet.shapes.Line(x=442, y=400, x2=337, y2=508, width = 1, batch = lines, color=(225,165,0))
timer21 = pyglet.shapes.Line(x=467, y=412, x2=394, y2=529, width = 1, batch = lines, color=(225,165,0))
timer22 = pyglet.shapes.Line(x=421, y=542, x2=500, y2=428, width = 1, batch = lines, color=(225,165,0))
timer23 = pyglet.shapes.Line(x=565, y=454, x2=451, y2=554, width = 1, batch = lines, color=(225,165,0))
timer24 = pyglet.shapes.Line(x=455, y=577, x2=591, y2=508, width = 1, batch = lines, color=(225,165,0))
timer25 = pyglet.shapes.Line(x=611, y=565, x2=458, y2=597, width = 1, batch = lines, color=(225,165,0))
timer26 = pyglet.shapes.Line(x=462, y=624, x2=608, y2=626, width = 1, batch = lines, color=(225,165,0))
timer27 = pyglet.shapes.Line(x=447, y=658, x2=607, y2=697, width = 1, batch = lines, color=(225,165,0))
timer28 = pyglet.shapes.Line(x=425, y=705, x2=589, y2=760, width = 1, batch = lines, color=(225,165,0))
timer29 = pyglet.shapes.Line(x=401, y=752, x2=565, y2=815, width = 1, batch = lines, color=(225,165,0))
timer30 = pyglet.shapes.Line(x=555, y=838, x2=364, y2=833, width = 1, batch = lines, color=(225,165,0))
timer31 = pyglet.shapes.Line(x=555, y=855, x2=384, y2=964, width = 1, batch = lines, color=(225,165,0))
timer32 = pyglet.shapes.Line(x=565, y=863, x2=495, y2=1032, width = 1, batch = lines, color=(225,165,0))
timer33 = pyglet.shapes.Line(x=627, y=1049, x2=571, y2=859, width = 1, batch = lines, color=(225,165,0))
timer34 = pyglet.shapes.Line(x=710, y=993, x2=579, y2=850, width = 1, batch = lines, color=(225,165,0))
timer35 = pyglet.shapes.Line(x=733, y=921, x2=582, y2=839, width = 1, batch = lines, color=(225,165,0))
timer36 = pyglet.shapes.Line(x=584, y=798, x2=751, y2=872, width = 1, batch = lines, color=(225,165,0))
timer37 = pyglet.shapes.Line(x=617, y=742, x2=771, y2=842, width = 1, batch = lines, color=(225,165,0))
timer38 = pyglet.shapes.Line(x=790, y=798, x2=654, y2=700, width = 1, batch = lines, color=(225,165,0))
timer39 = pyglet.shapes.Line(x=801, y=778, x2=724, y2=660, width = 1, batch = lines, color=(225,165,0))
timer40 = pyglet.shapes.Line(x=834, y=774, x2=802, y2=629, width = 1, batch = lines, color=(225,165,0))
timer41 = pyglet.shapes.Line(x=874, y=774, x2=863, y2=635, width = 1, batch = lines, color=(225,165,0))
timer42 = pyglet.shapes.Line(x=897, y=772, x2=944, y2=639, width = 1, batch = lines, color=(225,165,0))
timer43 = pyglet.shapes.Line(x=937, y=793, x2=998, y2=655, width = 1, batch = lines, color=(225,165,0))
timer44 = pyglet.shapes.Line(x=972, y=808, x2=1043, y2=677, width = 1, batch = lines, color=(225,165,0))
timer45 = pyglet.shapes.Line(x=1011, y=826, x2=1083, y2=699, width = 1, batch = lines, color=(225,165,0))
timer46 = pyglet.shapes.Line(x=1049, y=841, x2=1125, y2=720, width = 1, batch = lines, color=(225,165,0))
timer47 = pyglet.shapes.Line(x=1094, y=863, x2=1173, y2=744, width = 1, batch = lines, color=(225,165,0))
timer48 = pyglet.shapes.Line(x=1227, y=770, x2=1145, y2=886, width = 1, batch = lines, color=(225,165,0))
timer49 = pyglet.shapes.Line(x=1198, y=909, x2=1281, y2=798, width = 1, batch = lines, color=(225,165,0))
timer50 = pyglet.shapes.Line(x=1277, y=942, x2=1346, y2=831, width = 1, batch = lines, color=(225,165,0))
timer51 = pyglet.shapes.Line(x=1341, y=970, x2=1398, y2=857, width = 1, batch = lines, color=(225,165,0))
timer52 = pyglet.shapes.Line(x=1384, y=990, x2=1442, y2=877, width = 1, batch = lines, color=(225,165,0))
timer53 = pyglet.shapes.Line(x=1467, y=884, x2=1431, y2=1009, width = 1, batch = lines, color=(225,165,0))
timer54 = pyglet.shapes.Line(x=1486, y=1023, x2=1496, y2=888, width = 1, batch = lines, color=(225,165,0))
timer55 = pyglet.shapes.Line(x=1536, y=893, x2=1537, y2=1023, width = 1, batch = lines, color=(225,165,0))
timer56 = pyglet.shapes.Line(x=1555, y=882, x2=1631, y2=1022, width = 1, batch = lines, color=(225,165,0))
timer57 = pyglet.shapes.Line(x=1697, y=983, x2=1563, y2=873, width = 1, batch = lines, color=(225,165,0))
timer58 = pyglet.shapes.Line(x=1758, y=904, x2=1576, y2=857, width = 1, batch = lines, color=(225,165,0))
timer59 = pyglet.shapes.Line(x=1594, y=837, x2=1763, y2=848, width = 1, batch = lines, color=(225,165,0))
timer60 = pyglet.shapes.Line(x=1761, y=793, x2=1586, y2=810, width = 1, batch = lines, color=(225,165,0))
timer61 = pyglet.shapes.Line(x=1576, y=776, x2=1726, y2=729, width = 1, batch = lines, color=(225,165,0))
timer62 = pyglet.shapes.Line(x=1555, y=749, x2=1688, y2=675, width = 1, batch = lines, color=(225,165,0))
timer63 = pyglet.shapes.Line(x=1633, y=635, x2=1516, y2=720, width = 1, batch = lines, color=(225,165,0))
timer64 = pyglet.shapes.Line(x=1470, y=685, x2=1596, y2=607, width = 1, batch = lines, color=(225,165,0))
timer65 = pyglet.shapes.Line(x=1573, y=587, x2=1415, y2=649, width = 1, batch = lines, color=(225,165,0))
timer66 = pyglet.shapes.Line(x=1563, y=549, x2=1385, y2=601, width = 1, batch = lines, color=(225,165,0))
timer67 = pyglet.shapes.Line(x=1580, y=513, x2=1356, y2=545, width = 1, batch = lines, color=(225,165,0))
timer68 = pyglet.shapes.Line(x=1376, y=462, x2=1595, y2=504, width = 1, batch = lines, color=(225,165,0))
timer69 = pyglet.shapes.Line(x=1434, y=412, x2=1601, y2=504, width = 1, batch = lines, color=(225,165,0))
timer70 = pyglet.shapes.Line(x=1639, y=486, x2=1502, y2=377, width = 1, batch = lines, color=(225,165,0))
timer71 = pyglet.shapes.Line(x=1524, y=365, x2=1709, y2=451, width = 1, batch = lines, color=(225,165,0))
timer72 = pyglet.shapes.Line(x=1525, y=347, x2=1764, y2=391, width = 1, batch = lines, color=(225,165,0))
timer73 = pyglet.shapes.Line(x=1776, y=296, x2=1526, y2=326, width = 1, batch = lines, color=(225,165,0))
timer74 = pyglet.shapes.Line(x=1721, y=219, x2=1526, y2=326, width = 1, batch = lines, color=(225,165,0))
timer75 = pyglet.shapes.Line(x=1516, y=324, x2=1618, y2=203, width = 1, batch = lines, color=(225,165,0))
timer76 = pyglet.shapes.Line(x=1475, y=322, x2=1546, y2=192, width = 1, batch = lines, color=(225,165,0))
timer77 = pyglet.shapes.Line(x=1438, y=317, x2=1493, y2=183, width = 1, batch = lines, color=(225,165,0))
timer78 = pyglet.shapes.Line(x=1389, y=309, x2=1433, y2=175, width = 1, batch = lines, color=(225,165,0))
timer79 = pyglet.shapes.Line(x=1350, y=302, x2=1367, y2=166, width = 1, batch = lines, color=(225,165,0))
timer80 = pyglet.shapes.Line(x=1283, y=296, x2=1315, y2=156, width = 1, batch = lines, color=(225,165,0))
timer81 = pyglet.shapes.Line(x=1208, y=286, x2=1256, y2=149, width = 1, batch = lines, color=(225,165,0))
timer82 = pyglet.shapes.Line(x=1162, y=278, x2=1200, y2=140, width = 1, batch = lines, color=(225,165,0))
timer83 = pyglet.shapes.Line(x=1108, y=270, x2=1148, y2=131, width = 1, batch = lines, color=(225,165,0))
timer84 = pyglet.shapes.Line(x=1048, y=262, x2=1101, y2=125, width = 1, batch = lines, color=(225,165,0))
timer85 = pyglet.shapes.Line(x=1020, y=258, x2=1054, y2=117, width = 1, batch = lines, color=(225,165,0))



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
line25 = pyglet.shapes.Line(x=269, y=478, x2=211, y2=370, width = 1, batch = lines)
line26 = pyglet.shapes.Line(x=211, y=370, x2=207, y2=245, width = 1, batch = lines)
line27 = pyglet.shapes.Line(x=207, y=245, x2=278, y2=98, width = 1, batch = lines)
line28 = pyglet.shapes.Line(x=278, y=98, x2=355, y2=36, width = 1, batch = lines)
line29 = pyglet.shapes.Line(x=355, y=36, x2=472, y2=23, width = 1, batch = lines)

#inside lines
line30 = pyglet.shapes.Line(x=470, y=181, x2=1525, y2=325, width = 1, batch = lines)
line31 = pyglet.shapes.Line(x=1525, y=325, x2=1526, y2=363, width = 1, batch = lines)
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
line54 = pyglet.shapes.Line(x=400, y=364, x2=383, y2=277, width = 1, batch = lines)
line55 = pyglet.shapes.Line(x=383, y=277, x2=404, y2=217, width = 1, batch = lines)
line56 = pyglet.shapes.Line(x=404, y=217, x2=470, y2=181, width = 1, batch = lines)

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

lapCompleted = False

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
  displays.draw()
  #lap_displays() this function is commented out since it was causing lag
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
    max_velocity = 8

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