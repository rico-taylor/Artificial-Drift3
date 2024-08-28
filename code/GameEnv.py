#importing variables
import pyglet
import time
import random
from pyglet import sprite, image
from pyglet.window import key, mouse
from math import sin, cos, atan, acos, asin, radians, sqrt, tanh

#batches
wall_lines = pyglet.graphics.Batch()
gate_lines = pyglet.graphics.Batch()


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
    timer1 = pyglet.shapes.Line(x=995/1920 *window_width, y=100/1080 *window_height, x2=985/1920 *window_width, y2=250/1080 *window_height, width = 1, color=(255,165,0))
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
def chooseAction(int):
    if int == 1:
        action = [True, False, False, False, False]
    elif int == 2:
        action = [True, False, False, False, True]
    elif int == 3:
        action = [True, False, True, False, False]
    elif int == 4:
        action = [True, False, True, False, True]
    elif int == 5:
        action = [True, False, False, True, False]
    elif int == 6:
        action = [True, False, False, True, True]
    elif int == 7:
        action = [False, True, False, False, False]
    elif int == 8:
        action = [False, True, True, False, False]
    elif int == 9:
        action = [False, True, False, True, False]
    elif int == 10:
        action = [False, False, False, False, False]
    elif int == 11:
        action = [False, False, False, False, True]
    elif int == 12:
        action = [False, False, True, False, False]
    elif int == 13:
        action = [False, False, True, False, True]
    elif int == 14:
        action = [False, False, False, True, False]
    elif int == 15:
        action = [False, False, False, True, True]
    
    return action

walls = get_walls(windowwidth, windowheight)
for wall in walls:
    wall.batch = wall_lines

gates = get_gates(windowwidth, windowheight)
for gate in gates:
    gate.opacity = 40
    gate.batch = gate_lines

line_list = walls + gates

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

        self.lap_list = []

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
        self.observation_space = [0.0, 260, 540.7883010831061, 248.6026368207048, 122.23394041784448, 84.87471813575465, 68.58619476103772, 58.57323663106676, 80.89115626007674, 575.4958984540862, 89.799454388119, 63.25040349127835, 72.87139630657704, 89.1023960305774, 125.65244082804028, 240.87486636892078]

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
            self.lap_list.append(float("{:#.2f}".format(self.elapsed)))
            self.lapCompleted = False
            print(self.lap_list)

        self.current = time.time()
        if self.going == True:
            if self.swap == True:
                self.start = time.time()
        elif self.going == False:
            self.current = self.start
        self.elapsed = self.current - self.start
        self.swap = False
        
        return "{:#.2f}".format(self.elapsed)
    
    #function calculates the reward of each tick
    def reward(self):
        reward = 0
        if self.reward_gate == True and self.new_gate_signal == True:
            reward += 2
        if self.wall_collision == True:
            reward -= 3

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
        if symbol == self.forward_key:
            self.forward = True
        if symbol == self.backward_key:
            self.backward = True
        if symbol == self.left_key:
            self.aclockwise = True
        if symbol == self.right_key:
            self.clockwise = True
        if symbol == self.drift_key:
            self.drift = True
            self.rotation_speed = 3.5
            self.rounds = 0
        
        self.action_list = [self.forward, self.backward, self.clockwise, self.aclockwise, self.drift]

    #function for when the user realeses the key
    def on_key_release(self, symbol, modifiers):
        if symbol == self.forward_key:
            self.forward = False
        if symbol == self.backward_key:
            self.backward = False
        if symbol == self.left_key:
            self.aclockwise = False
        if symbol == self.right_key:
            self.clockwise = False
        if symbol == self.drift_key:
            self.drift = False
            self.rotation_speed = 3
        
        self.action_list = [self.forward, self.backward, self.clockwise, self.aclockwise, self.drift]

    #update function that is called every tick. Is used for the car movement, timing, collisions, etc.
    def action(self, actions):
        #----------CAR MOVEMENT----------#
        if type(actions) == int:
            print("here")
            self.actions = chooseAction(actions)
        else:
            print("here2")
            self.actions = actions
        print(actions)
        print(self.actions)
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
        
        self.observation_space = [self.velocity, self.car.rotation] + self.aiVisionList

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

        self.player1 = Car(car_start_x,car_start_y,260,"images/car.png", key.UP, key.DOWN, key.LEFT, key.RIGHT, key.LSHIFT)
        self.user_action = [False,False,False,False,False]

        #loading in walls
        self.walls = get_walls(windowwidth, windowheight)
        for wall in self.walls:
            wall.batch = self.wall_lines
        
        #loading in gates
        self.gates = get_gates(windowwidth, windowheight)
        for gate in self.gates:
            gate.opacity = 40
            gate.batch = self.gate_lines
        
        #defining the line list
        self.line_list = self.walls + self.gates

        #defining boolean which control if each aspect is rendered or not
        self.SHOW_WALLS = True
        self.SHOW_CARS = True
        self.SHOW_GATES = True
        self.SHOW_RAYS = False

        #amount of wall collisions in one episode
        self.hits = 0
        #length of the episode
        self.ticks = 0

        self.MAX_EPISODE_LENGTH = 1000
        
    def reset(self):
        self.player1 = Car(car_start_x,car_start_y,260,"images/car.png", key.UP, key.DOWN, key.LEFT, key.RIGHT, key.LSHIFT)
        
        #reloading in walls
        self.walls = get_walls(windowwidth, windowheight)
        for wall in self.walls:
            wall.batch = self.wall_lines
        
        #reloading in gates
        self.gates = get_gates(windowwidth, windowheight)
        for gate in self.gates:
            gate.opacity = 40
            gate.batch = self.gate_lines
        
        #redefining the line list
        self.line_list = self.walls + self.gates

        return self.player1.observation_space

    def step(self, action):
        done = False

        #updating the car
        self.player1.action(action)
        
        #finding the reward the car made
        reward = self.player1.tick_reward

        #getting the new state (observation space)
        new_state = self.player1.observation_space

        #checking if the edisode is over
        if reward < 0:
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

        return new_state, reward, done
        
    def render(self):
        self.clear()
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

    def on_key_press(self, symbol, modifiers):
        self.player1.on_key_press(symbol, modifiers)
        self.user_action = self.player1.action_list
    
    def on_key_release(self, symbol, modifiers):
        self.player1.on_key_release(symbol, modifiers)
        self.user_action = self.player1.action_list

    def update(self,dt):
        self.step(self.user_action)
        self.render()
            
    def end(self):
        self.close()


if __name__ == '__main__':
    screen = RacingEnv()
    pyglet.clock.schedule_interval(screen.update, 1/60)
    pyglet.app.run()



