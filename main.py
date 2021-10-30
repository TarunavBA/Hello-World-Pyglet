import pyglet

# create the window
window = pyglet.window.Window()

# Create the label for Hello World text, and center it
label = pyglet.text.Label('Hello, World',
    font_name='Menlo',
    font_size=36,
    x=window.width//2, y=window.height//2,
    anchor_x='center', anchor_y='center'
)

# An on_draw() event is dispatched to the window to give it a chance to redraw its contents. pyglet provides several ways to attach event handlers to objects; a simple way is to use a decorator:
@window.event
def on_draw():
    window.clear()
    label.draw()

# finally call,
pyglet.app.run()
# TODO:improve the program