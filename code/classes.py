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

scale_factor = (window.width/1920)%1

class Car:
    def __init__(self,x,y,r,img): #x,y is the start position of the car, r is the start rotation of the car

        self.car_image = image.load(img)

        self.car_image.anchor_x = self.car_image.width// 2
        self.car_image.anchor_y = self.car_image.height // 2

        self.car = sprite.Sprite(self.car_image, x, y)
        self.car.scale = 0.1*scale_factor
        self.car.rotation = r

        self.velocity = 0
        self.forward = False
        self.acceleration = 0.1 *scale_factor
    
    def on_key_press(self,symbol,modifiers):
        if symbol == key.UP:
            self.forward = True
    
    def update(self):
        if self.forward == True:
            self.velocity += self.acceleration
        
            self.dy = self.velocity * cos(radians(self.car.rotation))
            self.dx = self.velocity * sin(radians(self.car.rotation))

            self.car.x += self.dx
            self.car.y += self.dy

player1 = Car(100,100,260,"images/car.png")

@window.event
def on_draw():
    window.clear()
    player1.update()
    player1.car.draw()

pyglet.app.run()