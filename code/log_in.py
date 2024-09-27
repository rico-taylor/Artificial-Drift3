import pyglet
import time
import random
from pyglet import sprite, image
from pyglet.window import key, mouse
from math import sin, cos, atan, acos, asin, radians, sqrt, tanh

text_input1 = str()
text_input2 = str()
text_input3 = str()

selected_textbox = 1

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

#"password"
password_img = image.load("images/text_password.png")
password_img.anchor_x = password_img.width//2
password_img.anchor_y = password_img.height//2
passwordHeading = sprite.Sprite(password_img, x=windowwidth//2-200, y=windowheight//2 +30, batch=loginDisplays)
passwordHeading.scale = 0.1*scale_factor

#"confirm password"
confirm_img = image.load("images/text_confirm-password.png")
confirm_img.anchor_x = confirm_img.width//2
confirm_img.anchor_y = confirm_img.height//2
confirmHeading = sprite.Sprite(confirm_img, x=windowwidth//2-140, y=windowheight//2 -80, batch=loginDisplays)
confirmHeading.scale = 0.15*scale_factor

#textbox1
rectangle3 = pyglet.shapes.Rectangle(x=450, y=520, width=500, height=50, color=(255, 255, 255), batch=loginDisplays)
rectangle3.opacity = 50

#textbox2
rectangle5 = pyglet.shapes.Rectangle(x=450, y=410, width=500, height=50, color=(255, 255, 255), batch=loginDisplays)
rectangle5.opacity = 50

#textbox3
rectangle6 = pyglet.shapes.Rectangle(x=450, y=300, width=500, height=50, color=(255, 255, 255), batch=loginDisplays)
rectangle6.opacity = 50

#label
label1 = pyglet.text.Label(text_input1, font_name='Arial', font_size=20, x=700, y=700, batch=loginDisplays)
label2 = pyglet.text.Label(text_input2, font_name='Arial', font_size=20, x=700, y=700, batch=loginDisplays)
label3 = pyglet.text.Label(text_input3, font_name='Arial', font_size=20, x=700, y=700, batch=loginDisplays)


@window.event
def on_draw():
    loginDisplays.draw()

next_letter = False
@window.event
def on_key_press(symbol,modifiers):
    global text_input1
    global text_input2
    global text_input3
    global selected_textbox
    global next_letter
    global label1
    global label2
    global label3
    if selected_textbox == 1:
        if symbol == key.LSHIFT or symbol == key.RSHIFT:
            next_letter = True
        if next_letter == True:
            if key.A <= symbol <= key.Z:
                text_input1 = text_input1 + str(chr(symbol)).upper()
                next_letter = False
        else:
            if symbol == key.BACKSPACE:
                text_input1 = text_input1[:-1]
            elif key.A <= symbol <= key.Z or symbol == key.SPACE:
                text_input1 = text_input1 + str(chr(symbol))

        label1 = pyglet.text.Label(text_input1, font_name='Arial', font_size=20, x=460, y=535, batch=loginDisplays)
    elif selected_textbox == 2:
        if symbol == key.BACKSPACE:
            text_input2 = text_input2[:-1]
        else:
            text_input2 = text_input2 + str(chr(symbol))

        label2 = pyglet.text.Label(text_input2, font_name='Arial', font_size=20, x=460, y=425, batch=loginDisplays)
        rectangle3.color = (255,255,255)
        rectangle5.color = (0, 0, 0)
        rectangle6.color = (255, 255, 255)
    else:
        if symbol == key.BACKSPACE:
            print("here")
            text_input2 = text_input3[:-1]
        else:
            text_input3 = text_input3 + str(chr(symbol))

        label3 = pyglet.text.Label(text_input3, font_name='Arial', font_size=20, x=460, y=315, batch=loginDisplays)
        rectangle3.color = (255,255,255)
        rectangle5.color = (255, 255, 255)
        rectangle6.color = (0, 0, 0)


@window.event
def on_mouse_press(x,y,button, modifiers):
    global text_input1
    global selected_textbox
    if button == mouse.LEFT:
        if 449 < x < 951:
            if 519 < y < 571:
                selected_textbox = 1
                rectangle3.color = (0,0,0)
                rectangle5.color = (255, 255, 255)
                rectangle6.color = (255, 255, 255)
            elif 409 < y < 451:
                selected_textbox = 2
                rectangle3.color = (255,255,255)
                rectangle5.color = (0, 0, 0)
                rectangle6.color = (255, 255, 255)
            elif 299 < y < 351:
                selected_textbox = 3
                rectangle3.color = (255,255,255)
                rectangle5.color = (255, 255, 255)
                rectangle6.color = (0, 0, 0)


        
        print(x,y)

pyglet.app.run()