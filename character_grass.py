from pico2d import *
import math

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

def render_frame(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)

clear_canvas_now()
grass.draw_now(400,30)
character.draw_now(400,90)
delay(1)

def run_circle():
    print('CIRCLE')
    cx, cy, r = 400, 300, 200

    for deg in range(0, 360, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        render_frame(x,y)

def run_rectangle():
    print('RECTANGLE')
    for x in range(50,750+1,5):
        render_frame(x,90) # xy위치에 캐릭터 그려주는 함수

    for x in range(750,50-1,-5):
        render_fframe(x,550)


while True:
    run_circle()
    run_rectangle()
