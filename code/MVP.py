#importing variables
import pyglet
import time
import random
import sqlite3
import datetime
import threading
from datetime import datetime
from pyglet import sprite, image
from pyglet.window import key, mouse
from math import sin, cos, atan, acos, asin, radians, sqrt, tanh

#batches
wall_lines = pyglet.graphics.Batch()
gate_lines = pyglet.graphics.Batch()

#loading in custom font - Zen Dots
pyglet.font.add_file('ZenDots-Regular.ttf')

#scale_factor = (windowwidth/1920)%1

windowwidth, windowheight, scale_factor = 1440, 900, 0.75

#creating all of the walls
def get_walls(window_width, window_height):
    line = pyglet.shapes.Line(x=472/1920 * window_width, y=23/1080 * window_height, x2=1723/1920 * window_width, y2=217/1080 * window_height, width = 1)
    line1 = pyglet.shapes.Line(x=1723/1920 * window_width, y=217/1080 * window_height, x2=1777/1920 * window_width, y2=295/1080 * window_height, width = 1)
    line2 = pyglet.shapes.Line(x=1777/1920 * window_width, y=295/1080 * window_height, x2=1764/1920 * window_width, y2=392/1080 * window_height, width = 1)
    line3 = pyglet.shapes.Line(x=1764/1920 * window_width, y=392/1080 * window_height, x2=1704/1920 * window_width, y2=459/1080 * window_height, width = 1)
    line4 = pyglet.shapes.Line(x=1704/1920 * window_width, y=459/1080 * window_height, x2=1580/1920 * window_width, y2=510/1080 * window_height, width = 1)
    line5 = pyglet.shapes.Line(x=1580/1920 * window_width, y=510/1080 * window_height, x2=1562/1920 * window_width, y2=548/1080 * window_height, width = 1)
    line6 = pyglet.shapes.Line(x=1562/1920 * window_width, y=548/1080 * window_height, x2=1571/1920 * window_width, y2=584/1080 * window_height, width = 1)
    line7 = pyglet.shapes.Line(x=1571/1920 * window_width, y=584/1080 * window_height, x2=1707/1920 * window_width, y2=690/1080 * window_height, width = 1)
    line8 = pyglet.shapes.Line(x=1707/1920 * window_width, y=690/1080 * window_height, x2=1765/1920 * window_width, y2=800/1080 * window_height, width = 1)
    line9 = pyglet.shapes.Line(x=1765/1920 * window_width, y=800/1080 * window_height, x2=1760/1920 * window_width, y2=901/1080 * window_height, width = 1)
    line10 = pyglet.shapes.Line(x=1760/1920 * window_width, y=901/1080 * window_height, x2=1696/1920 * window_width, y2=984/1080 * window_height, width = 1)
    line11 = pyglet.shapes.Line(x=1696/1920 * window_width, y=984/1080 * window_height, x2=1632/1920 * window_width, y2=1021/1080 * window_height, width = 1)
    line12 = pyglet.shapes.Line(x=1632/1920 * window_width, y=1021/1080 * window_height, x2=1462/1920 * window_width, y2=1022/1080 * window_height, width = 1)
    line13 = pyglet.shapes.Line(x=1462/1920 * window_width, y=1022/1080 * window_height, x2=1193/1920 * window_width, y2=906/1080 * window_height, width = 1)
    line14 = pyglet.shapes.Line(x=1193/1920 * window_width, y=906/1080 * window_height, x2=892/1920 * window_width, y2=771/1080 * window_height, width = 1)
    line15 = pyglet.shapes.Line(x=892/1920 * window_width, y=771/1080 * window_height, x2=802/1920 * window_width, y2=777/1080 * window_height, width = 1)
    line16 = pyglet.shapes.Line(x=802/1920 * window_width, y=777/1080 * window_height, x2=746/1920 * window_width, y2=883/1080 * window_height, width = 1)
    line17 = pyglet.shapes.Line(x=746/1920 * window_width, y=883/1080 * window_height, x2=711/1920 * window_width, y2=995/1080 * window_height, width = 1)
    line18 = pyglet.shapes.Line(x=711/1920 * window_width, y=995/1080 * window_height, x2=628/1920 * window_width, y2=1050/1080 * window_height, width = 1)
    line19 = pyglet.shapes.Line(x=628/1920 * window_width, y=1050/1080 * window_height, x2=494/1920 * window_width, y2=1031/1080 * window_height, width = 1)
    line20 = pyglet.shapes.Line(x=494/1920 * window_width, y=1031/1080 * window_height, x2=384/1920 * window_width, y2=964/1080 * window_height, width = 1)
    line21 = pyglet.shapes.Line(x=384/1920 * window_width, y=964/1080 * window_height, x2=364/1920 * window_width, y2=832/1080 * window_height, width = 1)
    line22 = pyglet.shapes.Line(x=364/1920 * window_width, y=832/1080 * window_height, x2=462/1920 * window_width, y2=624/1080 * window_height, width = 1)
    line23 = pyglet.shapes.Line(x=462/1920 * window_width, y=624/1080 * window_height, x2=453/1920 * window_width, y2=555/1080 * window_height, width = 1)
    line24 = pyglet.shapes.Line(x=453/1920 * window_width, y=555/1080 * window_height, x2=269/1920 * window_width, y2=478/1080 * window_height, width = 1)
    line25 = pyglet.shapes.Line(x=269/1920 * window_width, y=478/1080 * window_height, x2=211/1920 * window_width, y2=370/1080 * window_height, width = 1)
    line26 = pyglet.shapes.Line(x=211/1920 * window_width, y=370/1080 * window_height, x2=207/1920 * window_width, y2=245/1080 * window_height, width = 1)
    line27 = pyglet.shapes.Line(x=207/1920 * window_width, y=245/1080 * window_height, x2=278/1920 * window_width, y2=98/1080 * window_height, width = 1)
    line28 = pyglet.shapes.Line(x=278/1920 * window_width, y=98/1080 * window_height, x2=355/1920 * window_width, y2=36/1080 * window_height, width = 1)
    line29 = pyglet.shapes.Line(x=355/1920 * window_width, y=36/1080 * window_height, x2=472/1920 * window_width, y2=23/1080 * window_height, width = 1)

    #inside lines
    line30 = pyglet.shapes.Line(x=470/1920 *window_width, y=181/1080 *window_height, x2=1525/1920 *window_width, y2=325/1080 *window_height, width = 1)
    line31 = pyglet.shapes.Line(x=1525/1920 *window_width, y=325/1080 *window_height, x2=1526/1920 *window_width, y2=363/1080 *window_height, width = 1)
    line32 = pyglet.shapes.Line(x=1526/1920 *window_width, y=363/1080 *window_height, x2=1383/1920 *window_width, y2=435/1080 *window_height, width = 1)
    line33 = pyglet.shapes.Line(x=1383/1920 *window_width, y=435/1080 *window_height, x2=1354/1920 *window_width, y2=554/1080 *window_height, width = 1)
    line34 = pyglet.shapes.Line(x=1354/1920 *window_width, y=554/1080 *window_height, x2=1414/1920 *window_width, y2=644/1080 *window_height, width = 1)
    line35 = pyglet.shapes.Line(x=1414/1920 *window_width, y=644/1080 *window_height, x2=1569/1920 *window_width, y2=758/1080 *window_height, width = 1)
    line36 = pyglet.shapes.Line(x=1569/1920 *window_width, y=758/1080 *window_height, x2=1596/1920 *window_width, y2=838/1080 *window_height, width = 1)
    line37 = pyglet.shapes.Line(x=1596/1920 *window_width, y=838/1080 *window_height, x2=1545/1920 *window_width, y2=891/1080 *window_height, width = 1)
    line38 = pyglet.shapes.Line(x=1545/1920 *window_width, y=891/1080 *window_height, x2=1457/1920 *window_width, y2=882/1080 *window_height, width = 1)
    line39 = pyglet.shapes.Line(x=1457/1920 *window_width, y=882/1080 *window_height, x2=969/1920 *window_width, y2=639/1080 *window_height, width = 1)
    line40 = pyglet.shapes.Line(x=969/1920 *window_width, y=639/1080 *window_height, x2=801/1920 *window_width, y2=629/1080 *window_height, width = 1)
    line41 = pyglet.shapes.Line(x=801/1920 *window_width, y=629/1080 *window_height, x2=676/1920 *window_width, y2=676/1080 *window_height, width = 1)
    line42 = pyglet.shapes.Line(x=676/1920 *window_width, y=676/1080 *window_height, x2=618/1920 *window_width, y2=739/1080 *window_height, width = 1)
    line43 = pyglet.shapes.Line(x=618/1920 *window_width, y=739/1080 *window_height, x2=585/1920 *window_width, y2=793/1080 *window_height, width = 1)
    line44 = pyglet.shapes.Line(x=585/1920 *window_width, y=793/1080 *window_height, x2=581/1920 *window_width, y2=848/1080 *window_height, width = 1)
    line45 = pyglet.shapes.Line(x=581/1920 *window_width, y=848/1080 *window_height, x2=566/1920 *window_width, y2=864/1080 *window_height, width = 1)
    line46 = pyglet.shapes.Line(x=566/1920 *window_width, y=864/1080 *window_height, x2=555/1920 *window_width, y2=854/1080 *window_height, width = 1)
    line47 = pyglet.shapes.Line(x=555/1920 *window_width, y=854/1080 *window_height, x2=554/1920 *window_width, y2=840/1080 *window_height, width = 1)
    line48 = pyglet.shapes.Line(x=554/1920 *window_width, y=840/1080 *window_height, x2=581/1920 *window_width, y2=785/1080 *window_height, width = 1)
    line49 = pyglet.shapes.Line(x=581/1920 *window_width, y=785/1080 *window_height, x2=608/1920 *window_width, y2=697/1080 *window_height, width = 1)
    line50 = pyglet.shapes.Line(x=608/1920 *window_width, y=697/1080 *window_height, x2=612/1920 *window_width, y2=548/1080 *window_height, width = 1)
    line51 = pyglet.shapes.Line(x=612/1920 *window_width, y=548/1080 *window_height, x2=565/1920 *window_width, y2=452/1080 *window_height, width = 1)
    line52 = pyglet.shapes.Line(x=565/1920 *window_width, y=452/1080 *window_height, x2=440/1920 *window_width, y2=399/1080 *window_height, width = 1)
    line53 = pyglet.shapes.Line(x=440/1920 *window_width, y=399/1080 *window_height, x2=400/1920 *window_width, y2=364/1080 *window_height, width = 1)
    line54 = pyglet.shapes.Line(x=400/1920 *window_width, y=364/1080 *window_height, x2=383/1920 *window_width, y2=277/1080 *window_height, width = 1)
    line55 = pyglet.shapes.Line(x=383/1920 *window_width, y=277/1080 *window_height, x2=404/1920 *window_width, y2=217/1080 *window_height, width = 1)
    line56 = pyglet.shapes.Line(x=404/1920 *window_width, y=217/1080 *window_height, x2=470/1920 *window_width, y2=181/1080 *window_height, width = 1)

    barrierLineList = [line, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15, line16, line17, line18, line19, line20, line21, line22, line23, line24, line25, line26, line27, line28, line29, line30, line31, line32, line33, line34, line35, line36, line37, line38, line39, line40, line41, line42, line43, line44, line45, line46, line47, line48, line49, line50, line51, line52, line53, line54, line55, line56]
    return barrierLineList

