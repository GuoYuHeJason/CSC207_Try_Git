from tkinter import*
import random
import time

#game start, 1 = before, 2 = start, 3 = lose, 4 = win
game_state = 1
time_start = 2688192572.480042
ball_list = []
ball_number = 0
moving_ball_number = 0
def gstart():
    global game_state
    global time_start
    game_state = 2
    print(game_state)
    print('game start')
    time_start = time.time()
    #print(time_start)
    btn_game_start.pack_forget()
    canvas.delete(tut_text)
   
#game window
tk = Tk()
tk.title("Game")
tk.resizable(0,0)
#tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=1000,height=600,bd=0,highlightthickness=0)
canvas.pack()
btn_game_start = Button(tk, text = 'start game', command=gstart)
btn_game_start.pack()
tk.update

#player, id =1 , blue
class Player:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,10,10,fill=color)
        #print(self.id)
        self.canvas.move(self.id,490,490)
#global
player = Player(canvas, 'blue')
player_pos = canvas.coords(1)
print(player_pos)

#moveplayers
def moveplayer(event):
    global game_state
    global player_pos
    if event.keysym == 'w' and game_state == 2 and player_pos[1] > 50:
        canvas.move(1,0,-20)
    if event.keysym == 's' and game_state == 2 and player_pos[3] < 550:
        canvas.move(1,0,20)
    if event.keysym == 'a' and game_state == 2 and player_pos[0] > 50:
        canvas.move(1,-20,0)
    if event.keysym == 'd' and game_state == 2 and player_pos[2] < 950:
        canvas.move(1,20,0)
canvas.bind_all('<KeyPress-w>',moveplayer)
canvas.bind_all('<KeyPress-s>',moveplayer)
canvas.bind_all('<KeyPress-a>',moveplayer)
canvas.bind_all('<KeyPress-d>',moveplayer)


#ball
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(0,0,20,20,fill=color)
        self.canvas.move(self.id,(self.id-3)*10,0)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = starts[1]
        self.canvas_height = self.canvas.winfo_height()
        self.moving = 0
    def draw(self):
        self.moving = 1
        global game_state
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        bounce1 = [1,2,3]
        bounce2 = [-3,-2,-1]
        #print(pos)
        #print(pos[1])
        #print(pos[3])
        if pos[1] <= 0:
            random.shuffle(bounce1)
            self.y = bounce1[0]
        if pos[3] >= 600:
            random.shuffle(bounce2)
            self.y = bounce2[0]
        if pos[0] <= 0:
            random.shuffle(bounce1)
            self.x = bounce1[0]
        if pos[2] >= 1000:
            random.shuffle(bounce2)
            self.x = bounce2[0]
        if pos[2] >= player_pos[0] and pos[0] <= player_pos[2]:
            if (pos[3] >= player_pos[1] and pos[3] <= player_pos[3]) or (pos[1] <= player_pos[3] and pos[1] >= player_pos[1]):
                game_state = 3
                #print(game_state)
               
#create ball
for x in range (1,101):
    ball = Ball(canvas,'red')
    ball_list.append(ball)
    #print(ball_list)
    ball_number = ball_number +1

#tutorial
tut_text = canvas.create_text(500,300,text='wasd')

#mainloop
while 1:
    moving_ball_number = 0
    time_now = time.time()
    #print(time_now)
    player_pos = canvas.coords(1)
    if game_state ==2:
        ball_list[0].draw()
    #actual mainloop
    for x in range (1,100):
        if time_now-time_start >= x*5:
            ball_list[x].draw()
        if ball_list[99].moving == 1:
            game_state = 4
        if game_state ==3:
            canvas.create_text(500,300,text='YOU LOSE')
            #print('YOU LOSE')
            print(game_state)
            break
        if game_state ==4:
            canvas.create_text(500,300,text='YOU WIN')
            #print('YOU WIN')
            print(game_state)
            break
    for x in range (1,100):
        moving_ball_number = moving_ball_number+ball_list[x].moving
    if game_state ==3:
        canvas.create_text(500,300,text='YOU LOSE')
        canvas.create_text(500,350,text='score: %s' % (moving_ball_number + 1))
        print('YOU LOSE')
        print('score: %s' % (moving_ball_number + 1))
        #print(game_state)
        break
    if game_state ==4:
        canvas.create_text(500,300,text='YOU WIN')
        canvas.create_text(500,350,text='score: %s' % (moving_ball_number + 1))
        print('YOU WIN')
        print('score: %s' % (moving_ball_number + 1))
        #print(game_state)
        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)