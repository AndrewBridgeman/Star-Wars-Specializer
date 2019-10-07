import pyglet

vid = "drop.avi"

window = pyglet.window.Window(fullscreen = False)
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()

MediaLoad = pyglet.media.load(vid)

player.queue(MediaLoad)

player.play()

@window.event
def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(0,0, width = 200, height = 200)

pyglet.app.run()
