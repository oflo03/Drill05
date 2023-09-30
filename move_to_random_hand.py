from pico2d import *
import random
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')
run = [load_image('marin_run_back_right.png'), load_image('marin_run_back.png'),
       load_image('marin_run_back_left.png'), load_image('marin_run_front_left.png'),
       load_image('marin_run_front.png'), load_image('marin_run_front_right.png')]


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hand_x, hand_y = random.randrange(0, TUK_WIDTH), random.randrange(0, TUK_HEIGHT)
frame = 0
face = 1

while running:
    clear_canvas()
    ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(hand_x, hand_y)
    run[face].clip_draw(frame * run[face].w // 6, 0, run[face].w // 6, run[face].h, x, y,
                        run[face].w // 6 * 4, run[face].h * 4)
    print(face)
    update_canvas()
    handle_events()
    x += (hand_x - x) * 0.1
    y += (hand_y - y) * 0.1
    if abs(hand_x - x) < (run[face].w + hand.w) // 2 and abs(hand_y - y) < (run[face].h + hand.h) // 2:
        hand_x, hand_y = random.randrange(0, TUK_WIDTH), random.randrange(0, TUK_HEIGHT)
    face = int(math.acos((hand_x - x) / math.sqrt(math.pow(hand_x - x, 2) + math.pow(hand_y - y, 2))) * 3 / math.pi)
    if hand_y < y:
        face = face * -1 + 5
    frame = (frame + 1) % 6
    delay(0.08)

close_canvas()
