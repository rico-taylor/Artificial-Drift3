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