#creating all of the reward gates
def get_gates(window_width, window_height):
    global timer1
    timer1 = pyglet.shapes.Line(x=995/1920 *window_width, y=102/1080 *window_height, x2=985/1920 *window_width, y2=250/1080 *window_height, width = 1, color=(255,165,0))
    timer2 = pyglet.shapes.Line(x=939/1920 *window_width, y=246/1080 *window_height, x2=947/1920 *window_width, y2=98/1080 *window_height, width = 1, color=(255,165,0))
    timer3 = pyglet.shapes.Line(x=889/1920 *window_width, y=239/1080 *window_height, x2=898/1920 *window_width, y2=91/1080 *window_height, width = 1, color=(225,165,0))
    timer4 = pyglet.shapes.Line(x=838/1920 *window_width, y=233/1080 *window_height, x2=844/1920 *window_width, y2=82/1080 *window_height, width = 1, color=(225,165,0))
    timer5 = pyglet.shapes.Line(x=789/1920 *window_width, y=225/1080 *window_height, x2=793/1920 *window_width, y2=75/1080 *window_height, width = 1, color=(225,165,0))
    timer6 = pyglet.shapes.Line(x=733/1920 *window_width, y=218/1080 *window_height, x2=742/1920 *window_width, y2=66/1080 *window_height, width = 1, color=(225,165,0))
    timer7 = pyglet.shapes.Line(x=682/1920 *window_width, y=210/1080 *window_height, x2=690/1920 *window_width, y2=58/1080 *window_height, width = 1, color=(225,165,0))
    timer8 = pyglet.shapes.Line(x=631/1920 *window_width, y=204/1080 *window_height, x2=637/1920 *window_width, y2=50/1080 *window_height, width = 1, color=(225,165,0))
    timer9 = pyglet.shapes.Line(x=584/1920 *window_width, y=198/1080 *window_height, x2=590/1920 *window_width, y2=43/1080 *window_height, width = 1, color=(225,165,0))
    timer10 = pyglet.shapes.Line(x=532/1920 *window_width, y=191/1080 *window_height, x2=542/1920 *window_width, y2=34/1080 *window_height, width = 1, color=(225,165,0))
    timer11 = pyglet.shapes.Line(x=476/1920 *window_width, y=183/1080 *window_height, x2=479/1920 *window_width, y2=26/1080 *window_height, width = 1, color=(225,165,0))
    timer12 = pyglet.shapes.Line(x=437/1920 *window_width, y=198/1080 *window_height, x2=381/1920 *window_width, y2=34/1080 *window_height, width = 1, color=(225,165,0))
    timer13 = pyglet.shapes.Line(x=402/1920 *window_width, y=217/1080 *window_height, x2=308/1920 *window_width, y2=74/1080 *window_height, width = 1, color=(225,165,0))
    timer14 = pyglet.shapes.Line(x=397/1920 *window_width, y=234/1080 *window_height, x2=253/1920 *window_width, y2=147/1080 *window_height, width = 1, color=(225,165,0))
    timer15 = pyglet.shapes.Line(x=386/1920 *window_width, y=268/1080 *window_height, x2=213/1920 *window_width, y2=229/1080 *window_height, width = 1, color=(225,165,0))
    timer16 = pyglet.shapes.Line(x=198/1920 *window_width, y=300/1080 *window_height, x2=390/1920 *window_width, y2=314/1080 *window_height, width = 1, color=(225,165,0))
    timer17 = pyglet.shapes.Line(x=393/1920 *window_width, y=338/1080 *window_height, x2=210/1920 *window_width, y2=371/1080 *window_height, width = 1, color=(225,165,0))
    timer18 = pyglet.shapes.Line(x=401/1920 *window_width, y=365/1080 *window_height, x2=243/1920 *window_width, y2=430/1080 *window_height, width = 1, color=(225,165,0))
    timer19 = pyglet.shapes.Line(x=422/1920 *window_width, y=384/1080 *window_height, x2=270/1920 *window_width, y2=480/1080 *window_height, width = 1, color=(225,165,0))
    timer20 = pyglet.shapes.Line(x=442/1920 *window_width, y=400/1080 *window_height, x2=337/1920 *window_width, y2=508/1080 *window_height, width = 1, color=(225,165,0))
    timer21 = pyglet.shapes.Line(x=467/1920 *window_width, y=412/1080 *window_height, x2=394/1920 *window_width, y2=529/1080 *window_height, width = 1, color=(225,165,0))
    timer22 = pyglet.shapes.Line(x=421/1920 *window_width, y=542/1080 *window_height, x2=500/1920 *window_width, y2=428/1080 *window_height, width = 1, color=(225,165,0))
    timer23 = pyglet.shapes.Line(x=565/1920 *window_width, y=454/1080 *window_height, x2=451/1920 *window_width, y2=554/1080 *window_height, width = 1, color=(225,165,0))
    timer24 = pyglet.shapes.Line(x=455/1920 *window_width, y=577/1080 *window_height, x2=591/1920 *window_width, y2=508/1080 *window_height, width = 1, color=(225,165,0))
    timer25 = pyglet.shapes.Line(x=611/1920 *window_width, y=565/1080 *window_height, x2=458/1920 *window_width, y2=597/1080 *window_height, width = 1, color=(225,165,0))
    timer26 = pyglet.shapes.Line(x=462/1920 *window_width, y=624/1080 *window_height, x2=608/1920 *window_width, y2=626/1080 *window_height, width = 1, color=(225,165,0))
    timer27 = pyglet.shapes.Line(x=447/1920 *window_width, y=658/1080 *window_height, x2=607/1920 *window_width, y2=697/1080 *window_height, width = 1, color=(225,165,0))
    timer28 = pyglet.shapes.Line(x=425/1920 *window_width, y=705/1080 *window_height, x2=589/1920 *window_width, y2=760/1080 *window_height, width = 1, color=(225,165,0))
    timer29 = pyglet.shapes.Line(x=401/1920 *window_width, y=752/1080 *window_height, x2=565/1920 *window_width, y2=815/1080 *window_height, width = 1, color=(225,165,0))
    timer30 = pyglet.shapes.Line(x=555/1920 *window_width, y=838/1080 *window_height, x2=364/1920 *window_width, y2=833/1080 *window_height, width = 1, color=(225,165,0))
    timer31 = pyglet.shapes.Line(x=555/1920 *window_width, y=855/1080 *window_height, x2=384/1920 *window_width, y2=964/1080 *window_height, width = 1, color=(225,165,0))
    timer32 = pyglet.shapes.Line(x=565/1920 *window_width, y=863/1080 *window_height, x2=495/1920 *window_width, y2=1032/1080 *window_height, width = 1, color=(225,165,0))
    timer33 = pyglet.shapes.Line(x=627/1920 *window_width, y=1049/1080 *window_height, x2=571/1920 *window_width, y2=859/1080 *window_height, width = 1, color=(225,165,0))
    timer34 = pyglet.shapes.Line(x=710/1920 *window_width, y=993/1080 *window_height, x2=579/1920 *window_width, y2=850/1080 *window_height, width = 1, color=(225,165,0))
    timer35 = pyglet.shapes.Line(x=733/1920 *window_width, y=921/1080 *window_height, x2=582/1920 *window_width, y2=839/1080 *window_height, width = 1, color=(225,165,0))
    timer36 = pyglet.shapes.Line(x=584/1920 *window_width, y=798/1080 *window_height, x2=751/1920 *window_width, y2=872/1080 *window_height, width = 1, color=(225,165,0))
    timer37 = pyglet.shapes.Line(x=617/1920 *window_width, y=742/1080 *window_height, x2=771/1920 *window_width, y2=842/1080 *window_height, width = 1, color=(225,165,0))
    timer38 = pyglet.shapes.Line(x=790/1920 *window_width, y=798/1080 *window_height, x2=654/1920 *window_width, y2=700/1080 *window_height, width = 1, color=(225,165,0))
    timer39 = pyglet.shapes.Line(x=801/1920 *window_width, y=778/1080 *window_height, x2=724/1920 *window_width, y2=660/1080 *window_height, width = 1, color=(225,165,0))
    timer40 = pyglet.shapes.Line(x=834/1920 *window_width, y=774/1080 *window_height, x2=802/1920 *window_width, y2=629/1080 *window_height, width = 1, color=(225,165,0))
    timer41 = pyglet.shapes.Line(x=874/1920 *window_width, y=774/1080 *window_height, x2=863/1920 *window_width, y2=635/1080 *window_height, width = 1, color=(225,165,0))
    timer42 = pyglet.shapes.Line(x=897/1920 *window_width, y=772/1080 *window_height, x2=944/1920 *window_width, y2=639/1080 *window_height, width = 1, color=(225,165,0))
    timer43 = pyglet.shapes.Line(x=937/1920 *window_width, y=793/1080 *window_height, x2=998/1920 *window_width, y2=655/1080 *window_height, width = 1, color=(225,165,0))
    timer44 = pyglet.shapes.Line(x=972/1920 *window_width, y=808/1080 *window_height, x2=1043/1920 *window_width, y2=677/1080 *window_height, width = 1, color=(225,165,0))
    timer45 = pyglet.shapes.Line(x=1011/1920 *window_width, y=826/1080 *window_height, x2=1083/1920 *window_width, y2=699/1080 *window_height, width = 1, color=(225,165,0))
    timer46 = pyglet.shapes.Line(x=1049/1920 *window_width, y=841/1080 *window_height, x2=1125/1920 *window_width, y2=720/1080 *window_height, width = 1, color=(225,165,0))
    timer47 = pyglet.shapes.Line(x=1094/1920 *window_width, y=863/1080 *window_height, x2=1173/1920 *window_width, y2=744/1080 *window_height, width = 1, color=(225,165,0))
    timer48 = pyglet.shapes.Line(x=1227/1920 *window_width, y=770/1080 *window_height, x2=1145/1920 *window_width, y2=886/1080 *window_height, width = 1, color=(225,165,0))
    timer49 = pyglet.shapes.Line(x=1198/1920 *window_width, y=909/1080 *window_height, x2=1281/1920 *window_width, y2=798/1080 *window_height, width = 1, color=(225,165,0))
    timer50 = pyglet.shapes.Line(x=1277/1920 *window_width, y=942/1080 *window_height, x2=1346/1920 *window_width, y2=831/1080 *window_height, width = 1, color=(225,165,0))
    timer51 = pyglet.shapes.Line(x=1341/1920 *window_width, y=970/1080 *window_height, x2=1398/1920 *window_width, y2=857/1080 *window_height, width = 1, color=(225,165,0))
    timer52 = pyglet.shapes.Line(x=1384/1920 *window_width, y=990/1080 *window_height, x2=1442/1920 *window_width, y2=877/1080 *window_height, width = 1, color=(225,165,0))
    timer53 = pyglet.shapes.Line(x=1467/1920 *window_width, y=884/1080 *window_height, x2=1431/1920 *window_width, y2=1009/1080 *window_height, width = 1, color=(225,165,0))
    timer54 = pyglet.shapes.Line(x=1486/1920 *window_width, y=1023/1080 *window_height, x2=1496/1920 *window_width, y2=888/1080 *window_height, width = 1, color=(225,165,0))
    timer55 = pyglet.shapes.Line(x=1536/1920 *window_width, y=893/1080 *window_height, x2=1537/1920 *window_width, y2=1023/1080 *window_height, width = 1, color=(225,165,0))
    timer56 = pyglet.shapes.Line(x=1555/1920 *window_width, y=882/1080 *window_height, x2=1631/1920 *window_width, y2=1022/1080 *window_height, width = 1, color=(225,165,0))
    timer57 = pyglet.shapes.Line(x=1697/1920 *window_width, y=983/1080 *window_height, x2=1563/1920 *window_width, y2=873/1080 *window_height, width = 1, color=(225,165,0))
    timer58 = pyglet.shapes.Line(x=1758/1920 *window_width, y=904/1080 *window_height, x2=1576/1920 *window_width, y2=857/1080 *window_height, width = 1, color=(225,165,0))
    timer59 = pyglet.shapes.Line(x=1594/1920 *window_width, y=837/1080 *window_height, x2=1763/1920 *window_width, y2=848/1080 *window_height, width = 1, color=(225,165,0))
    timer60 = pyglet.shapes.Line(x=1761/1920 *window_width, y=793/1080 *window_height, x2=1586/1920 *window_width, y2=810/1080 *window_height, width = 1, color=(225,165,0))
    timer61 = pyglet.shapes.Line(x=1576/1920 *window_width, y=776/1080 *window_height, x2=1726/1920 *window_width, y2=729/1080 *window_height, width = 1, color=(225,165,0))
    timer62 = pyglet.shapes.Line(x=1555/1920 *window_width, y=749/1080 *window_height, x2=1688/1920 *window_width, y2=675/1080 *window_height, width = 1, color=(225,165,0))
    timer63 = pyglet.shapes.Line(x=1633/1920 *window_width, y=635/1080 *window_height, x2=1516/1920 *window_width, y2=720/1080 *window_height, width = 1, color=(225,165,0))
    timer64 = pyglet.shapes.Line(x=1470/1920 *window_width, y=685/1080 *window_height, x2=1596/1920 *window_width, y2=607/1080 *window_height, width = 1, color=(225,165,0))
    timer65 = pyglet.shapes.Line(x=1573/1920 *window_width, y=587/1080 *window_height, x2=1415/1920 *window_width, y2=649/1080 *window_height, width = 1, color=(225,165,0))
    timer66 = pyglet.shapes.Line(x=1563/1920 *window_width, y=549/1080 *window_height, x2=1385/1920 *window_width, y2=601/1080 *window_height, width = 1, color=(225,165,0))
    timer67 = pyglet.shapes.Line(x=1580/1920 *window_width, y=513/1080 *window_height, x2=1356/1920 *window_width, y2=545/1080 *window_height, width = 1, color=(225,165,0))
    timer68 = pyglet.shapes.Line(x=1376/1920 *window_width, y=462/1080 *window_height, x2=1595/1920 *window_width, y2=504/1080 *window_height, width = 1, color=(225,165,0))
    timer69 = pyglet.shapes.Line(x=1434/1920 *window_width, y=412/1080 *window_height, x2=1601/1920 *window_width, y2=504/1080 *window_height, width = 1, color=(225,165,0))
    timer70 = pyglet.shapes.Line(x=1639/1920 *window_width, y=486/1080 *window_height, x2=1502/1920 *window_width, y2=377/1080 *window_height, width = 1, color=(225,165,0))
    timer71 = pyglet.shapes.Line(x=1524/1920 *window_width, y=365/1080 *window_height, x2=1709/1920 *window_width, y2=451/1080 *window_height, width = 1, color=(225,165,0))
    timer72 = pyglet.shapes.Line(x=1525/1920 *window_width, y=347/1080 *window_height, x2=1764/1920 *window_width, y2=391/1080 *window_height, width = 1, color=(225,165,0))
    timer73 = pyglet.shapes.Line(x=1776/1920 *window_width, y=296/1080 *window_height, x2=1526/1920 *window_width, y2=326/1080 *window_height, width = 1, color=(225,165,0))
    timer74 = pyglet.shapes.Line(x=1721/1920 *window_width, y=219/1080 *window_height, x2=1526/1920 *window_width, y2=326/1080 *window_height, width = 1, color=(225,165,0))
    timer75 = pyglet.shapes.Line(x=1516/1920 *window_width, y=324/1080 *window_height, x2=1618/1920 *window_width, y2=203/1080 *window_height, width = 1, color=(225,165,0))
    timer76 = pyglet.shapes.Line(x=1475/1920 *window_width, y=322/1080 *window_height, x2=1546/1920 *window_width, y2=192/1080 *window_height, width = 1, color=(225,165,0))
    timer77 = pyglet.shapes.Line(x=1438/1920 *window_width, y=317/1080 *window_height, x2=1493/1920 *window_width, y2=183/1080 *window_height, width = 1, color=(225,165,0))
    timer78 = pyglet.shapes.Line(x=1389/1920 *window_width, y=309/1080 *window_height, x2=1433/1920 *window_width, y2=175/1080 *window_height, width = 1, color=(225,165,0))
    timer79 = pyglet.shapes.Line(x=1350/1920 *window_width, y=302/1080 *window_height, x2=1367/1920 *window_width, y2=166/1080 *window_height, width = 1, color=(225,165,0))
    timer80 = pyglet.shapes.Line(x=1283/1920 *window_width, y=296/1080 *window_height, x2=1315/1920 *window_width, y2=156/1080 *window_height, width = 1, color=(225,165,0))
    timer81 = pyglet.shapes.Line(x=1208/1920 *window_width, y=286/1080 *window_height, x2=1256/1920 *window_width, y2=149/1080 *window_height, width = 1, color=(225,165,0))
    timer82 = pyglet.shapes.Line(x=1108/1920 *window_width, y=270/1080 *window_height, x2=1148/1920 *window_width, y2=131/1080 *window_height, width = 1, color=(225,165,0))
    timer83 = pyglet.shapes.Line(x=1020/1920 *window_width, y=258/1080 *window_height, x2=1054/1920 *window_width, y2=117/1080 *window_height, width = 1, color=(225,165,0))

    gates = [timer1, timer2, timer3, timer4, timer5, timer6, timer7, timer8, timer9, timer10, timer11, timer12, timer13, timer14, timer15, timer16, timer17, timer18, timer19, timer20, timer21, timer22, timer23, timer24, timer25, timer26, timer27, timer28, timer29, timer30, timer31, timer32, timer33, timer34, timer35, timer36, timer37, timer38, timer39, timer40, timer41, timer42, timer43, timer44, timer45, timer46, timer47, timer48, timer49, timer50, timer51, timer52, timer53, timer54, timer55, timer56, timer57, timer58, timer59, timer60, timer61, timer62, timer63, timer64, timer65, timer66, timer67, timer68, timer69, timer70, timer71, timer72, timer73, timer74, timer75, timer76, timer77, timer78, timer79, timer80, timer81, timer82, timer83] 
    return gates

#distance between two points function
def distance_points(point1,point2):
  x1 = point1[0]
  y1 = point1[1]
  x2 = point2[0]
  y2 = point2[1]
  distance = sqrt((x2-x1)**2+(y2-y1)**2)
  return distance

#gradient between two points function
def grad_points(point1,point2):
  x1 = point1[0]
  y1 = point1[1]
  x2 = point2[0]
  y2 = point2[1]
  m = (y2-y1)/(x2-x1)
  return m

#co-ordinates of the midpoint of a line
def midpoint(line):
  midpointX = (line.x + line.x2)//2
  midpointY = (line.y + line.y2)//2
  return midpointX, midpointY

#if the AI can only output a single digit then this function is used to convert it
def chooseAction(x):
    if x == 0:
        action = [True, False, False, False, False]
    elif x == 1:
        action = [True, False, False, False, True]
    elif x == 2:
        action = [True, False, True, False, False]
    elif x == 3:
        action = [True, False, True, False, True]
    elif x == 4:
        action = [True, False, False, True, False]
    elif x == 5:
        action = [True, False, False, True, True]
    elif x == 6:
        action = [False, True, False, False, False]
    elif x == 7:
        action = [False, True, True, False, False]
    elif x == 8:
        action = [False, True, False, True, False]
    elif x == 9:
        action = [False, False, False, False, False]
    elif x == 10:
        action = [False, False, False, False, True]
    elif x == 11:
        action = [False, False, True, False, False]
    elif x == 12:
        action = [False, False, True, False, True]
    elif x == 13:
        action = [False, False, False, True, False]
    elif x == 14:
        action = [False, False, False, True, True]
    else:
        action = x
    return action

walls = get_walls(windowwidth, windowheight)
for wall in walls:
    wall.batch = wall_lines

gates = get_gates(windowwidth, windowheight)
for gate in gates:
    gate.batch = gate_lines

line_list = walls + gates

#sorts the actions data by date range
def select_values(target_string, start_date, end_date):
    connection = sqlite3.connect("data2.db")
    cursor = connection.cursor()
    # Convert the dates to the format YYYY-MM-DD for comparison
    start_date_conv = datetime.strptime(start_date, "%d-%m-%Y").strftime("%Y-%m-%d")
    end_date_conv = datetime.strptime(end_date, "%d-%m-%Y").strftime("%Y-%m-%d")
    
    cursor.execute("""
    SELECT * FROM actions
    WHERE action_type = '{}'
    AND date(substr(date, 7, 4) || '-' || substr(date, 4, 2) || '-' || substr(date, 1, 2))
    BETWEEN date('{}') AND date('{}');
    """.format(target_string, start_date_conv, end_date_conv))
    
    new_data = cursor.fetchall()
    
    return new_data

