import pyglet
from pyglet.window import key
import time

window = pyglet.window.Window(width=900, height=600, caption="timer")

going = False
start = 0
current= 0
elapsed = 0
swap = False

def stopwatch():
  global going
  global start
  global current
  global elapsed
  global swap
  current = time.time()
  if going == True:
    if swap == True:
      start = time.time()
  elif going == False:
    current = start
  elapsed = current - start
  swap = False
  return "{:#.2f}".format(elapsed)

@window.event
def on_draw():
  window.clear()
  label.draw()

@window.event
def on_key_press(symbol, modifiers):
  global swap
  global going
  if symbol == key.Q:
    swap = True
    if going == False:
      going = True
    else:
      going = False

def update(dt):
  global label
  label = pyglet.text.Label(str(stopwatch()), font_size=36, x=window.width//2, y=window.height//2)

pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()