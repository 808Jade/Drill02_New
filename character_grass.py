from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

while True:
    while (x < 750):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    while (y < 550):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 2
        delay(0.01)

    while (x > 50):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 2
        delay(0.01)

    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 2
        delay(0.01)

    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    angle = -90
    radius = 200

    while angle <= 280:
        clear_canvas_now()
        grass.draw_now(400, 30)

        x = 400 + radius * math.cos(math.radians(angle))
        y = 290 + radius * math.sin(math.radians(angle))

        character.draw_now(x, y)
        angle += 1
        delay(0.01)      


close_canvas()