#admin function for managing changes to the database
def adminFunction():
    print("                         ------ WELCOME ADMIN ------                          ")
    print()
    print("Here you can view flow through the app and quantity of changes to the database")
    print()
    start_date = input("Enter starting date of time range (DD-MM-YYY): ")
    end_date = input("Enter ending date of time range (DD-MM-YYY): ")

    a = len(select_values("create_account",start_date,end_date))
    b = len(select_values("delete_account",start_date,end_date))
    c = len(select_values("update_password",start_date, end_date))
    d = len(select_values("update_lap_time",start_date, end_date))

    print()
    print()
    print("Categories:")
    print("Account Creations: ", a)
    print("Account Deletions: ", b)
    print("Password Updates: ", c)
    print("Lap Updates: ", d)

    print()
    if input("Type 1 to redo: ") == "1":
        adminFunction()

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

    def start(self):
        if not self.running:
            # Only set the start time to current time without adjusting for elapsed_time
            self.start_time = time.time()
            self.running = True

    def stop(self):
        if self.running:
            # Save the total elapsed time without resetting
            self.elapsed_time += time.time() - self.start_time
            self.running = False

    def reset(self):
        self.elapsed_time = 0
        self.start_time = None
        self.running = False

    def lap(self, listt):
        if self.running:
            # Calculate the lap time based on total elapsed time
            current_elapsed = self.elapsed_time + (time.time() - self.start_time)
            listt.append(float("{:.2f}".format(current_elapsed)))
            # Restart the lap timer
            self.start_time = time.time()
            self.elapsed_time = 0  # Reset accumulated time after lap

    def get_time(self):
        if self.running:
            # Add the current running time to previously accumulated elapsed time
            current_elapsed = self.elapsed_time + (time.time() - self.start_time)
            return "{:.2f}".format(current_elapsed)
        # Return accumulated elapsed time if stopped
        return "{:.2f}".format(self.elapsed_time)


