import pyglet
from pyglet import sprite, image
from pyglet.window import mouse

def entryScreen():
  #entry screen
  entryWindow = pyglet.window.Window(caption="Artificial Drift")
  entryWindow.set_fullscreen(True)

  entryDisplay = pyglet.graphics.Batch()

  #entry images
  logo_img = image.load("images/logo_finished.png")
  logo_img.anchor_x = logo_img.width//2
  logo_img.anchor_y = logo_img.height//2
  logo = sprite.Sprite(logo_img, x=entryWindow.width//2, y=entryWindow.height//2 +100, batch=entryDisplay)

  play_img = image.load("images/text_play.png")
  play_img.anchor_x = play_img.width//2
  play_img.anchor_y = play_img.height//2
  playButton = sprite.Sprite(play_img, x=entryWindow.width//2, y=entryWindow.height//2 -200, batch=entryDisplay)
  playButton.scale = 0.5

  triangle_img = image.load("images/triangle1_translucent.png")
  triangle_img.anchor_x = triangle_img.width//2
  triangle_img.anchor_y = triangle_img.height//2
  triangle1 = sprite.Sprite(triangle_img, x=100, y=100, batch=entryDisplay)
  triangle1.rotation = 30
  triangle1.scale = 0.3

  @entryWindow.event
  def on_draw():
    entryWindow.clear()
    entryDisplay.draw()


  @entryWindow.event
  def on_mouse_press(x,y,button,modifiers):
    if button == mouse.LEFT:
      entryWindow.close()

  pyglet.app.run()

entryScreen()