import pyglet
from pyglet import sprite, image
from pyglet.window import key

from math import sin, cos, radians

rectangle = pyglet.shapes.Rectangle(x=200, y=1000, width=1, height=80, color=(255,10,50))
rectangle.rotation = 45

half_width_rectangle = (rectangle.width // 2)
half_height_rectangle = (rectangle.height //2)

rectangle_hitbox = [
  rectangle.height*cos(1.57 - radians(rectangle.rotation))+rectangle.x,
  rectangle.height*sin(1.57 - radians(rectangle.rotation))+rectangle.y,

  rectangle.height*cos(1.57 - radians(rectangle.rotation))+rectangle.x+ rectangle.width*cos(radians(rectangle.rotation)), 
  rectangle.height*sin(1.57 - radians(rectangle.rotation))+rectangle.y - rectangle.width*sin(radians(rectangle.rotation)),

  rectangle.x, 
  rectangle.y,

  rectangle.x + (rectangle.width * cos(radians(rectangle.rotation))),
  rectangle.y - (rectangle.width *sin(radians(rectangle.rotation)))
  ] #top left, top right, bottom left, bottom right

rectangle_hitbox2 = [
  (rectangle.height*cos(1.57 - radians(rectangle.rotation))+rectangle.x, 
   rectangle.height*cos(1.57 - radians(rectangle.rotation))+rectangle.x+rectangle.width*cos(radians(rectangle.rotation)),
   rectangle.x,
   rectangle.x + (rectangle.width * cos(radians(rectangle.rotation)))),

  (rectangle.height*sin(1.57 - radians(rectangle.rotation))+rectangle.y,
   rectangle.height*sin(1.57 - radians(rectangle.rotation))+rectangle.y - rectangle.width*sin(radians(rectangle.rotation)),
   rectangle.y,
   rectangle.y - (rectangle.width * sin(radians(rectangle.rotation))))
  ] #x-co-ordinates, then y-co-ordinates

   
circle = pyglet.shapes.Circle(x=rectangle.height*cos(1.57 - radians(rectangle.rotation))+rectangle.x, y=rectangle.height*sin(1.57 - radians(rectangle.rotation))+rectangle.y, radius=1, color=(255,255,255))

circle2 = pyglet.shapes.Circle(x=(rectangle.height*cos(1.57 - radians(rectangle.rotation))+rectangle.x)+(rectangle.width*cos(radians(rectangle.rotation))), y=(rectangle.height*sin(1.57 - radians(rectangle.rotation))+rectangle.y) - (rectangle.width*sin(radians(rectangle.rotation))), radius=1, color=(255,0,255))


circle3 = pyglet.shapes.Circle(x=rectangle.x, y=rectangle.y, radius=1, color=(0,0,255))

circle4 = pyglet.shapes.Circle(x=rectangle.x + (rectangle.width * cos(radians(rectangle.rotation))), y= rectangle.y - (rectangle.width *sin(radians(rectangle.rotation))), radius=1, color=(255,255,0))