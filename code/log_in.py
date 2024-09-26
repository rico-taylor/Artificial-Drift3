import pyglet
import time
import random
from pyglet import sprite, image
from pyglet.window import key, mouse
from math import sin, cos, atan, acos, asin, radians, sqrt, tanh

#main window
window = pyglet.window.Window(resizable = False, caption="Artificial Drift")
window.set_fullscreen(True)

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
logo = sprite.Sprite(logo_img, x=window.width//2, y=window.height//2 +100, batch=loginDisplays)
logo.scale = scale_factor

#play button
login_img = image.load("images/text_log-in.png")
login_img.anchor_x = login_img.windowwidth//2
login_img.anchor_y = login_img.windowheight//2
loginHeading = sprite.Sprite(login_img, x=windowwidth//2, y=windowheight//2, batch=loginDisplays)
loginHeading.scale = 0.5*scale_factor

#triangle decoration
triangle_img = image.load("images/triangle1_translucent.png")
triangle_img.anchor_x = triangle_img.width//2
triangle_img.anchor_y = triangle_img.height//2
triangle1 = sprite.Sprite(triangle_img, x=100, y=100, batch=entryDisplay)
triangle1.rotation = 30
triangle1.scale = 0.3*scale_factor