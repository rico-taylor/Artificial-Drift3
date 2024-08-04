#importing variables
import pyglet
import time
import random
from pyglet import sprite, image
from pyglet.window import key, mouse
from math import sin, cos, atan, acos, asin, radians, sqrt, tanh

from walls import get_lines

#main window
window = pyglet.window.Window(resizable = False, caption="Artificial Drift")
window.set_fullscreen(True)

lines = pyglet.graphics.Batch()

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
        self.backward = False
        self.clockwise = False
        self.aclockwise = False

        self.velocity = 0 *scale_factor
        self.max_velocity = 8 *scale_factor
        self.friction = 0.07 *scale_factor
        self.acceleration = 0.1 *scale_factor
        self.rotation_speed = 3
        self.drift_time = 8 *scale_factor
    
    def on_key_press(self, symbol,modifiers):
        if symbol == key.UP:
            self.forward = True
        if symbol == key.DOWN:
            self.backward = True
        if symbol == key.LEFT:
            self.aclockwise = True
        if symbol == key.RIGHT:
            self.clockwise = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.forward = False
        if symbol == key.DOWN:
            self.backward = False
        if symbol == key.LEFT:
            self.aclockwise = False
        if symbol == key.RIGHT:
            self.clockwise = False


    def update(self, dt):
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
        if self.forward == True:
            self.velocity += self.acceleration
        if self.backward == True:
            self.velocity -= self.acceleration/1.3
        #making the car turn left and right
        if self.aclockwise == True:
            self.car.rotation -= self.rotation_speed
        if self.clockwise == True:
            self.car.rotation += self.rotation_speed

        

        dy = self.velocity * cos(radians(self.car.rotation))
        dx = self.velocity * sin(radians(self.car.rotation))

        self.car.y += dy
        self.car.x += dx

player1 = Car(100,100,45,"images/car.png")

walls = get_lines(window.width, window.height)
for wall in walls:
    wall.batch = lines

@window.event
def on_draw():
    window.clear()
    lines.draw()
    player1.car.draw()

@window.event
def on_key_press(symbol, modifiers):
    player1.on_key_press(symbol, modifiers)

@window.event
def on_key_release(symbol, modifiers):
    player1.on_key_release(symbol, modifiers)

pyglet.clock.schedule_interval(player1.update, 1/60)

pyglet.app.run()