class Car:
    def __init__(self,x,y,r,img, forward, backward, left, right, drift): #x,y is the start position of the car, r is the start rotation of the car
        #setting up the car sprite and image
        self.car_image = image.load(img)

        self.car_image.anchor_x = self.car_image.width// 2
        self.car_image.anchor_y = self.car_image.height // 2

        self.car = sprite.Sprite(self.car_image, x, y)
        self.car.scale = 0.1*scale_factor
        
        self.car.rotation = r

        #keys for the direction of the car
        self.forward_key = forward
        self.backward_key = backward
        self.left_key = left
        self.right_key = right
        self.drift_key = drift

        #variables and booleans which determine the cars movement
        self.forward = False
        self.backward = False
        self.clockwise = False
        self.aclockwise = False
        self.drift = False

        self.action_list = [self.forward, self.backward, self.clockwise, self.aclockwise, self.drift]

        self.velocity = 0 *scale_factor
        self.max_velocity = 8 *scale_factor
        self.friction = 0.07 *scale_factor
        self.acceleration = 0.1 *scale_factor
        self.rotation_speed = 3
        self.drift_time = 8 *scale_factor

        self.sprite_hitbox = [(0,0),(0,0),(0,0),(0,0)]

        self.reward_gate = False
        self.wall_collision = False
        self.collList = []
        self.checkerList = []

        self.backDict = {}
        self.rounds = 0

        #Booleans for timing
        self.noStart = False
        self.started = False
        self.swap = False
        self.going = False
        self.lapCompleted = False
        self.new_gate_signal = False
        self.going = 0
        self.start = 0
        self.elapsed = 0
        self.total_lap_time = 0

        self.lap_list = []
        self.timer = Stopwatch()

        for x in gates:
            self.checkerList.append(False)

        #constants for later use
        self.half_width_car = (self.car_image.width)*scale_factor // 20
        self.half_height_car = (self.car_image.height)*scale_factor// 20
        self.h = sqrt(self.half_width_car**2 + self.half_height_car**2)
        self.angle = atan(self.half_width_car/self.half_height_car) - radians(self.car.rotation)

        #defining things for the AI
        self.lineLength = 100000000
        self.oldCollisionPointsList = [(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y)]

        #defining the first observation space
        self.observation_space = [0.0, 260, 0.0, 540.7883010831061, 248.6026368207048, 122.23394041784448, 84.87471813575465, 68.58619476103772, 58.57323663106676, 80.89115626007674, 575.4958984540862, 89.799454388119, 63.25040349127835, 72.87139630657704, 89.1023960305774, 125.65244082804028, 240.87486636892078]

        #setting the reward system that if the car stay straight it get a reward to true
        self.DIRECTION_REWARD = True

    #function which finds IF two lines intersect, and if they do, finds the distance between the point of intersection and the car
    def find_intersection(self, line1, line2):
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
                dist = distance_points((self.car.x, self.car.y), (xi,yi))
                return (xi, yi, dist)
            else:
                return None

    #uses the gate to set up some things for the timings
    def lineChecks(self, input_line):
        self.noStart = False
        if input_line == gates[0]:
            for x in self.checkerList:
                if x != False:
                    self.noStart = True
                    break
            if self.noStart == False:
                if self.started == False:
                    self.timer.start() #to start the timer
                    self.started = True
                    self.checkerList[0] = True
                    self.swap = True
                    self.going = True
            
            if self.checkerList[gates.index(input_line)-1] == True or self.checkerList[gates.index(input_line)-2] == True or self.checkerList[gates.index(input_line)-3] == True or self.checkerList[gates.index(input_line)-4] == True or self.checkerList[gates.index(input_line)-5] == True or self.checkerList[gates.index(input_line)-6] == True:
                self.swap = True
                self.started = False
                self.lapCompleted = True
                for x in range(1,len(self.checkerList)+1):
                    self.checkerList[x-1] = False
                
                for line in gates:
                    line.color = (255,165,0)
                
                if self.going == False:
                    self.going = True
                else:
                    self.going = False
            
        else:
            if self.checkerList[gates.index(input_line)-1] == True or self.checkerList[gates.index(input_line)-2] == True or self.checkerList[gates.index(input_line)-3] == True or self.checkerList[gates.index(input_line)-4] == True or self.checkerList[gates.index(input_line)-5] == True or self.checkerList[gates.index(input_line)-6] == True:
                input_line.color = (255,255,255)
                if self.checkerList[gates.index(input_line)] == False:
                    self.new_gate_signal = True
                    self.checkerList[gates.index(input_line)] = True

    #function will check if the line is a gate or a wall. If the line is a gate then it will return true
    def timerLine(self,input_line):
        if input_line in gates:
            return True

    #this function finds the time for one lap
    def stopwatch(self):
        if self.lapCompleted == True:
            self.lapCompleted = False
            self.timer.lap(self.lap_list)
            print(self.lap_list)

            #check if it is the users best ever lap
            date = screen.find_date()
            if screen.get_data_db(screen.account_name,3) == 0.0:
                screen.update_lap_and_date_db(screen.account_name, self.lap_list[-1], date)
                screen.account_best_lap = self.lap_list[-1]
                screen.account_best_lap_date = date
                screen.new_data_entry_actions("update_lap_time", date)                
            if self.lap_list[-1] < screen.get_data_db(screen.account_name,3):
                screen.update_lap_and_date_db(screen.account_name, self.lap_list[-1], date)
                screen.account_best_lap = self.lap_list[-1]
                screen.account_best_lap_date = date
                screen.new_data_entry_actions("update_lap_time", date)
            
            #add new lap time to lap displays
            screen.display_times = str(screen.display_times) + """
Lap {}: {}""".format(len(self.lap_list),self.lap_list[-1])  
    
    #function to find how close the car is to pointing directly forwards
    def car_direction(self):
        #finding the next gate
        count = 0
        while True:
            count += 1
            if self.checkerList[count-1] == False:
                if count >= 83:
                    count = 1
                break
            if count >= 83:
                count = 1
                break
        
        #getting the directly forward car rotation
        a,b = self.car.x, self.car.y
        c,d = midpoint(gates[count])
        dist = distance_points((a,b), (c,d))
        vertical_height = d-b
        ang = (180/3.141)*asin(abs(vertical_height)/dist)
        if vertical_height > 0:
            if grad_points((a,b), (c,d)) > 0: #first quadrant
                ideal_rotation = 90 - ang
            else: #second quadrant
                ideal_rotation = 270 + ang
        else:
            if grad_points((a,b), (c,d)) > 0: #third quadrant
                ideal_rotation = 270 - ang
            else: #fourth quadrant
                ideal_rotation = 90 + ang
        
        angle_change = abs((self.car.rotation%360) - ideal_rotation) / 180
        return angle_change

    #function creates a variable which can be printed of lap times
    def next_lap(self):
        text = """
Lap {}: {}""".format(len(self.lap_list),self.lap_list[-1])   
        
        return text

    #function calculates the reward of each tick
    def reward(self):
        reward = 0
        
        #reward for passing gates
        if self.reward_gate == True and self.new_gate_signal == True:
            reward += 2
        #pentaly for hitting walls
        if self.wall_collision == True:
            reward -= 3

        if self.DIRECTION_REWARD == True:
            if self.car_direction() < 0.12:
                reward += 0.01
            elif self.car_direction() > 0.5:
                reward -= 0.02

        self.new_gate_signal = False
        self.reward_gate = False
        self.wall_collision = False

        return reward

    #this function is ran every tick and checks for the collision between the car and any of the gates or walls.
    def overlap_check(self, car_hitbox, input_lines):
        self.hitbox_lines = []
        for x in range(len(car_hitbox)):
            a,b = car_hitbox[x%4]
            c,d = car_hitbox[(x+1)%4]
            self.hitbox_lines.append(pyglet.shapes.Line(x=a, y=b, x2=c, y2=d, width=1))

        for wall in input_lines:
            for car_side in self.hitbox_lines:
                if self.find_intersection(car_side, wall) != None:
                    if self.timerLine(wall) == True:
                        self.reward_gate = True
                        self.lineChecks(wall)
                    else:
                        self.wall_collision = True
                        return True

    #used to update the lines which the AI uses to see
    def update_rays(self):
        viewingLine1 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation)), y2=self.lineLength*cos(radians(self.car.rotation)))
        viewingLine2 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation) + radians(15)), y2=self.lineLength*cos(radians(self.car.rotation)+ radians(15)))
        viewingLine3 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation) + radians(30)), y2=self.lineLength*cos(radians(self.car.rotation) + radians(30)))
        viewingLine4 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation) + radians(45)), y2=self.lineLength*cos(radians(self.car.rotation) + radians(45)))
        viewingLine5 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation) + radians(60)), y2=self.lineLength*cos(radians(self.car.rotation) + radians(60)))
        viewingLine6 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation) + radians(90)), y2=self.lineLength*cos(radians(self.car.rotation) + radians(90)))
        viewingLine7 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation) + radians(135)), y2=self.lineLength*cos(radians(self.car.rotation) + radians(135)))
        viewingLine8 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation) + radians(180)), y2=self.lineLength*cos(radians(self.car.rotation) + radians(180)))
        viewingLine9 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation) + radians(225)), y2=self.lineLength*cos(radians(self.car.rotation) + radians(225)))
        viewingLine10 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation) + radians(270)), y2=self.lineLength*cos(radians(self.car.rotation) + radians(270)))
        viewingLine11 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation) + radians(300)), y2=self.lineLength*cos(radians(self.car.rotation) + radians(300)))
        viewingLine12 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation) + radians(315)), y2=self.lineLength*cos(radians(self.car.rotation) + radians(315)))
        viewingLine13 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation) + radians(330)), y2=self.lineLength*cos(radians(self.car.rotation) + radians(330)))
        viewingLine14 = pyglet.shapes.Line(x=self.car.x, y=self.car.y, x2=self.lineLength*sin(radians(self.car.rotation) + radians(345)), y2=self.lineLength*cos(radians(self.car.rotation) + radians(345)))

        viewingLineList = [viewingLine1, viewingLine2, viewingLine3, viewingLine4, viewingLine5, viewingLine6, viewingLine7, viewingLine8, viewingLine9, viewingLine10, viewingLine11, viewingLine12, viewingLine13, viewingLine14]
        return viewingLineList

    #uses the rays to find points of intersection with the closest sides of the track - returns a list of points
    def aiVision(self, rays):
        intersectList = []
        for ray in rays:
            overlapList = []
            for wall in walls:
                overlapPoint = self.find_intersection(ray, wall)
                if overlapPoint is not None:
                    overlapList.append(overlapPoint)

            if overlapList:
                smallest = min(overlapList, key=lambda t: t[2])
                intersectList.append((smallest[0], smallest[1]))
        return intersectList

    #resets the car to a random point on the track
    def reset(self):
        #TOTAL VARIABLE RESET

        self.forward = False
        self.backward = False
        self.clockwise = False
        self.aclockwise = False
        self.drift = False

        self.action_list = [self.forward, self.backward, self.clockwise, self.aclockwise, self.drift]
        
        self.velocity = 0 *scale_factor
        self.max_velocity = 8 *scale_factor
        self.friction = 0.07 *scale_factor
        self.acceleration = 0.1 *scale_factor
        self.rotation_speed = 3
        self.drift_time = 8 *scale_factor
        
        self.sprite_hitbox = [(0,0),(0,0),(0,0),(0,0)]
        
        self.reward_gate = False
        self.wall_collision = False
        self.collList = []

        self.backDict = {}
        self.rounds = 0

        self.noStart = False
        self.started = False
        self.swap = False
        self.going = False
        self.lapCompleted = False
        self.new_gate_signal = False
        
        self.going = 0
        self.start = 0
        self.elapsed = 0

        self.lap_list = []

        #respawning the car at a random midpoint of a reward gate
        respawnLine = random.choice(gates)
        self.car.x, self.car.y = midpoint(respawnLine)

        for x in range(gates.index(respawnLine)):
            gates.append(gates[0])
            del gates[0]

        for x in range(len(self.checkerList)):
            self.checkerList[x] = False

        #getting the car rotation for the respawn
        a,b = midpoint(respawnLine)
        c,d = midpoint(gates[(gates.index(respawnLine)+1)%len(gates)])
        dist = distance_points((a,b), (c,d))
        vertical_height = d-b
        ang = (180/3.141)*asin(abs(vertical_height)/dist)
        if vertical_height > 0:
            if grad_points((a,b), (c,d)) > 0: #first quadrant
                self.car.rotation = 90 - ang
            else: #second quadrant
                self.car.rotation = 270 + ang
        else:
            if grad_points((a,b), (c,d)) > 0: #third quadrant
                self.car.rotation = 270 - ang
            else: #fourth quadrant
                self.car.rotation = 90 + ang

    #function for when the user presses a key
    def on_key_press(self, symbol, modifiers):
        if symbol == self.forward_key or symbol == key.UP:
            self.forward = True
        if symbol == self.backward_key or symbol == key.DOWN:
            self.backward = True
        if symbol == self.left_key or symbol == key.LEFT:
            self.aclockwise = True
        if symbol == self.right_key or symbol == key.RIGHT:
            self.clockwise = True
        if symbol == self.drift_key or symbol == key.RSHIFT:
            self.drift = True
            self.rotation_speed = 3.5
            self.rounds = 0
        
        self.action_list = [self.forward, self.backward, self.clockwise, self.aclockwise, self.drift]

    #function for when the user realeses the key
    def on_key_release(self, symbol, modifiers):
        if symbol == self.forward_key or symbol == key.UP:
            self.forward = False
        if symbol == self.backward_key or symbol == key.DOWN:
            self.backward = False
        if symbol == self.left_key or symbol == key.LEFT:
            self.aclockwise = False
        if symbol == self.right_key or symbol == key.RIGHT:
            self.clockwise = False
        if symbol == self.drift_key or symbol == key.RSHIFT:
            self.drift = False
            self.rotation_speed = 3
        
        self.action_list = [self.forward, self.backward, self.clockwise, self.aclockwise, self.drift]

    #update function that is called every tick. Is used for the car movement, timing, collisions, etc.
    def action(self, actions):
        #----------CAR MOVEMENT----------#
        self.actions = chooseAction(actions) #turns the ai input into a list, or keeps the user list the same.

        #slowing the car down due to frction
        if self.velocity > 0:
            self.velocity -= self.friction
        if self.velocity < 0:
            self.velocity += self.friction
        #making sure the car doesn't exceed max speeds from forward and backward directions
        if self.velocity > self.max_velocity:
            self.velocity = self.max_velocity
        if self.velocity < -(self.max_velocity-3):
            self.velocity = -(self.max_velocity-3)
        #making the car go forwards and backwards
        if self.actions[0] == True and self.overlap_check(self.sprite_hitbox, line_list) != True:
            self.velocity += self.acceleration
        if self.actions[1] == True and self.overlap_check(self.sprite_hitbox, line_list) != True:
            self.velocity -= self.acceleration/1.3
        #making the car turn left and right
        if self.actions[0] == True or self.actions[1] == True or self.velocity > self.friction or self.velocity < -self.friction: #this is so that the car only turns if it is moving forwards or backwards
            if self.actions[3] == True:
                self.car.rotation -= self.rotation_speed
            if self.actions[2] == True:
                self.car.rotation += self.rotation_speed
        
        #checks if the car has collided with a call, and if it has, stops the car
        if self.overlap_check(self.sprite_hitbox,line_list) == True:
            self.car.x, self.car.y = self.collList[int(-self.velocity//3)-2]
            self.actions[4] = False
            self.velocity = 0
        
        #this system is used so that the car doesn't get stuck in the wall and respawns slightly back from the wall
        new = (self.car.x, self.car.y)
        self.collList.append(new)
        if len(self.collList) > 13:
            del self.collList[0]

        
        #moving the postition of the car
        dy = self.velocity * cos(radians(self.car.rotation))
        dx = self.velocity * sin(radians(self.car.rotation))

        #drift code
        new = {dy:dx}
        self.backDict.update(new)
        if len(self.backDict) > self.drift_time:
            self.backDict.pop(list(self.backDict)[0])
        
        self.rounds += 1
        if self.actions[4] == True:
            if len(self.backDict) > 2:
                if self.rounds >= self.drift_time:
                    self.car.y += list(self.backDict)[0]
                    self.car.x += self.backDict[list(self.backDict)[1]]
                else:
                    self.car.y += dy
                    self.car.x += dx
        else:
            self.car.y += dy
            self.car.x += dx

        #----------CAR COLLISIONS----------#
        #car hitbox
        self.sprite_top_left = (self.h*cos(1.57 +self.angle) + self.car.x, self.h*sin(1.57 +self.angle) + self.car.y)
        self.sprite_top_right = (self.h*cos(1.57 - self.angle) + self.car.x, self.h*sin(1.57 - self.angle) + self.car.y)
        self.sprite_bottom_left = (self.h*cos(4.71 -self.angle) + self.car.x, self.h*sin(4.71 -self.angle) + self.car.y)
        self.sprite_bottom_right = (self.h*cos(-1.57 + self.angle) + self.car.x, self.h*sin(-1.57 + self.angle) + self.car.y)

        self.sprite_hitbox = [self.sprite_top_left,self.sprite_top_right,self.sprite_bottom_left,self.sprite_bottom_right ]

        self.overlap_check(self.sprite_hitbox, line_list)

        #----------TIMING CODE----------#
        self.stopwatch()

        #----------REWARDS----------#
        self.tick_reward = self.reward() #make sure that this is getting rewards from the actual tick not from the tick beofre

        #----------AI vision code----------#
        self.new_rays = self.update_rays()
        if len(self.aiVision(self.new_rays)) < 14:
            self.collisionPointsList = self.oldCollisionPointsList
        else:
            self.collisionPointsList = self.aiVision(self.new_rays)
            self.oldCollisionPointsList = self.collisionPointsList
        
        self.aiVisionList = []
        for point in self.collisionPointsList:
            self.aiVisionList.append(distance_points((self.car.x, self.car.y), point))
        
        self.rotation_difference = self.car_direction()
        
        self.observation_space = [self.velocity, self.car.rotation, self.rotation_difference] + self.aiVisionList


#finding the start position for player 1
car_start_x =  1020/1920 *windowwidth
car_start_y =  185/1080 *windowheight

class RacingEnv(pyglet.window.Window):
    def __init__(self):
        super().__init__(resizable=False, caption="Artificial Drift", fullscreen=True)

        self.set_fullscreen(True)
        self.wall_lines = pyglet.graphics.Batch()
        self.gate_lines = pyglet.graphics.Batch()
        self.ai_lines = pyglet.graphics.Batch()

        self.entry = pyglet.graphics.Batch()
        self.raceExtras = pyglet.graphics.Batch()
        self.logsignDisplays = pyglet.graphics.Batch()
        self.logExtras = pyglet.graphics.Batch()
        self.signExtras = pyglet.graphics.Batch()
        self.pauseMenu = pyglet.graphics.Batch()
        self.cp = pyglet.graphics.Batch()
        self.leaderboardDisplays = pyglet.graphics.Batch()
        self.tableDisplay = pyglet.graphics.Batch()
        self.confirm = pyglet.graphics.Batch()

        self.player1 = Car(car_start_x,car_start_y,260,"images/car.png", key.W, key.S, key.A, key.D, key.LSHIFT)
        self.user_action = [False,False,False,False,False]

        #loading in walls
        self.walls = get_walls(windowwidth, windowheight)
        for wall in self.walls:
            wall.batch = self.wall_lines
        
        #loading in gates
        self.gates = get_gates(windowwidth, windowheight)
        r = 0
        for gate in self.gates:
            r += 1
            if r == 1:
                gate.opacity = 150 #start line
            else:
                gate.opacity = 40
            gate.batch = self.gate_lines
        
        #defining the line list
        self.line_list = self.walls + self.gates

        #defining boolean which control if each aspect is rendered or not
        self.SHOW_WALLS = True
        self.SHOW_CARS = True
        self.SHOW_GATES = True
        self.SHOW_RAYS = False

        #boolean for whether the lap times are displayed or not
        self.SHOW_LAPS = True

        #defining booleans which control the type of reset
        self.SIMPLE_RESET = True
        self.LOCATION_RESET = False
        self.SLIGHT_ROT_RESET = False
        self.RANDOM_ROT_RESET = False

        #timer code for the pause screen
        self.race_paused = False
        self.pauseSwap = False

        #origional pages open
        self.screenOn = [1,0,0,0,0,0,0,0] #entry screen, pop-up log in, pop-up sign up, pop-up change password, pop-up leaderboard, pop-up confirm, pause screen, game play screen

        #log in
        self.admin = False

        self.logged = False
        self.account_name = str()
        self.account_password = str()
        self.account_best_lap_date = str()
        self.account_best_lap = float()

        #amount of wall collisions in one episode
        self.hits = 0
        #length of the episode
        self.ticks = 0

        self.MAX_EPISODE_LENGTH = 1000
        
        #RACING SCREEN ICONS, BUTTONS, DECORATIONS---------------------
        self.display_times = ""
        
        self.pauseBackdrop = pyglet.shapes.Rectangle(x=1337, y=800, width=71, height=80, color=(255, 255, 255), batch=self.raceExtras)
        self.pauseBackdrop.opacity = 10
        
        self.pause_img = image.load("images/icon_pause.png")
        self.pause_img.anchor_x = self.pause_img.width//2
        self.pause_img.anchor_y = self.pause_img.height//2
        self.pause = sprite.Sprite(self.pause_img, x=1372, y=840, batch=self.raceExtras)
        self.pause.scale = 0.2*scale_factor

        self.lap_splits_label = pyglet.text.Label("Lap Splits:", font_name='Zen Dots', font_size=27, x=10, y=800, color=(255,140,0,255), batch=self.raceExtras)
        self.lap_splits_label2 = pyglet.text.Label(self.display_times, font_name='Zen Dots', font_size=20, x=10, y=800, color=(220, 220 ,220, 1000), batch=self.raceExtras)

        #PAUSE SCREEN-----------------------
        self.backdrop2 = pyglet.shapes.Rectangle(x=0, y=0, width=windowwidth, height=windowheight, color=(0, 0, 0))
        self.backdrop2.opacity = 220 
        
        #box to cover the pause icon on the screen behind
        self.coverPause = pyglet.shapes.Rectangle(x=1337, y=800, width=71, height=80, color=(0, 0, 0), batch=self.pauseMenu)
        
        #header
        self.paused_header = image.load("images/text_paused.png")
        self.paused_header.anchor_x = self.paused_header.width//2
        self.paused_header.anchor_y = self.paused_header.height//2
        self.paused = sprite.Sprite(self.paused_header, x=windowwidth//2, y=windowheight//2 +350, batch=self.pauseMenu)
        self.paused.scale = 0.5*scale_factor

        #profile picture
        self.pp_img = image.load("images/icon_pp.png")
        self.pp_img.anchor_x = self.pp_img.width//2
        self.pp_img.anchor_y = self.pp_img.height//2
        self.profilePicture = sprite.Sprite(self.pp_img, x=windowwidth//2 -550, y=windowheight//2 +350, batch=self.pauseMenu)
        self.profilePicture.scale = 0.1*scale_factor

        #play button box
        self.coverPlay = pyglet.shapes.Rectangle(x=630, y=80, width=170, height=180, color=(126, 126, 126), batch=self.pauseMenu)
        self.coverPlay.opacity = 0

        #play icon
        self.play2_img = image.load("images/icon_play.png")
        self.play2_img.anchor_x = self.play2_img.width//2
        self.play2_img.anchor_y = self.play2_img.height//2
        self.resumeButton = sprite.Sprite(self.play2_img, x=720, y=170, batch=self.pauseMenu)
        self.resumeButton.scale = 0.57*scale_factor
        self.resumeButton.opacity = 100

        #account display labels (these are updated everytime the pause button is pushed)
        self.label_accountName = pyglet.text.Label("USERNAME: " + str(self.account_name), font_name='Zen Dots', bold=True, color=(220, 220 ,220, 1000), font_size=13, x=20, y=690, batch=self.pauseMenu)
        self.label_bestLap = pyglet.text.Label("BEST LAP: " + str(self.account_best_lap) + "seconds", font_name='Zen Dots', bold=True, color=(220, 220 ,220, 1000), font_size=13, x=20, y=650, batch=self.pauseMenu)
        self.label_bestLapDate = pyglet.text.Label("DATE ACHIEVED: " + str(self.account_best_lap_date), font_name='Zen Dots', bold=True, color=(220, 220 ,220, 1000), font_size=13, x=20, y=610, batch=self.pauseMenu)

        #delete account button
        self.label_delete = pyglet.text.Label("DELETE ACCOUNT", font_name='Zen Dots', color=(255, 0, 0, 145), font_size=11, x=60, y=560, batch=self.pauseMenu)
        self.delete_underline = pyglet.shapes.Line(x=60, y=556, x2=230, y2=556, color=(255, 0, 0, 255), width=2, batch=self.pauseMenu)
        self.delete_underline.opacity = 0

        #labels
        self.label_restart = pyglet.text.Label("RESTART", font_name='Zen Dots', bold=True, color=(180, 180 ,180, 150), font_size=30, x=585, y=680, batch=self.pauseMenu)
        self.underline1 = pyglet.shapes.Rectangle(x=582,y=671,height=5, width=268, batch=self.pauseMenu)
        self.underline1.opacity = 0
        self.label_leaderboards = pyglet.text.Label("LEADERBOARDS", font_name='Zen Dots', bold=True, color=(180, 180 ,180, 150), font_size=30, x=490, y=590, batch=self.pauseMenu)
        self.underline2 = pyglet.shapes.Rectangle(x=488,y=581, height = 5, width=459, batch=self.pauseMenu)
        self.underline2.opacity = 0
        self.label_btes = pyglet.text.Label("BACK TO ENTRY SCREEN", font_name='Zen Dots', bold=True, color=(180, 180 ,180, 150), font_size=30, x=370, y=500, batch=self.pauseMenu)
        self.underline3 = pyglet.shapes.Rectangle(x=369,y=491, height=5, width=687, batch=self.pauseMenu)
        self.underline3.opacity = 0
        self.label_changePassword = pyglet.text.Label("CHANGE PASSWORD", font_name='Zen Dots', bold=True, color=(180, 180 ,180, 150), font_size=30, x=445, y=410, batch=self.pauseMenu)
        self.underline4 = pyglet.shapes.Rectangle(x=443, y=401, height=5, width=554, batch=self.pauseMenu)
        self.underline4.opacity = 0
        self.label_logOut = pyglet.text.Label("LOG OUT", font_name='Zen Dots', bold=True, color=(180, 180 ,180, 150), font_size=30, x=595, y=320, batch=self.pauseMenu)
        self.underline5 = pyglet.shapes.Rectangle(x=593,y=311, height=5, width=254, batch=self.pauseMenu)
        self.underline5.opacity = 0

        #button to turn lap displays on and off
        self.rectangle16 = pyglet.shapes.Rectangle(x=1330, y=10, width=100, height=50, color=(34, 139, 34), batch=self.pauseMenu)
        self.rectangle16.opacity = 50
        self.rectangle16.color = (34, 139, 34)

        #ENTRY SCREEN CODE -------------------------
        #logo
        self.logo_img = image.load("images/logo_finished.png")
        self.logo_img.anchor_x = self.logo_img.width//2
        self.logo_img.anchor_y = self.logo_img.height//2
        self.logo = sprite.Sprite(self.logo_img, x=windowwidth//2, y=windowheight//2 +100, batch=self.entry)
        self.logo.scale = scale_factor

        #play button
        self.play_img = image.load("images/text_play.png")
        self.play_img.anchor_x = self.play_img.width//2
        self.play_img.anchor_y = self.play_img.height//2
        self.playButton = sprite.Sprite(self.play_img, x=windowwidth//2, y=windowheight//2 -200, batch=self.entry)
        self.playButton.scale = 0.5*scale_factor

        #triangle decoration
        self.triangle_img = image.load("images/triangle1_translucent.png")
        self.triangle_img.anchor_x = self.triangle_img.width//2
        self.triangle_img.anchor_y = self.triangle_img.height//2
        self.triangle1 = sprite.Sprite(self.triangle_img, x=100, y=100, batch=self.entry)
        self.triangle1.rotation = 30
        self.triangle1.scale = 0.3*scale_factor

        #LOG IN SCREEN------------------------------
        self.textbox_states = [2,0,0] #0=white (no hover and not selected) 1=grey (hover, but not selected) 2=black (selected)
        
        self.text_log_input1 = str()
        self.text_log_input2 = str()

        self.next_letter = False
        self.next_letter2 = False
        
        self.selected_textbox_log = 1

        self.MAXIMUM_CHARACTER_LIMIT = 20

        #backdrop box
        #entry images
        self.backdrop = pyglet.shapes.Rectangle(x=0, y=0, width=windowwidth, height=windowheight, color=(0, 0, 0), batch=self.logsignDisplays)
        self.backdrop.opacity = 190

        #inner box
        self.rectangle2= pyglet.shapes.Rectangle(x=398, y=148, width=windowwidth-(400*2)+4, height=554, color=(0, 0, 0), batch=self.logsignDisplays)
        self.rectangle2.opacity = 160

        #box
        self.rectangle = pyglet.shapes.Rectangle(x=400, y=150, width=windowwidth-(400*2), height=550, color=(240, 90, 25), batch=self.logsignDisplays)
        self.rectangle.opacity = 160

        #header
        self.login_img = image.load("images/text_log-in.png")
        self.login_img.anchor_x = self.login_img.width//2
        self.login_img.anchor_y = self.login_img.height//2
        self.loginHeading = sprite.Sprite(self.login_img, x=windowwidth//2, y=windowheight//2 +200, batch=self.logExtras)
        self.loginHeading.scale = 0.26*scale_factor

        #"username"
        self.username_img = image.load("images/text_username.png")
        self.username_img.anchor_x = self.username_img.width//2
        self.username_img.anchor_y = self.username_img.height//2
        self.usernameHeading = sprite.Sprite(self.username_img, x=windowwidth//2-200, y=windowheight//2 +140, batch=self.logsignDisplays)
        self.usernameHeading.scale = 0.1*scale_factor

        #"password"
        self.password_img = image.load("images/text_password.png")
        self.password_img.anchor_x = self.password_img.width//2
        self.password_img.anchor_y = self.password_img.height//2
        self.passwordHeading = sprite.Sprite(self.password_img, x=windowwidth//2-200, y=windowheight//2 +30, batch=self.logsignDisplays)
        self.passwordHeading.scale = 0.1*scale_factor

        #"don't have an account?"
        self.no_account_img = image.load("images/tex_no_account.png")
        self.no_account_img.anchor_x = self.no_account_img.width//2
        self.no_account_img.anchor_y = self.no_account_img.height//2
        self.no_accountHeading = sprite.Sprite(self.no_account_img, x=windowwidth//2, y=windowheight//2 -100, batch=self.logExtras)
        self.no_accountHeading.scale = 0.2*scale_factor

        #sign up button
        self.rectangle8 = pyglet.shapes.Rectangle(x=650, y=304, width=141, height=32, color=(0, 0, 0), batch=self.logExtras)
        self.rectangle8.opacity = 50

        self.sign_up_img = image.load("images/text_sign-up.png")
        self.sign_up_img.anchor_x = self.sign_up_img.width//2
        self.sign_up_img.anchor_y = self.sign_up_img.height//2
        self.sign_upHeading = sprite.Sprite(self.sign_up_img, x=windowwidth//2, y=windowheight//2 -130, batch=self.logExtras)
        self.sign_upHeading.scale = 0.13*scale_factor
        
        #"confirm password"
        self.confirm_img = image.load("images/text_confirm-password.png")
        self.confirm_img.anchor_x = self.confirm_img.width//2
        self.confirm_img.anchor_y = self.confirm_img.height//2
        self.confirmHeading = sprite.Sprite(self.confirm_img, x=windowwidth//2-140, y=windowheight//2 -80, batch=self.signExtras)
        self.confirmHeading.scale = 0.15*scale_factor

        #textbox1
        self.rectangle3 = pyglet.shapes.Rectangle(x=450, y=520, width=500, height=50, color=(255, 255, 255), batch=self.logsignDisplays)
        self.rectangle3.opacity = 150

        #textbox2
        self.rectangle5 = pyglet.shapes.Rectangle(x=450, y=410, width=500, height=50, color=(255, 255, 255), batch=self.logsignDisplays)
        self.rectangle5.opacity = 150

        #textbox3
        self.rectangle6 = pyglet.shapes.Rectangle(x=450, y=300, width=500, height=50, color=(255, 255, 255), batch=self.signExtras)
        self.rectangle6.opacity = 150

        #label
        self.label1 = pyglet.text.Label(self.text_log_input1, font_name='Arial', font_size=20, x=700, y=700, batch=self.logExtras)
        self.label2 = pyglet.text.Label(self.text_log_input2, font_name='Arial', font_size=20, x=700, y=700, batch=self.logExtras)

        #enter button
        self.rectangle7 = pyglet.shapes.Rectangle(x=770, y=180, width=180, height=50, color=(0, 0, 0), batch=self.logsignDisplays)
        self.rectangle7.opacity = 50

        self.enter_img = image.load("images/text_enter....png")
        self.enter_img.anchor_x = self.enter_img.width//2
        self.enter_img.anchor_y = self.enter_img.height//2
        self.enterHeading = sprite.Sprite(self.enter_img, x=860, y=205, batch=self.logsignDisplays)
        self.enterHeading.scale = 0.15*scale_factor

        #log in error messages
        self.dummy = pyglet.text.Label("", font_name='Arial', bold=True, color=(255, 255 ,255, 1000), font_size=12, x=778, y=235)
        self.noUsername = pyglet.text.Label("username not found...", font_name='Arial', bold=True, color=(255, 255 ,255, 1000), font_size=12, x=778, y=235)
        self.badPassword = pyglet.text.Label("incorrect password...", font_name='Arial', bold=True, color=(255, 255 ,255, 1000), font_size=12, x=778, y=235)
        self.log_error_message = self.dummy

        #SIGN UP EXTRAS------------------------------
        self.text_sign_input1 = str()
        self.text_sign_input2 = str()
        self.text_sign_input3 = str()

        self.next_letter3 = False
        self.next_letter4 = False
        self.next_letter5 = False
        
        self.selected_textbox_sign = 1
        
        #heading
        self.sign_up2_img = image.load("images/text_sign-up.png")
        self.sign_up2_img.anchor_x = self.sign_up2_img.width//2
        self.sign_up2_img.anchor_y = self.sign_up2_img.height//2
        self.sign_up2Heading = sprite.Sprite(self.sign_up2_img, x=windowwidth//2, y=windowheight//2 +200, batch=self.signExtras)
        self.sign_up2Heading.scale = 0.26*scale_factor

        #back button
        self.rectangle9 = pyglet.shapes.Rectangle(x=450, y=627, width=46, height=46, color=(0, 0, 0), batch=self.signExtras)
        self.rectangle9.opacity = 50

        #back icon
        self.back_img = image.load("images/icon_back.png")
        self.back_img.anchor_x = self.back_img.width//2
        self.back_img.anchor_y = self.back_img.height//2
        self.backButton = sprite.Sprite(self.back_img, x=473, y=650, batch=self.signExtras)
        self.backButton.scale = 0.25*scale_factor

        #labels
        self.label3 = pyglet.text.Label(self.text_sign_input1, font_name='Arial', font_size=20, x=700, y=700, batch=self.signExtras)
        self.label4 = pyglet.text.Label(self.text_sign_input2, font_name='Arial', font_size=20, x=700, y=700, batch=self.signExtras)
        self.label5 = pyglet.text.Label(self.text_sign_input3, font_name='Arial', font_size=20, x=700, y=700, batch=self.signExtras)

        #error messages
        self.doesNotMatch = pyglet.text.Label("passwords do not match", font_name='Arial', bold=True, color=(255, 255 ,255, 1000), font_size=12, x=765, y=235)
        self.tooShort = pyglet.text.Label("password must be greater than 8 characters", font_name='Arial', bold=True, color=(255, 255 ,255, 1000), font_size=12, x=695, y=235)
        self.userExists = pyglet.text.Label("username already exists", font_name='Arial', bold=True, color=(255, 255 ,255, 1000), font_size=12, x=768, y=235)
        self.sign_error_message = self.dummy

        #CHANGE PASSWORD SCREEN --------------------
        self.textbox_states_cp = [2,0,0]
        self.selected_textbox_cp = 1

        self.text_cp_input1 = str()
        self.text_cp_input2 = str()
        self.text_cp_input3 = str()

        self.next_letter6 = False
        self.next_letter7 = False
        self.next_letter8 = False
        
        #backdrop
        self.backdrop3 = pyglet.shapes.Rectangle(x=0, y=0, width=windowwidth, height=windowheight, color=(0, 0, 0), batch=self.cp)
        self.backdrop3.opacity = 190 

        #inner box
        self.r2ectangle2= pyglet.shapes.Rectangle(x=398, y=148, width=windowwidth-(400*2)+4, height=554, color=(0, 0, 0), batch=self.cp)
        self.r2ectangle2.opacity = 160

        #box
        self.r2ectangle = pyglet.shapes.Rectangle(x=400, y=150, width=windowwidth-(400*2), height=550, color=(240, 90, 25), batch=self.cp)
        self.r2ectangle.opacity = 160
        
        #header
        self.cp_img = image.load("images/text_change-password.png")
        self.cp_img.anchor_x = self.cp_img.width//2
        self.cp_img.anchor_y = self.cp_img.height//2
        self.cpHeading = sprite.Sprite(self.cp_img, x=windowwidth//2, y=windowheight//2 +200, batch=self.cp)
        self.cpHeading.scale = 0.26*scale_factor

        #"old password"
        self.oldp_img = image.load("images/text_old-password.png")
        self.oldp_img.anchor_x = self.oldp_img.width//2
        self.oldp_img.anchor_y = self.oldp_img.height//2
        self.oldpHeading = sprite.Sprite(self.oldp_img, x=windowwidth//2-170, y=windowheight//2 +140, batch=self.cp)
        self.oldpHeading.scale = 0.12*scale_factor

        #"new password"
        self.np_img = image.load("images/text_new-password.png")
        self.np_img.anchor_x = self.np_img.width//2
        self.np_img.anchor_y = self.np_img.height//2
        self.newPasswordHeading = sprite.Sprite(self.np_img, x=windowwidth//2-170, y=windowheight//2 +30, batch=self.cp)
        self.newPasswordHeading.scale = 0.12*scale_factor

        #"confirm new password"
        self.confirm_new_img = image.load("images/text_confirm-new-password.png")
        self.confirm_new_img.anchor_x = self.confirm_new_img.width//2
        self.confirm_new_img.anchor_y = self.confirm_new_img.height//2
        self.confirmNewHeading = sprite.Sprite(self.confirm_new_img, x=windowwidth//2-117, y=windowheight//2 -80, batch=self.cp)
        self.confirmNewHeading.scale = 0.18*scale_factor

        #textbox1
        self.rectangle10 = pyglet.shapes.Rectangle(x=450, y=520, width=500, height=50, color=(255, 255, 255), batch=self.cp)
        self.rectangle10.opacity = 150

        #textbox2
        self.rectangle11 = pyglet.shapes.Rectangle(x=450, y=410, width=500, height=50, color=(255, 255, 255), batch=self.cp)
        self.rectangle11.opacity = 150

        #textbox3
        self.rectangle12 = pyglet.shapes.Rectangle(x=450, y=300, width=500, height=50, color=(255, 255, 255), batch=self.cp)
        self.rectangle12.opacity = 150
        
        #back button
        self.rectangle14 = pyglet.shapes.Rectangle(x=450, y=180, width=50, height=50, color=(0, 0, 0), batch=self.cp)
        self.rectangle14.opacity = 50

        #back icon
        self.back_img = image.load("images/icon_back.png")
        self.back_img.anchor_x = self.back_img.width//2
        self.back_img.anchor_y = self.back_img.height//2
        self.b2ackButton = sprite.Sprite(self.back_img, x=473, y=205, batch=self.cp)
        self.b2ackButton.scale = 0.25*scale_factor

        #enter button
        self.rectangle13 = pyglet.shapes.Rectangle(x=770, y=180, width=180, height=50, color=(0, 0, 0), batch=self.cp)
        self.rectangle13.opacity = 50

        self.e2nter_img = image.load("images/text_enter....png")
        self.e2nter_img.anchor_x = self.e2nter_img.width//2
        self.e2nter_img.anchor_y = self.e2nter_img.height//2
        self.e2nterHeading = sprite.Sprite(self.e2nter_img, x=860, y=205, batch=self.cp)
        self.e2nterHeading.scale = 0.15*scale_factor

        #labels
        self.label6 = pyglet.text.Label(self.text_cp_input1, font_name='Arial', font_size=20, x=700, y=700, batch=self.cp)
        self.label7 = pyglet.text.Label(self.text_cp_input2, font_name='Arial', font_size=20, x=700, y=700, batch=self.cp)
        self.label8 = pyglet.text.Label(self.text_cp_input3, font_name='Arial', font_size=20, x=700, y=700, batch=self.cp)
        
        #error messages
        self.incorrect_old_password = pyglet.text.Label("incorrect old password...", font_name='Arial', bold=True, color=(255, 255 ,255, 1000), font_size=12, x=765, y=235)
        #self.doesNotMatch and self.tooShort can also be used in self.cp_error_message
        self.cp_error_message = self.dummy

        #CONFIRM DELETION SCREEN -------------
        #backdrop
        self.backdrop5 = pyglet.shapes.Rectangle(x=0, y=0, width=windowwidth, height=windowheight, color=(0, 0, 0), batch=self.confirm)
        self.backdrop5.opacity = 120 

        #outer box
        self.cdBoxOut = pyglet.shapes.Rectangle(x=55, y=327, height = 206, width=406, color=(0, 0, 0), batch=self.confirm)
        self.cdBoxOut.opacity = 190

        #box
        self.cdBox = pyglet.shapes.Rectangle(x=58, y=330, height = 200, width=400, color=(240, 90, 25), batch=self.confirm)
        self.cdBox.opacity = 130

        #header label
        self.areYouSure = pyglet.text.Label("Are You Sure?", x=138, y=495, bold=True, font_name='Zen Dots', font_size=20, batch=self.confirm)
        self.areYouSure.color = (255,255,255, 240)
        self.warningLabel = pyglet.text.Label("     Deleting is permanint, account will be lost forever", multiline=True, width=300, x=123, y=463, font_name='Zen Dots', font_size=12, batch=self.confirm)
        self.warningLabel.color = (255,255,255,199)

        #cancel button
        self.cancelOuterButton = pyglet.shapes.Rectangle(x=76, y=348, height=54, width=154, color=(0,0,0), batch=self.confirm)
        self.cancelButton = pyglet.shapes.Rectangle(x=78, y=350, height=50, width=150, color=(199,199,199), batch=self.confirm)
        self.cancelLabel = pyglet.text.Label("CANCEL", x=92, y=367, font_name='Zen Dots', font_size=17, bold= True, color=(0,0,0,240), batch=self.confirm)

        #confirm button
        self.confirmButton = pyglet.shapes.Rectangle(x=288, y=350, height=50, width=150, color=(40,40,40), batch=self.confirm)
        self.confirmLabel = pyglet.text.Label("CONFIRM", x=296, y=367, font_name='Zen Dots', font_size=17, color=(255,15,15,190), batch=self.confirm)

        #LEADERBOARD SCREEN ----------------------------
        #backdrop
        self.backdrop4 = pyglet.shapes.Rectangle(x=0, y=0, width=windowwidth, height=windowheight, color=(0, 0, 0), batch=self.leaderboardDisplays)
        self.backdrop4.opacity = 220 

        #triangle decorations (behind main boxes)
        self.triangle2 = sprite.Sprite(self.triangle_img, x=1350, y=850, batch=self.leaderboardDisplays)
        self.triangle2.rotation = 160
        self.triangle2.scale = 0.4*scale_factor
        self.triangle2.opacity = 50

        self.triangle3 = sprite.Sprite(self.triangle_img, x=1450, y=750, batch=self.leaderboardDisplays)
        self.triangle3.rotation = 20
        self.triangle3.scale = 0.3*scale_factor
        self.triangle3.opacity = 50
        
        #box
        self.leaderBox = pyglet.shapes.Rectangle(x=10, y=10, width=1420, height=880, color=(240, 90, 25), batch=self.leaderboardDisplays)
        self.leaderBox.opacity = 210

        #inner box
        self.leaderBox2 = pyglet.shapes.Rectangle(x=15, y=15, width=1410, height=870, color=(0, 0, 0), batch=self.leaderboardDisplays)
        self.leaderBox2.opacity = 190

        #heading
        self.leader_img = image.load("images/text_leaderboard.png")
        self.leader_img.anchor_x = self.leader_img.width//2
        self.leader_img.anchor_y = self.leader_img.height//2
        self.leaderHeading = sprite.Sprite(self.leader_img, x=windowwidth//2, y=windowheight//2 +370, batch=self.leaderboardDisplays)
        self.leaderHeading.scale = 0.5*scale_factor

        #back button
        self.rectangle15 = pyglet.shapes.Rectangle(x=50, y=770, width=80, height=80, color=(0, 0, 0), batch=self.leaderboardDisplays)
        self.rectangle15.opacity = 50

        #back icon
        self.b3ackButton = sprite.Sprite(self.back_img, x=90, y=810, batch=self.leaderboardDisplays)
        self.b3ackButton.scale = 0.4*scale_factor

        #column labels
        self.lable_username = pyglet.text.Label("USERNAME", font_name='Zen Dots', font_size=19, x=345, y=720, color=(255,140,0,255), batch=self.leaderboardDisplays)
        self.lable_date = pyglet.text.Label("PB DATE", font_name='Zen Dots', font_size=19, x=648, y=720, color=(255,140,0,255), batch=self.leaderboardDisplays)
        self.lable_time = pyglet.text.Label("BEST LAP", font_name='Zen Dots', font_size=19, x=920, y=720, color=(255,140,0,255), batch=self.leaderboardDisplays)

        #box for table
        self.tableLine = pyglet.shapes.Line(x=300, y=710, x2=1140, y2=710, width=5, color=(240, 90, 25), batch=self.leaderboardDisplays)
        self.tableLine2 = pyglet.shapes.Line(x=300, y=110, x2=1140, y2=110, width=5, color=(240, 90, 25), batch=self.leaderboardDisplays)
        self.tableLine3 = pyglet.shapes.Line(x=303, y=110, x2=303, y2=710, width=5, color=(240, 90, 25), batch=self.leaderboardDisplays)
        self.tableLine4 = pyglet.shapes.Line(x=1138, y=110, x2=1138, y2=710, width=5, color=(240, 90, 25), batch=self.leaderboardDisplays)
        
        self.upstick2 = pyglet.shapes.Line(x=581, y=110, x2=581, y2=710, width=1, color=(240, 90, 25), batch=self.leaderboardDisplays)
        self.upstick3 = pyglet.shapes.Line(x=859, y=110, x2=859, y2=710, width=1, color=(240, 90, 25), batch=self.leaderboardDisplays)

        #arrows for ordering of table
        self.selected_arrow = 3 #1-username, 2-date, 3-time
        self.arrowStates = [0,0,0] #0-not selected, 1-hovering, 2-selected

        self.text_search = str()
        self.next_letter9 = False

        self.usernameBox = pyglet.shapes.Rectangle(x=540, y=720, height=16, width=16, color=(255,255,255), batch=self.leaderboardDisplays)
        self.usernameBox.opacity = 60
        self.downArrow1 = sprite.Sprite(self.play2_img, x=548, y=728, batch=self.leaderboardDisplays)
        self.downArrow1.rotation = 90
        self.downArrow1.scale = 0.04*scale_factor
        
        self.dateBox = pyglet.shapes.Rectangle(x=800, y=720, height=16, width=16, color=(255,255,255), batch=self.leaderboardDisplays)
        self.dateBox.opacity = 60
        self.downArrow2 = sprite.Sprite(self.play2_img, x=808, y=728, batch=self.leaderboardDisplays)
        self.downArrow2.rotation = 90
        self.downArrow2.scale = 0.04*scale_factor
        
        self.timeBox = pyglet.shapes.Rectangle(x=1093, y=720, height=16, width=16, color=(255,255,255), batch=self.leaderboardDisplays)
        self.timeBox.opacity = 60
        self.downArrow3 = sprite.Sprite(self.play2_img, x=1101, y=728, batch=self.leaderboardDisplays)
        self.downArrow3.rotation = 90
        self.downArrow3.scale = 0.04*scale_factor

        #"search" label
        self.searchLabel = pyglet.text.Label("SEARCH: ", x=350, y=50, font_name="Zen Dots", font_size=21, color=(255,140,0,255), batch=self.leaderboardDisplays)

        #search bar
        self.searchBar = pyglet.shapes.Rectangle(x=525, y=35, width=500, height=50, color=(255, 255, 255), batch=self.leaderboardDisplays)
        self.searchBar.opacity = 150

        #search button
        self.searchButton = pyglet.shapes.Rectangle(x=1027, y=35, width=50, height = 50, color=(0,0,0), batch=self.leaderboardDisplays)
        self.searchButton.opacity = 100

        #serach icon
        self.search_img = image.load("images/icon_search.png")
        self.search_img.anchor_x = self.search_img.width//2
        self.search_img.anchor_y = self.search_img.height//2
        self.searchIcon = sprite.Sprite(self.search_img, x=1051, y=60, batch=self.leaderboardDisplays)
        self.searchIcon.scale = 0.15*scale_factor
        
        #search text
        self.label9 = pyglet.text.Label(self.text_search, font_name='Arial', font_size=20, x=540, y=40, batch=self.leaderboardDisplays)

        #rectangles to judge row size width etc
        #col = (50,50,50)
        #self.listT = []
        #for x in range(0,12):
        #    if col == (50,50,50):
        #        col = (150,150,150)
        #    else:
        #        col = (50,50,50)
        #    self.listT.append(pyglet.shapes.Rectangle(x=300, y=110+(50*x), width = 840, height=50, color=col, batch=self.leaderboardDisplays))

        #constants for the table
        self.row_height = 50
        self.visible_rows = 12
        self.table_start_y = 678  # Starting Y position for the first row
        self.scroll_offset = 0

        self.MAXIMUM_LABEL_WIDTH = 230

        self.data = []
        self.labels = []

        #DATABASE -----------------------------
        self.connection = sqlite3.connect("data2.db")
        self.cursor = self.connection.cursor()

        self.Order = 3 #0=order by name, 1=order default, 2=order by date, 3=order by lap time

    #function that displays database on screen
    def show_table(self, data):
        self.labels = []
        self.data = data
        if self.Order == 1:
            pass
        elif self.Order == 0:
            self.data = self.sort_by_date(self.data)
            self.data = self.sort_by_lap_times(self.data)
            self.data = self.sort_alphabetical(self.data)
        elif self.Order == 2:
            self.data = self.sort_alphabetical(self.data)
            self.data = self.sort_by_lap_times(self.data)
            self.data = self.sort_by_date(self.data)
        elif self.Order == 3:
            self.data = self.sort_alphabetical(self.data)
            self.data = self.sort_by_date(self.data)
            self.data = self.sort_by_lap_times(self.data)
        
        start_value = self.scroll_offset
        end_value = min(self.scroll_offset + self.visible_rows, len(self.data))

        for x, row in enumerate(self.data[start_value:end_value]):
            username, password, date, time = row
            a = pyglet.text.Label(username, x=325, y=self.table_start_y - (x*self.row_height), font_name='Zen Dots', font_size=14, batch=self.leaderboardDisplays)
            self.shorten_label(a)
            a
            if date == '0':
                date = "N/A"
            b = pyglet.text.Label(date, x=645, y=self.table_start_y - (x*self.row_height), font_name='Zen Dots', font_size=14, batch=self.leaderboardDisplays)
            if time == 0.0:
                time = "N/A"
            c = pyglet.text.Label(str(time), x=970, y=self.table_start_y - (x*self.row_height), font_name='Zen Dots', font_size=14, batch=self.leaderboardDisplays)
            self.labels.append(a)
            self.labels.append(b)
            self.labels.append(c)

    #function shortens the text in the label
    def shorten_label(self, label):
        ellipsis = "..."
        if label.content_width <= self.MAXIMUM_LABEL_WIDTH:
            return
        else:
            while label.content_width > self.MAXIMUM_LABEL_WIDTH:
                label.text = label.text[:-1]
            
            label.text = label.text + ellipsis
            return label

    #function to show the lap times
    def screen_displays(self):
        total_time = "{:.2f}".format(float(sum(self.player1.lap_list)) + float(self.player1.timer.get_time()))
        self.time_label1 = pyglet.text.Label("TIME: ", font_name='Zen Dots', font_size=32, x=600, y=835, color=(255,140,0,255), batch=self.raceExtras)
        self.time_label = pyglet.text.Label(total_time, font_name='Zen Dots', font_size=32, x=780, y=835, batch=self.raceExtras)

    #function finds the current date
    def find_date(self):
        rawDateTime = datetime.now()
        rawDate = str(rawDateTime)[:-16]
        date = rawDate[-2:] + "-" + rawDate[5:7] + "-" + rawDate[:4]
        
        return date

    #function for checking if the user name and password pair are in the database
    def check_if_in_db(self, player_name, password):
        self.cursor.execute("""
        SELECT * FROM lap_times
        WHERE gamer_name = '{}'
    """.format(player_name))
        players = self.cursor.fetchall() 
        try:
            player = players[0]
            if password == player[1]:
                return 0 #the passwords match
            else:
                return 1 #the passwords DON'T match
        except:
            return 2 #username not found

    #function that checks if the username is in the database regardless of the password
    def check_username_db(self, player_name):
        self.cursor.execute("""
        SELECT * FROM lap_times
        WHERE gamer_name = '{}'
    """.format(player_name))
        players = self.cursor.fetchall() 
        if len(players) > 0:
            return True
        else:
            return False

    #function that adds an item to the database
    def new_player_db(self, player_name, password):
        self.cursor.execute("""
        INSERT INTO lap_times VALUES
        ('{}', '{}', '{}', {})             
        """.format(player_name, password, 0, 0))

        self.connection.commit()

    #function that deletes a player from the database
    def delete_player_db(self, player_name):
        self.cursor.execute("""
        DELETE FROM lap_times
            WHERE gamer_name = '{}'
        """.format(player_name))

        self.connection.commit()

    #function that changes the password based on the username
    def update_password_db(self, player_name, new_password):
        self.cursor.execute("""
        UPDATE lap_times
        SET password = '{}'
        WHERE gamer_name = '{}'
    """.format(new_password, player_name))
        
        self.connection.commit()

    #function that finds the users best lap time
    def get_data_db(self, player_name, column):
        self.cursor.execute("""
        SELECT * FROM lap_times
        WHERE gamer_name = '{}'
    """.format(player_name))
        all = self.cursor.fetchall() 
        player = all[0]
        best_time = player[column]
        return best_time

    #function that updates the lap time and date completed of best lap
    def update_lap_and_date_db(self, player_name, new_lap_time, new_date):
        self.cursor.execute("""
        UPDATE lap_times
        SET date = '{}', time = {}
        WHERE gamer_name = '{}'
    """.format(new_date, new_lap_time, player_name))
        
        self.connection.commit()

    #function that fetches the whole database
    def get_db(self):
        self.cursor.execute("SELECT * FROM lap_times")
        results = self.cursor.fetchall()
        return results

    #gets the row based on the username
    def get_row_db(self,username):
        self.cursor.execute("""
        SELECT * FROM lap_times
        WHERE gamer_name = '{}'
    """.format(username))
        rowList = self.cursor.fetchall() 
        row = rowList[0]
        return row

    #sorts the database alphabetically
    def sort_alphabetical(self, data):
        name_list = []
        for row in data:
            username, password, date, time = row
            name_list.append(username)
        ordered_names = sorted(name_list)
        new_data = []
        for x in ordered_names:
            new_data.append(self.get_row_db(x))
        return new_data
    
    #sorting by date
    def sort_tuples_by_date(self, tuples_list):
        # Define a function to convert date from DD-MM-YYYY to a sortable format
        def convert_date(date_str):
            return datetime.strptime(date_str, "%d-%m-%Y")

        sorted_list = sorted(tuples_list, key=lambda x: convert_date(x[0]), reverse=True)
        
        return sorted_list

    #list all data sorted by date
    def sort_by_date(self, data):
        date_list = []
        reject_list = []
        for row in data:
            username, password, date, time = row
            if date == '0':
                reject_list.append(row)
            else:
                date_list.append((date, username, password, time))
        date_list = self.sort_tuples_by_date(date_list)
        new_data = []
        for x in date_list:
            new_data.append(self.get_row_db(x[1]))
        
        new_data += reject_list
        return new_data

    #list all data sorted by lap times
    def sort_by_lap_times(self, data):
        rejects_list = []
        valid_data_list = []
        for x in data:
            if x[3] == 0.0:
                rejects_list.append(x)
            else:
                valid_data_list.append(x)

        sorted_list = sorted(valid_data_list, key=lambda x: x[3])
        new_data = sorted_list + rejects_list

        return new_data

    #creates a new data set which is applicable to the serach
    def select(self, data, input_string):
        new_list = [t for t in data if any(input_string in str(x) for i, x in enumerate(t) if i != 1)]
        return new_list

    #enters data into the actions table
    def new_data_entry_actions(self, action, date):
        self.cursor.execute("""
        INSERT INTO actions VALUES
        ('{}', '{}')             
        """.format(action, date))

        self.connection.commit()

    def reset(self):
        self.display_times = ""

        if self.SIMPLE_RESET == True: #respawning the car at the start line
            if self.SLIGHT_ROT_RESET == True: #respawning the car facing forwards but at a slihgtly different rotation
                self.car_respawn_rotation = random.randint(25500,26500)/100
                self.player1 = Car(car_start_x,car_start_y,self.car_respawn_rotation,"images/car.png", key.W, key.S, key.A, key.D, key.LSHIFT)

            if self.RANDOM_ROT_RESET == True: #respawning the car at a complete random rotation
                self.car_respawn_rotation = random.randint(0,360)
                self.player1 = Car(car_start_x,car_start_y,self.car_respawn_rotation,"images/car.png", key.W, key.S, key.A, key.D, key.LSHIFT)

            else: #no rotation reset, just facing straight forward
                self.car_respawn_rotation = 260
                self.player1 = Car(car_start_x,car_start_y,self.car_respawn_rotation,"images/car.png", key.W, key.S, key.A, key.D, key.LSHIFT)
        
        elif self.LOCATION_RESET == True: #respawning the car at a random midpoint of a gate
            #respawning the car at a random midpoint of a reward gate
            respawnLine = random.choice(gates)
            self.car_respawn_x, self.car_respawn_y = midpoint(respawnLine)
            
            for x in range(gates.index(respawnLine)):
                gates.append(gates[0])
                del gates[0]
            
            for x in range(len(self.player1.checkerList)):
                self.player1.checkerList[x] = False

            if self.SLIGHT_ROT_RESET == True:
                #getting the car rotation for the respawn
                a,b = midpoint(respawnLine)
                c,d = midpoint(gates[(gates.index(respawnLine)+1)%len(gates)])
                dist = distance_points((a,b), (c,d))
                vertical_height = d-b
                ang = (180/3.141)*asin(abs(vertical_height)/dist)
                if vertical_height > 0:
                    if grad_points((a,b), (c,d)) > 0: #first quadrant
                        self.car_base_rotation = 90 - ang
                    else: #second quadrant
                        self.car_base_rotation = 270 + ang
                else:
                    if grad_points((a,b), (c,d)) > 0: #third quadrant
                        self.car_base_rotation = 270 - ang
                    else: #fourth quadrant
                        self.car_base_rotation = 90 + ang

                self.car_respawn_rotation = random.randint(int(self.car_base_rotation*100 -500),int(self.car_base_rotation*100 +500))/100
                self.player1 = Car(self.car_respawn_x,self.car_respawn_y,self.car_respawn_rotation,"images/car.png", key.W, key.A, key.S, key.D, key.LSHIFT)

            elif self.RANDOM_ROT_RESET == True:
                self.car_respawn_rotation = random.randint(0, 360)
                self.player1 = Car(self.car_respawn_x,self.car_respawn_y,self.car_respawn_rotation,"images/car.png", key.W, key.A, key.S, key.D, key.LSHIFT)

            else: #no rotation reset
                #getting the car rotation for the respawn
                a,b = midpoint(respawnLine)
                c,d = midpoint(gates[(gates.index(respawnLine)+1)%len(gates)])
                dist = distance_points((a,b), (c,d))
                vertical_height = d-b
                ang = (180/3.141)*asin(abs(vertical_height)/dist)
                if vertical_height > 0:
                    if grad_points((a,b), (c,d)) > 0: #first quadrant
                        self.car_respawn_rotation = 90 - ang
                    else: #second quadrant
                        self.car_respawn_rotation = 270 + ang
                else:
                    if grad_points((a,b), (c,d)) > 0: #third quadrant
                        self.car_respawn_rotation = 270 - ang
                    else: #fourth quadrant
                        self.car_respawn_rotation = 90 + ang
                
                self.player1 = Car(self.car_respawn_x,self.car_respawn_y,self.car_respawn_rotation,"images/car.png", key.W, key.A, key.S, key.D, key.LSHIFT)

        self.render()

        return self.player1.observation_space

    def step(self, action):
        done = False
        info = {}
        #updating the car
        self.player1.action(action)
        
        #finding the reward the car made
        reward = self.player1.tick_reward

        #getting the new state (observation space)
        new_state = self.player1.observation_space

        #checking if the edisode is over
        if reward < -1:
            self.hits += 1
        if self.hits > 10:
            done = True
            self.hits = 0
            self.ticks = 0
        if done == False:
            self.ticks += 1
        if self.ticks > self.MAX_EPISODE_LENGTH:
            done = True
            self.ticks = 0
            self.hits = 0

        return new_state, reward, done, info
        
    def textbox_colour(self, states_list, numb, rectangle):
        if states_list[numb] == 0:
            rectangle.color = (255,255,255)
        elif states_list[numb] == 1:
            rectangle.color = (126,126,126)
        else:
            rectangle.color = (0,0,0)
    
    def arrow_colour(self, states_list, numb, rectangle):
        if states_list[numb] == 0:
            rectangle.opacity = 60
        elif states_list[numb] == 1:
            rectangle.opacity = 130
        else:
            rectangle.opacity = 250

    def render(self, mode="human"):
        self.clear()
        #rendering dependant on the window
        if self.screenOn[0] == 1:
            self.entry.draw()
        if self.screenOn[1] == 1:
            self.logsignDisplays.draw()
            self.logExtras.draw()
            self.log_error_message.draw()
            self.textbox_colour(self.textbox_states, 0, self.rectangle3)
            self.textbox_colour(self.textbox_states, 1, self.rectangle5)
        if self.screenOn[2] == 1:
            self.logsignDisplays.draw()
            self.signExtras.draw()
            self.sign_error_message.draw()
            self.textbox_colour(self.textbox_states, 0, self.rectangle3)    
            self.textbox_colour(self.textbox_states, 1, self.rectangle5)    
            self.textbox_colour(self.textbox_states, 2, self.rectangle6)    
        if self.screenOn[7] == 1:
            if self.SHOW_LAPS == True:
                self.lap_splits_label2 = pyglet.text.Label(self.display_times, multiline=True, width=500, font_name='Zen Dots', font_size=20, x=10, y=800, color=(220, 220 ,220, 1000), batch=self.raceExtras)
            self.raceExtras.draw()
            if self.SHOW_WALLS == True:
                self.wall_lines.draw()
            if self.SHOW_CARS == True:
                self.player1.car.draw()
            if self.SHOW_GATES == True:
                self.gate_lines.draw()
            if self.SHOW_RAYS == True:
                pointsList = []
                #adding all the rays to the batch
                for ray in self.player1.new_rays:
                    ray.batch = self.ai_lines
                    ray.opacity = 100
                #adding all the points where the ray collides with the cloest wall to the batch
                for point in self.player1.collisionPointsList:
                    pointsList.append(pyglet.shapes.Circle(x=point[0], y=point[1], radius=5, color=(255,0,0), batch=self.ai_lines))
                
                self.ai_lines.draw()
            #self.flip() #for the ai, can be removed for casual play
        if self.screenOn[6] == 1:
            self.backdrop2.draw()
            self.pauseMenu.draw()
            #update labels on screen:
            self.label_accountName = pyglet.text.Label("username: " + str(self.account_name), font_name='Zen Dots', bold=True, color=(220, 220 ,220, 1000), font_size=13, x=20, y=690, batch=self.pauseMenu)
            if self.account_best_lap == 0.0:
                self.label_bestLap = pyglet.text.Label("best lap:  -- ", font_name='Zen Dots', bold=True, color=(220, 220 ,220, 1000), font_size=13, x=20, y=650, batch=self.pauseMenu)
                self.label_bestLapDate = pyglet.text.Label("achieved on: -- ", font_name='Zen Dots', bold=True, color=(220, 220 ,220, 1000), font_size=13, x=20, y=610, batch=self.pauseMenu)
            else:
                self.label_bestLap = pyglet.text.Label("best lap: " + str(self.account_best_lap) + " seconds", font_name='Zen Dots', bold=True, color=(220, 220 ,220, 1000), font_size=13, x=20, y=650, batch=self.pauseMenu)
                self.label_bestLapDate = pyglet.text.Label("achieved on: " + str(self.account_best_lap_date), font_name='Zen Dots', bold=True, color=(220, 220 ,220, 1000), font_size=13, x=20, y=610, batch=self.pauseMenu)
        if self.screenOn[5] == 1:
            self.confirm.draw()
        if self.screenOn[4] == 1:
            self.leaderboardDisplays.draw()
            self.label9 = pyglet.text.Label(self.text_search, font_name='Arial', font_size=22, x=535, y=50, batch=self.leaderboardDisplays)
            self.arrow_colour(self.arrowStates, 0, self.usernameBox)
            self.arrow_colour(self.arrowStates, 1, self.dateBox)
            self.arrow_colour(self.arrowStates, 2, self.timeBox)
        if self.screenOn[3] == 1:
            self.cp.draw()
            self.cp_error_message.draw()
            self.textbox_colour(self.textbox_states_cp, 0, self.rectangle10)    
            self.textbox_colour(self.textbox_states_cp, 1, self.rectangle11)    
            self.textbox_colour(self.textbox_states_cp, 2, self.rectangle12)  

    def on_key_press(self, symbol, modifiers):
        #if the log in screen is on
        if self.screenOn[1] == 1:
            if self.selected_textbox_log == 1:
                if symbol == key.LSHIFT or symbol == key.RSHIFT:
                    self.next_letter = True
                if self.next_letter == True:
                    if key.A <= symbol <= key.Z:
                        if len(self.text_log_input1) < 20:
                            self.text_log_input1 = self.text_log_input1 + str(chr(symbol)).upper()
                        self.next_letter = False
                else:
                    if symbol == key.BACKSPACE:
                        self.text_log_input1 = self.text_log_input1[:-1]
                    elif key.A <= symbol <= key.Z or symbol == key.SPACE:
                        if len(self.text_log_input1) < 20:
                            self.text_log_input1 = self.text_log_input1 + str(chr(symbol))

                self.label1 = pyglet.text.Label(self.text_log_input1, font_name='Arial', font_size=20, x=460, y=535, batch=self.logExtras)

            elif self.selected_textbox_log == 2:
                if symbol == key.LSHIFT or symbol == key.RSHIFT:
                    self.next_letter2 = True
                if symbol == key.BACKSPACE:
                    self.text_log_input2 = self.text_log_input2[:-1]
                if self.next_letter2 == True:
                    if key.A <= symbol <= key.Z:
                        if len(self.text_log_input2) < 20:
                            self.text_log_input2 = self.text_log_input2 + str(chr(symbol)).upper()
                        self.next_letter2 = False
                else:
                    if symbol != key.BACKSPACE:
                        if len(self.text_log_input2) < 20:
                            self.text_log_input2 = self.text_log_input2 + str(chr(symbol))

                self.label2 = pyglet.text.Label(self.text_log_input2, font_name='Arial', font_size=20, x=460, y=425, batch=self.logExtras)

        elif self.screenOn[2] == 1:
            if self.selected_textbox_sign == 1:
                if symbol == key.LSHIFT or symbol == key.RSHIFT:
                    self.next_letter3 = True
                if self.next_letter3 == True:
                    if key.A <= symbol <= key.Z:
                        if len(self.text_sign_input1) < 20:
                            self.text_sign_input1 = self.text_sign_input1 + str(chr(symbol)).upper()
                        self.next_letter3 = False
                else:
                    if symbol == key.BACKSPACE:
                        self.text_sign_input1 = self.text_sign_input1[:-1]
                    elif key.A <= symbol <= key.Z or symbol == key.SPACE:
                        if len(self.text_sign_input1) < 20:
                            self.text_sign_input1 = self.text_sign_input1 + str(chr(symbol))

                self.label3 = pyglet.text.Label(self.text_sign_input1, font_name='Arial', font_size=20, x=460, y=535, batch=self.signExtras)
            if self.selected_textbox_sign == 2:
                if symbol == key.LSHIFT or symbol == key.RSHIFT:
                    self.next_letter4 = True
                if symbol == key.BACKSPACE:
                    self.text_sign_input2 = self.text_sign_input2[:-1]
                if self.next_letter4 == True:
                    if key.A <= symbol <= key.Z:
                        if len(self.text_sign_input2) < 20:
                            self.text_sign_input2 = self.text_sign_input2 + str(chr(symbol)).upper()
                        self.next_letter4 = False
                else:
                    if symbol != key.BACKSPACE:
                        if len(self.text_sign_input2) < 20:
                            self.text_sign_input2 = self.text_sign_input2 + str(chr(symbol))

                self.label4 = pyglet.text.Label(self.text_sign_input2, font_name='Arial', font_size=20, x=460, y=425, batch=self.signExtras)
            if self.selected_textbox_sign == 3:
                if symbol == key.LSHIFT or symbol == key.RSHIFT:
                    self.next_letter5 = True
                if symbol == key.BACKSPACE:
                    self.text_sign_input3 = self.text_sign_input3[:-1]
                if self.next_letter5 == True:
                    if key.A <= symbol <= key.Z:
                        if len(self.text_sign_input3) < 20:
                            self.text_sign_input3 = self.text_sign_input3 + str(chr(symbol)).upper()
                        self.next_letter5 = False
                else:
                    if symbol != key.BACKSPACE:
                        if len(self.text_sign_input3) < 20:
                            self.text_sign_input3 = self.text_sign_input3 + str(chr(symbol))

                self.label5 = pyglet.text.Label(self.text_sign_input3, font_name='Arial', font_size=20, x=460, y=315, batch=self.signExtras)

        elif self.screenOn[3] == 1:
            if self.selected_textbox_cp == 1:
                if symbol == key.LSHIFT or symbol == key.RSHIFT:
                    self.next_letter6 = True
                if self.next_letter6 == True:
                    if key.A <= symbol <= key.Z:
                        if len(self.text_cp_input1) < 20:
                            self.text_cp_input1 = self.text_cp_input1 + str(chr(symbol)).upper()
                        self.next_letter6 = False
                else:
                    if symbol != key.BACKSPACE:
                        if len(self.text_cp_input1) < 20:
                            self.text_cp_input1 = self.text_cp_input1 + str(chr(symbol))

                self.label6 = pyglet.text.Label(self.text_cp_input1, font_name='Arial', font_size=20, x=460, y=535, batch=self.cp)
            if self.selected_textbox_cp == 2:
                if symbol == key.LSHIFT or symbol == key.RSHIFT:
                    self.next_letter7 = True
                if symbol == key.BACKSPACE:
                    self.text_cp_input2 = self.text_cp_input2[:-1]
                if self.next_letter7 == True:
                    if key.A <= symbol <= key.Z:
                        if len(self.text_cp_input2) < 20:
                            self.text_cp_input2 = self.text_cp_input2 + str(chr(symbol)).upper()
                        self.next_letter7 = False
                else:
                    if symbol != key.BACKSPACE:
                        if len(self.text_cp_input2) < 20:
                            self.text_cp_input2 = self.text_cp_input2 + str(chr(symbol))

                self.label7 = pyglet.text.Label(self.text_cp_input2, font_name='Arial', font_size=20, x=460, y=425, batch=self.cp)
            if self.selected_textbox_cp == 3:
                if symbol == key.LSHIFT or symbol == key.RSHIFT:
                    self.next_letter8 = True
                if symbol == key.BACKSPACE:
                    self.text_cp_input3 = self.text_cp_input3[:-1]
                if self.next_letter8 == True:
                    if key.A <= symbol <= key.Z:
                        if len(self.text_cp_input3) < 20:
                            self.text_cp_input3 = self.text_cp_input3 + str(chr(symbol)).upper()
                        self.next_letter8 = False
                else:
                    if symbol != key.BACKSPACE:
                        if len(self.text_cp_input3) < 20:
                            self.text_cp_input3 = self.text_cp_input3 + str(chr(symbol))

                self.label8 = pyglet.text.Label(self.text_cp_input3, font_name='Arial', font_size=20, x=460, y=315, batch=self.cp)

        elif self.screenOn[4] == 1:
            if self.searchBar.color == (0,0,0,150):
                if symbol == key.LSHIFT or symbol == key.RSHIFT:
                    self.next_letter9 = True
                if symbol == key.BACKSPACE:
                    self.text_search = self.text_search[:-1]
                if self.next_letter9 == True:
                    if key.A <= symbol <= key.Z:
                        if len(self.text_search) < 20:
                            self.text_search = self.text_search + str(chr(symbol)).upper()
                        self.next_letter9 = False
                else:
                    if symbol != key.BACKSPACE:
                        if len(self.text_search) < 20:
                            self.text_search = self.text_search + str(chr(symbol))
        
        #if the racing screen is on (or the pause screen so that the user can hold down the keys they want to press before pressing play)
        if self.screenOn[6] == 1 or self.screenOn[7] == 1:
            self.player1.on_key_press(symbol, modifiers)
            self.user_action = self.player1.action_list
    
    def on_key_release(self, symbol, modifiers):
        if self.screenOn[6] == 1 or self.screenOn[7] == 1:
            self.player1.on_key_release(symbol, modifiers)
            self.user_action = self.player1.action_list

    def on_mouse_press(self, x,y,button, modifiers):
        if button == mouse.RIGHT:
            print(x,y)
        if button == mouse.LEFT:
            if self.screenOn == [1,0,0,0,0,0,0,0]:
                if x > 525 and x < 930:
                    if y > 195 and y < 300:
                        if self.logged == True:
                            self.screenOn = [0,0,0,0,0,0,0,1]
                        else:
                            self.screenOn = [1,1,0,0,0,0,0,0]
            elif self.screenOn[1] == 1:
                #for all buttons
                if 449 < x < 951:
                    #for text boxes
                    if 519 < y < 571:
                        self.selected_textbox_log = 1
                        self.textbox_states = [2,0,0]
                    elif 409 < y < 451:
                        self.selected_textbox_log = 2
                        self.textbox_states = [0,2,0]

                    #for the enter button
                    if 769 < x < 951:
                        if 179 < y < 231:
                            if self.check_if_in_db(self.text_log_input1, self.text_log_input2) == 0:
                                self.screenOn = [0,0,0,0,0,0,0,1]
                                self.logged = True
                                self.log_error_message = self.dummy
                                self.account_name = self.text_log_input1
                                self.account_password = self.text_log_input2
                                self.account_best_lap = self.get_data_db(self.account_name,3)
                                self.account_best_lap_date = self.get_data_db(self.account_name,2)
                                #checking if admin
                                if self.account_name == "Rico Taylor":
                                    self.admin = True
                                if self.admin == True:
                                    thread = threading.Thread(target=adminFunction)
                                    thread.start()
                            
                            elif self.check_if_in_db(self.text_log_input1, self.text_log_input2) == 1:
                                self.log_error_message = self.badPassword
                            else:
                                self.log_error_message = self.noUsername

                    #for the sign up button
                    if 649 < x < 792:
                        if 303 < y < 337:
                            self.screenOn[1] = 0
                            self.screenOn[2] = 1
                            if self.selected_textbox_sign == 1:
                                self.textbox_states = [2,0,0]
                            elif self.selected_textbox_sign == 2:
                                self.textbox_states = [0,2,0]
                            else:
                                self.textbox_states = [0,0,2]            
            elif self.screenOn[2] == 1:
                #for the back button
                if 449 < x < 497:
                    if 626 < y < 674:
                        self.screenOn[1] = 1
                        self.screenOn[2] = 0
                        if self.selected_textbox_log == 2:
                            self.textbox_states = [0,2,0]
                        else:
                            self.textbox_states = [2,0,0]
                        
                #for the text boxes
                if 449 < x < 951:
                    if 519 < y < 571:
                        self.selected_textbox_sign = 1
                        self.textbox_states = [2,0,0]
                    elif 409 < y < 451:
                        self.selected_textbox_sign = 2
                        self.textbox_states = [0,2,0]
                    elif 299 < y < 351:
                        self.selected_textbox_sign = 3
                        self.textbox_states = [0,0,2]
                #for the enter button
                    if 769 < x < 951:
                        if 179 < y < 231:
                            if self.text_sign_input2 != self.text_sign_input3:
                                self.sign_error_message = self.doesNotMatch
                            elif len(self.text_sign_input2) < 8:
                                self.sign_error_message = self.tooShort
                            elif self.check_username_db(self.text_sign_input1) == True:
                                self.sign_error_message = self.userExists
                            else:
                                self.new_player_db(self.text_sign_input1, self.text_sign_input2)
                                self.screenOn = [0,0,0,0,0,0,0,1]
                                self.sign_error_message = self.dummy
                                self.logged = True
                                self.account_name = self.text_sign_input1
                                self.account_password = self.text_sign_input2
                                self.account_best_lap = self.get_data_db(self.account_name,3)
                                self.account_best_lap_date = self.get_data_db(self.account_name,2)

                                #update database actions
                                self.new_data_entry_actions("create_account",str(self.find_date()))
            elif self.screenOn[3] == 1:
                #for the text boxes
                if 449 < x < 951:
                    if 519 < y < 571:
                        self.selected_textbox_cp = 1
                        self.textbox_states_cp = [2,0,0]
                    elif 409 < y < 451:
                        self.selected_textbox_cp = 2
                        self.textbox_states_cp = [0,2,0]
                    elif 299 < y < 351:
                        self.selected_textbox_cp = 3
                        self.textbox_states_cp = [0,0,2]
                
                #back button
                if 449 < x < 501:
                    if 179 < y < 231:
                        self.screenOn[3] = 0

                #for the enter button
                if 769 < x < 951:
                    if 179 < y < 231:
                        if self.check_if_in_db(self.account_name, self.text_cp_input1) == 1:
                            self.cp_error_message = self.incorrect_old_password
                        elif self.text_cp_input2 != self.text_cp_input3:
                                self.cp_error_message = self.doesNotMatch
                        elif len(self.text_cp_input2) < 8:
                                self.cp_error_message = self.tooShort
                        else:
                            self.cp_error_message = self.dummy
                            self.update_password_db(self.account_name, self.text_cp_input2)
                            self.screenOn[3] = 0
                            self.account_password = self.text_cp_input2

                            #update actions database
                            self.new_data_entry_actions("update_password",self.find_date())
            elif self.screenOn[4] == 1:
                #back button
                if 49 < x < 131:
                    if 769 < y < 851:
                        self.screenOn[4] = 0
                
                #sorting arrows
                if 719 < y < 737:
                    if 539 < x < 557:
                        self.selected_arrow = 1
                        self.arrowStates = [2,0,0]
                        self.Order = 0
                        self.show_table(self.data)
                    elif 799 < x < 817:
                        self.selected_arrow = 2
                        self.arrowStates = [0,2,0]
                        self.Order = 2
                        self.show_table(self.data)
                    elif 1092 < x < 1110:
                        self.selected_arrow = 3
                        self.arrowStates = [0,0,2]
                        self.Order = 3
                        self.show_table(self.data)
                
                #search bar
                if 525 < x < 1025:
                    if 35 < y < 85:
                        self.searchBar.color = (0,0,0)
                
                #search button
                if 1027 < x < 1077:
                    if 24 < y < 76:
                        self.show_table(self.select(self.get_db(), self.text_search))
            elif self.screenOn[5] == 1:
                #cancel button
                if 75 < x < 231:
                    if 347 < y < 403:
                        self.screenOn[5] = 0
                
                #delete button
                if 287 < x < 439:
                    if 349 < y < 401:
                        self.delete_player_db(self.account_name)
                        self.reset()
                        self.screenOn = [1,0,0,0,0,0,0,0]
                        self.account_name = ""
                        self.account_password = ""
                        self.account_best_lap = 0.0
                        self.account_best_lap_date = ""
                        self.logged = False
                        self.text_log_input1 = str()
                        self.text_log_input2 = str()
                        self.text_sign_input1 = str()
                        self.text_sign_input2 = str()
                        self.text_sign_input3 = str()
                        self.text_cp_input1 = str()
                        self.text_cp_input2 = str()
                        self.text_cp_input3 = str()
                        self.selected_textbox_log = 1
                        self.selected_textbox_sign = 1
                        self.selected_textbox_cp = 1
                        self.label1 = pyglet.text.Label(self.text_log_input1, font_name='Arial', font_size=20, x=700, y=700, batch=self.logExtras)
                        self.label2 = pyglet.text.Label(self.text_log_input2, font_name='Arial', font_size=20, x=700, y=700, batch=self.logExtras)
                        self.label3 = pyglet.text.Label(self.text_sign_input1, font_name='Arial', font_size=20, x=700, y=700, batch=self.signExtras)
                        self.label4 = pyglet.text.Label(self.text_sign_input2, font_name='Arial', font_size=20, x=700, y=700, batch=self.signExtras)
                        self.label5 = pyglet.text.Label(self.text_sign_input3, font_name='Arial', font_size=20, x=700, y=700, batch=self.signExtras)
                        self.label6 = pyglet.text.Label(self.text_cp_input1, font_name='Arial', font_size=20, x=700, y=700, batch=self.cp)
                        self.label7 = pyglet.text.Label(self.text_cp_input2, font_name='Arial', font_size=20, x=700, y=700, batch=self.cp)
                        self.label8 = pyglet.text.Label(self.text_cp_input3, font_name='Arial', font_size=20, x=700, y=700, batch=self.cp)

                        #update actions database
                        self.new_data_entry_actions("delete_account",self.find_date())
            elif self.screenOn[6] == 1:
                #restart button
                if 679 < y < 710:
                    if 587 < x < 848:
                        self.reset()
                        self.screenOn[6] = 0

                #leaderboard button
                if 589 < y < 620:
                    if 491 < x < 942:
                        self.screenOn[4] = 1
                        self.label_leaderboards.color = (180, 180, 180, 150)
                        self.underline2.opacity = 0

                        #updates the table for the leaderboard screen
                        self.show_table(self.get_db())
                        self.text_search = str()
                        self.searchBar.color = (255,255,255,150)

                #back to entry button
                elif 499 < y < 530:
                    if 371 < x < 1053:
                        self.reset()
                        self.screenOn = [1,0,0,0,0,0,0,0]
                
                #change password button
                elif 409 < y < 440:
                    if 443 < x < 1055:
                        self.screenOn[3] = 1
                        self.label_changePassword.color = (180, 180, 180, 150)
                        self.underline4.opacity = 0

                #log out button
                elif 319 < y < 350:
                    if 597 < x < 843:
                        self.reset()
                        self.screenOn = [1,0,0,0,0,0,0,0]
                        self.account_name = ""
                        self.account_password = ""
                        self.account_best_lap = 0.0
                        self.account_best_lap_date = ""
                        self.logged = False
                        self.text_log_input1 = str()
                        self.text_log_input2 = str()
                        self.text_sign_input1 = str()
                        self.text_sign_input2 = str()
                        self.text_sign_input3 = str()
                        self.text_cp_input1 = str()
                        self.text_cp_input2 = str()
                        self.text_cp_input3 = str()
                        self.selected_textbox_log = 1
                        self.selected_textbox_sign = 1
                        self.selected_textbox_cp = 1
                        self.label1 = pyglet.text.Label(self.text_log_input1, font_name='Arial', font_size=20, x=700, y=700, batch=self.logExtras)
                        self.label2 = pyglet.text.Label(self.text_log_input2, font_name='Arial', font_size=20, x=700, y=700, batch=self.logExtras)
                        self.label3 = pyglet.text.Label(self.text_sign_input1, font_name='Arial', font_size=20, x=700, y=700, batch=self.signExtras)
                        self.label4 = pyglet.text.Label(self.text_sign_input2, font_name='Arial', font_size=20, x=700, y=700, batch=self.signExtras)
                        self.label5 = pyglet.text.Label(self.text_sign_input3, font_name='Arial', font_size=20, x=700, y=700, batch=self.signExtras)
                        self.label6 = pyglet.text.Label(self.text_cp_input1, font_name='Arial', font_size=20, x=700, y=700, batch=self.cp)
                        self.label7 = pyglet.text.Label(self.text_cp_input2, font_name='Arial', font_size=20, x=700, y=700, batch=self.cp)
                        self.label8 = pyglet.text.Label(self.text_cp_input3, font_name='Arial', font_size=20, x=700, y=700, batch=self.cp)

                #resume button
                if 629 < x < 801:
                    if 79 < y < 261:     
                        self.resumeButton.opacity = 100
                        self.coverPlay.opacity = 0
                        self.screenOn[6] = 0

                        #timer
                        self.player1.timer.start()
                
                #turn off lap displays button
                if 1329 < x < 1431:
                    if 9 < y < 61:
                        if self.rectangle16.color == (34, 139, 34, 50): #if green (lap displays are on)
                            self.rectangle16.color = (210, 43, 43, 50)
                            self.SHOW_LAPS = False
                        else: #if red (lap displays are off)
                            self.rectangle16.color = (34, 139, 34, 50)
                            self.SHOW_LAPS = True
                
                #delete button (hover)
                if 59 < x < 232:
                    if 558 < y < 571:
                        self.label_delete.color = (255,0,0,145)
                        self.delete_underline.opacity = 0
                        self.screenOn[5] = 1
            elif self.screenOn[7] == 1:
                #pause button
                if 1336 < x < 1409:
                    if 799 < y < 881:
                        self.screenOn[6] = 1
                        self.pauseBackdrop.opacity = 0
                        #redefining labels so that they can be updated
                        self.label_accountName = pyglet.text.Label("USERNAME: " + str(self.account_name), font_name='Zen Dots', bold=True, color=(220, 220 ,220, 1000), font_size=13, x=20, y=690, batch=self.pauseMenu)
                        self.label_bestLap = pyglet.text.Label("BEST LAP: " + str(self.account_best_lap), font_name='Zen Dots', bold=True, color=(220, 220 ,220, 1000), font_size=13, x=20, y=650, batch=self.pauseMenu)
                        self.label_bestLapDate = pyglet.text.Label("DATE ACHIEVED: " + str(self.account_best_lap_date), font_name='Zen Dots', bold=True, color=(220, 220 ,220, 1000), font_size=13, x=20, y=610, batch=self.pauseMenu)

                        #timer code
                        self.player1.timer.stop()

    def on_mouse_motion(self, x, y, dx, dy):
        if self.screenOn[1] or self.screenOn[2] == 1:
            #enter button hover effect
            if 769 < x < 951:
                if 179 < y < 231:
                    self.rectangle7.opacity = 150
            if not 769 < x < 951 or not 179 < y < 231:
                    self.rectangle7.opacity = 50
        if self.screenOn[1] == 1: #I am doing this seperately from the last one since three windows will have the enter button in the same place meaning it makes sense for it not to be repeated, so I might change the top one later
            #sign up button (reset)
            self.rectangle8.opacity = 50
            #sign up button (change)
            if 649 < x < 792:
                if 303 < y < 337:
                    self.rectangle8.opacity = 150

            #text boxes (reset)
            if self.selected_textbox_log == 1:
                self.textbox_states[0] = 2
                self.textbox_states[1] = 0
            else:
                self.textbox_states[0] = 0
                self.textbox_states[1] = 2
        
            #text boxes (colour based on location of mouse)
            if 449 < x < 951:
                if 519 < y < 571:
                    if self.textbox_states[0] == 0:
                        self.textbox_states[0] = 1
                elif 409 < y < 461:
                    if self.textbox_states[1] == 0:
                        self.textbox_states[1] = 1
        elif self.screenOn[2] == 1:
            #back button (reset)
            self.rectangle9.opacity = 50
            #back button (change)
            if 449 < x < 497:
                if 626 < y < 674:
                    self.rectangle9.opacity = 150
            
            #text boxes (reset)
            if self.selected_textbox_sign == 1:
                self.textbox_states = [2,0,0]
            elif self.selected_textbox_sign == 2:
                self.textbox_states = [0,2,0]
            else:
                self.textbox_states = [0,0,2]

            #text boxes (colour based on location of mouse)
            if 449 < x < 951:
                if 519 < y < 571:
                    if self.textbox_states[0] == 0:
                        self.textbox_states[0] = 1
                elif 409 < y < 461:
                    if self.textbox_states[1] == 0:
                        self.textbox_states[1] = 1
                elif 299 < y < 351:
                    if self.textbox_states[2] == 0:
                        self.textbox_states[2] = 1
        elif self.screenOn[3] == 1:
            #back button (reset)
            self.rectangle14.opacity = 50
            #back button (change)
            if 449 < x < 501:
                    if 179 < y < 231:
                        self.rectangle14.opacity = 150

            #enter button (reset)
            self.rectangle13.opacity = 50
            #enter button (change)
            if 769 < x < 951:
                if 179 < y < 231:
                    self.rectangle13.opacity = 150
            
            #text boxes (reset)
            if self.selected_textbox_cp == 1:
                self.textbox_states_cp = [2,0,0]
            elif self.selected_textbox_cp == 2:
                self.textbox_states_cp = [0,2,0]
            else:
                self.textbox_states_cp = [0,0,2]

            #text boxes (colour based on location of mouse)
            if 449 < x < 951:
                if 519 < y < 571:
                    if self.textbox_states_cp[0] == 0:
                        self.textbox_states_cp[0] = 1
                elif 409 < y < 461:
                    if self.textbox_states_cp[1] == 0:
                        self.textbox_states_cp[1] = 1
                elif 299 < y < 351:
                    if self.textbox_states_cp[2] == 0:
                        self.textbox_states_cp[2] = 1
        elif self.screenOn[4] == 1:
            #back button (reset)
            self.rectangle15.opacity = 50

            #50 770, 8080
            #back button (hover)
            if 49 < x < 131:
                if 769 < y < 851:
                    self.rectangle15.opacity = 150
            
            #down arrows (reset)
            if self.selected_arrow == 1:
                self.arrowStates = [2,0,0]
            elif self.selected_arrow == 2:
                self.arrowStates = [0,2,0]
            elif self.selected_arrow == 3:
                self.arrowStates = [0,0,2]
            
            #down arrows (hover)
            if 719 < y < 737:
                if 539 < x < 557:
                    if self.selected_arrow != 1:
                        self.arrowStates[0] = 1
                elif 799 < x < 817:
                    if self.selected_arrow != 2:
                        self.arrowStates[1] = 1
                elif 1092 < x < 1110:
                    if self.selected_arrow != 3:
                        self.arrowStates[2] = 1
            
            #search bar (reset)
            if self.searchBar.color != (0,0,0, 150):
                self.searchBar.color = (255,255,255)

            #search bar (hover)
            if 524 < x < 1026:
                if 34 < y < 86:
                    if self.searchBar.color != (0,0,0,150):
                        self.searchBar.color = (126,126,126)

            #search button (reset)
            self.searchButton.color = (0,0,0,100)

            #search button (hover)
            if 1027 < x < 1077:
                if 24 < y < 76:
                    self.searchButton.color = (255,255,255,100)
        elif self.screenOn[5] == 1:
            #cancel button (reset)
            self.cancelButton.opacity = 255
            #concel button (hover)
            #x=76, y=348, height=54, width=154
            if 75 < x < 231:
                if 347 < y < 403:
                    self.cancelButton.opacity = 150
            
            #confirm delete (reset)
            self.confirmButton.color = (40,40,40)

            #confirm delete (hover)
            if 287 < x < 439:
                if 349 < y < 401:
                    self.confirmButton.color = (70, 0, 0)
        elif self.screenOn[6] == 1:
            #play button (reset)
            self.resumeButton.opacity = 100
            self.coverPlay.opacity = 0
            #play button(on hover)
            if 629 < x < 801:
                if 79 < y < 261:     
                    self.resumeButton.opacity = 250
                    self.coverPlay.opacity = 50
            
            #labels (reset) and lines (reset)
            self.label_restart.color = (180, 180, 180, 150)
            self.label_leaderboards.color = (180, 180, 180, 150)
            self.label_btes.color = (180, 180, 180, 150)
            self.label_changePassword.color = (180, 180, 180, 150)
            self.label_logOut.color = (180, 180, 180, 150)

            self.underline1.opacity = 0
            self.underline2.opacity = 0
            self.underline3.opacity = 0
            self.underline4.opacity = 0
            self.underline5.opacity = 0

            #labels (on hover)
            if 679 < y < 710:
                if 587 < x < 848:
                    self.label_restart.color = (255, 255, 255, 1000)
                    self.underline1.opacity = 255
            elif 589 < y < 620:
                if 491 < x < 942:
                    self.label_leaderboards.color = (255, 255, 255, 1000)
                    self.underline2.opacity = 255
            elif 499 < y < 530:
                if 371 < x < 1053:
                    self.label_btes.color = (255, 255, 255, 1000)
                    self.underline3.opacity = 255
            elif 409 < y < 440:
                if 443 < x < 1055:
                    self.label_changePassword.color = (255, 255, 255, 1000)
                    self.underline4.opacity = 255
            elif 319 < y < 350:
                if 597 < x < 843:
                    self.label_logOut.color = (255, 255, 255, 1000)
                    self.underline5.opacity = 255
            
            #delete button (reset)
            self.label_delete.color = (255,0,0,145)
            self.delete_underline.opacity = 0

            #delete button (hover)
            if 59 < x < 232:
                if 558 < y < 571:
                    self.label_delete.color = (255,0,0,255)
                    self.delete_underline.opacity = 255
        elif self.screenOn[7] == 1:
            #pause button (reset)
            self.pauseBackdrop.opacity = 10
            #pause button
            if 1336 < x < 1409:
                if 799 < y < 881:
                    self.pauseBackdrop.opacity = 100
    
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        if self.screenOn[4] == 1:
            if scroll_y > 0 and self.scroll_offset > 0:
                self.scroll_offset -= 1  # Scroll up
            elif scroll_y < 0 and self.scroll_offset < len(self.data) - self.visible_rows:
                self.scroll_offset += 1  # Scroll down
            self.show_table(self.data)

    def update(self,dt):
        if self.screenOn == [0,0,0,0,0,0,0,1]:
            self.screen_displays()
            self.step(self.user_action)
        self.render()
            
    def end(self):
        self.close()

if __name__ == '__main__':
    screen = RacingEnv()
    pyglet.clock.schedule_interval(screen.update, 1/60)
    pyglet.app.run()



