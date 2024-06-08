import pyglet
from pyglet.window import mouse

window1 = pyglet.window.Window(width=400, height=300, caption='Window 1')
window2 = pyglet.window.Window(width=400, height=300, caption='Window 2')

window1.set_fullscreen(False)
window2.set_fullscreen(False)
#maybe for my actual game it would be good to have another screen as a backdrop since when I did this there is slight time delay where you can see the code.

@window1.event
def on_draw():
  window1.clear()

@window1.event
def on_mouse_press(x, y, button, modifiers):
  if button == mouse.LEFT:
    window1.set_visible(False)
    window2.set_visible(True)

@window2.event
def on_draw():
  window2.clear()

@window2.event
def on_mouse_press(x, y, button, modifiers):
  if button == mouse.LEFT:
    window2.set_visible(False)
    window1.set_visible(True)

window2.set_visible(True)  # Start with the second window hidden

pyglet.app.run()