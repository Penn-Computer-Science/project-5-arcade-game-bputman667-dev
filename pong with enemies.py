import tkinter as tk
import random

#PARAMETERS
WIDTH = 600
HEIGHT = 450

paddles = []
balls = []
score_texts = []
num_balls = 1
ball_dx = 0
ball_dy = 0
score_p1 = 0
score_p2 = 0
loop_id = None
computer = True

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
    ball = canvas.create_image(ballx, bally, image=ball_image, anchor = "nw")
    balls.append(ball)

def move_ball():
    global ball_dy, ball_dx
    global score_p1
    global score_p2
    for b in balls:
        canvas.move(b, ball_dx, ball_dy)
        bx1, by1, bx2, by2 = canvas.bbox(b)
        if by1 <= 0 or by2 >= HEIGHT:
            ball_dy = ball_dy * -1
        if bx1 <= 0:
            canvas.delete(b)
            balls.clear()
            set_up_balls()
            score_p2 += 1
            create_score_text()
        elif bx2 >= WIDTH:
            canvas.delete(b)
            balls.clear()
            set_up_balls()
            score_p1 += 1
            create_score_text()
def start(event=None):
    global score_p1
    global score_p2
    global ball_dx
    global ball_dy
    global loop_id
    if loop_id:
        root.after_cancel(loop_id)
    paddles = []
    balls = []
    score_texts = []
    num_balls = 1
    ball_dx = 0
    ball_dy = 0
    score_p1 = 0
    score_p2 = 0
    canvas.delete("all")
    set_up_paddles()
    set_up_balls()
    create_score_text()
    game_loop()


def game_loop():
    global loop_id
    paddle_collision()
    move_ball()
    paddle_stop()
    if computer:
        paddle_computer()
    loop_id = root.after(40, game_loop)

p1_down = 0
p1_up = 0
p2_down = 0
p2_up = 0
def stop1_up(event):
    global p1_up
    p1_up = 0

def stop1_down(event):
    global p1_down
    p1_down = 0

def stop2_up(event):
    global p2_up
    p2_up = 0

def stop2_down(event):
    global p2_down
    p2_down = 0

def move_up(event=None):
    global p1_up, p1_down, p2_up, p2_down
    canvas.move(paddles[0], 0, -8)
    p1_up = 1
    if p2_down == 1:
        canvas.move(paddles[1], 0, 8)
    elif p2_up == 1:
        canvas.move(paddles[1], 0, -8)


def move_down(event=None):
    global p1_up, p1_down, p2_up, p2_down
    canvas.move(paddles[0], 0, 8)
    p1_down = 1
    if p2_down == 1:
        print("a")
        canvas.move(paddles[1], 0, 8)
    elif p2_up == 1:
        print("a")
        canvas.move(paddles[1], 0, -8)

def p2_move_up(event=None):
    global p1_up, p1_down, p2_up, p2_down
    if computer == False:
        canvas.move(paddles[1], 0, -8)
        p2_up = 1
        if p1_down == 1:
            canvas.move(paddles[0], 0, 8)
        elif p1_up == 1:
            canvas.move(paddles[0], 0, -8)

def p2_move_down(event=None):
    global p1_up, p1_down, p2_up, p2_down
    if computer == False:
        canvas.move(paddles[1], 0, 8)
        p2_down = 1
        if p1_down == 1:
            canvas.move(paddles[0], 0, 8)
        elif p1_up == 1:
            canvas.move(paddles[0], 0, -8)

def start_computer(event):
    global computer
    computer = True
    start()

def start_multiplayer(event):
    global computer
    computer = False
    start()

root.bind("<Up>", move_up)
root.bind("<KeyRelease-Up>", stop1_up)
root.bind("<Down>", move_down)
root.bind("<KeyRelease-Down>", stop1_down)
root.bind("r", start)
root.bind("m", start_multiplayer)
root.bind("c", start_computer)
root.bind("w", p2_move_up)
root.bind("<KeyRelease-w>", stop2_up)
root.bind("s", p2_move_down)
root.bind("<KeyRelease-s>", stop2_down)

def paddle_collision():
    global ball_dx
    bx1, by1, bx2, by2 = canvas.bbox(balls[0])
    p1x1, p1y1, p1x2, p1y2 = canvas.bbox(paddles[0])
    p2x1, p2y1, p2x2, p2y2 = canvas.bbox(paddles[1])
    if (bx1 < p1x2 or bx2 < p1x1) and by1 < p1y2+10 and by2 > p1y1-10:
        ball_dx = ball_dx*-1
        for ball in balls[:]:
            canvas.move(ball, 5, 0)
    if bx1 > p2x1 and bx2 > p2x2 and by1 < p2y2+10 and by2 > p2y1-10:
        ball_dx = ball_dx*-1
        for ball in balls[:]:
            canvas.move(ball, -5, 0)

def paddle_stop():
    global paddles
    for paddle in paddles[:]:
        px1, py1, px2, py2 = canvas.bbox(paddle)
        if py1 < 0:
            canvas.move(paddle, 0, 16)
        if py2 > HEIGHT:
            canvas.move(paddle, 0, -16)

def create_score_text():
    for t in score_texts[:]:
        canvas.delete(t)
        score_texts.remove(t)
    p1_score_text = canvas.create_text(40, 40, text = str(score_p1), fill="white")
    score_texts.append(p1_score_text)
    p2_score_text = canvas.create_text(WIDTH-40, 40, text = str(score_p2), fill="white")
    score_texts.append(p2_score_text)

def paddle_computer():
    bx1, by1, bx2, by2 = canvas.bbox(balls[0])
    px1, py1, px2, py2 = canvas.bbox(paddles[1])
    if py1+5 > by1:
        canvas.move(paddles[1], 0, -3)
    if py2-5 < by2:
        canvas.move(paddles[1], 0, 3)

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
canvas.pack()

start()
root.mainloop()
