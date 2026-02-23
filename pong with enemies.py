import tkinter as tk
import random

#PARAMETERS
WIDTH = 600
HEIGHT = 450

paddles = []
balls = []
num_balls = 1
ball_dx = 0
ball_dy = 0
score_p1 = 0
score_p2 = 0

def make_paddle_sprite():
    pattern = [
        "0011211100",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "1111211111",
        "1111121111",
        "0011211100"
    ]
    h = len(pattern)
    w = len(pattern[0])

    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("red",(x,y))
            elif pattern[y][x] == "2":
                img.put("blue",(x,y))
    return img


def make_ball_sprite():
    pattern = [
        "01111110",
        "11111111",
        "11111111",
        "11111111",
        "11111111",
        "11111111",
        "11111111",
        "01111110"
    ]
    h = len(pattern)
    w = len(pattern[0])

    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("green",(x,y))
    return img

root = tk.Tk()
root.title("ULTRA-PONG")

paddle_image = make_paddle_sprite()
ball_image = make_ball_sprite()

def set_up_paddles():
    paddles.clear()
    paddle_px = 20
    paddle_py = HEIGHT//2
    paddle_ex = WIDTH-30
    paddle_ey = HEIGHT//2
    player_paddle = canvas.create_image(paddle_px, paddle_py, image=paddle_image, anchor = "nw")
    paddles.append(player_paddle)
    enemy_paddle = canvas.create_image(paddle_ex, paddle_ey, image=paddle_image, anchor = "nw")
    paddles.append(enemy_paddle)

def set_up_balls():
    global ball_dx
    global ball_dy
    balls.clear()
    ballx = WIDTH//2
    bally = HEIGHT//2
    ball_selector = random.randint(1, 4)
    if ball_selector == 1:
        ball_dx = 5
        ball_dy = 5
    elif ball_selector == 2:
        ball_dx = 5
        ball_dy = -5
    elif ball_selector == 3:
        ball_dx = -5
        ball_dy = 5
    else:
        ball_dx = -5
        ball_dy = -5
    ball = canvas.create_image(ballx, bally, image=ball_image, anchor = "center")
    balls.append(ball)

def move_ball():
    global ball_dy
    for b in balls[:]:
        canvas.move(b, ball_dx, ball_dy)
        bx1, by1, bx2, by2 = canvas.bbox(b)
        if by1 <= 0 or by2 >= HEIGHT:
            ball_dy = ball_dy * -1
        if bx1 <= 0 or bx2 >= WIDTH:
            canvas.delete(b)
            balls.clear()
            set_up_balls()
def start():
    set_up_paddles()
    set_up_balls()
    game_loop()

def game_loop():
    paddle_collision()
    move_ball()
    root.after(40, game_loop)

def move_up(event):
    canvas.move(paddles[0], 0, -8)

def move_down(event):
    canvas.move(paddles[0], 0, 8)

root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

def paddle_collision():
    global ball_dx
    bx1, by1, bx2, by2 = canvas.bbox(balls[0])
    p1x1, p1y1, p1x2, p1y2 = canvas.bbox(paddles[0])
    p2x1, p2y1, p2x2, p2y2 = canvas.bbox(paddles[1])
    if bx1 < p1x2 and bx2 < p1x1 and by1 < p1y2+10 and by2 > p1y1-10:
        ball_dx = ball_dx*-1
        print("test")
    if bx1 > p2x1 and bx2 > p2x2 and by1 < p2y2+10 and by2 > p2y1-10:
        ball_dx = ball_dx*-1



canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
canvas.pack()

start()
root.mainloop()
