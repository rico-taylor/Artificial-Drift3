import pyglet
import time
import random
from pyglet import sprite, image
from pyglet.window import key, mouse
from math import sin, cos, atan, acos, asin, radians, sqrt, tanh

text_input = str()

#main window
window = pyglet.window.Window(resizable = False, caption="Artificial Drift")
window.set_fullscreen(True)

window.canvas

#scaling so that all screen sizes can play
scale_factor = (window.width/1920)%1
windowwidth = window.width
windowheight = window.height
scale_factor = 0.75

#defining batches
loginDisplays = pyglet.graphics.Batch()


#entry images
rectangle4 = pyglet.shapes.Rectangle(x=0, y=0, width=windowwidth, height=windowheight, color=(0, 106, 36), batch=loginDisplays)
rectangle4.opacity = 20

#inner box
rectangle2= pyglet.shapes.Rectangle(x=398, y=148, width=windowwidth-(400*2)+4, height=554, color=(0, 0, 0), batch=loginDisplays)
rectangle2.opacity = 16

#box
rectangle = pyglet.shapes.Rectangle(x=400, y=150, width=windowwidth-(400*2), height=550, color=(254, 106, 36), batch=loginDisplays)
rectangle.opacity = 16

#header
login_img = image.load("images/text_log-in.png")
login_img.anchor_x = login_img.width//2
login_img.anchor_y = login_img.height//2
loginHeading = sprite.Sprite(login_img, x=windowwidth//2, y=windowheight//2 +200, batch=loginDisplays)
loginHeading.scale = 0.26*scale_factor

#"username"
username_img = image.load("images/text_username.png")
username_img.anchor_x = username_img.width//2
username_img.anchor_y = username_img.height//2
usernameHeading = sprite.Sprite(username_img, x=windowwidth//2-200, y=windowheight//2 +140, batch=loginDisplays)
usernameHeading.scale = 0.1*scale_factor

#textbox1
rectangle3 = pyglet.shapes.Rectangle(x=450, y=520, width=500, height=50, color=(255, 255, 255), batch=loginDisplays)
rectangle3.opacity = 50

#label
label = pyglet.text.Label(text_input, font_name='Arial', font_size=20, x=700, y=800, batch=loginDisplays)


@window.event
def on_draw():
    loginDisplays.draw()

next_letter = False
@window.event
def on_key_press(symbol,modifiers):
    global text_input
    global next_letter
    global label
    if symbol == key.LSHIFT or symbol == key.RSHIFT:
        next_letter = True
    if next_letter == True:
        if key.A <= symbol <= key.Z:
            text_input = text_input + str(chr(symbol)).upper()
            next_letter = False
    else:
        if symbol == key.BACKSPACE:
            text_input = text_input[:-1]
        elif key.A <= symbol <= key.Z or symbol == key.SPACE:
            text_input = text_input + str(chr(symbol))

    label = pyglet.text.Label(text_input, font_name='Arial', font_size=20, x=500, y=500, batch=loginDisplays)


@window.event
def on_mouse_press(x,y,button, modifiers):
    global text_input
    if button == mouse.LEFT:
        print(text_input)
        text_input = str()

pyglet.app.run()