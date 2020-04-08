from tkinter import*
import time
import random

class Ball():
      def __init__(self,canvas,paddle1,paddle2):   
         self.paddle1=paddle1
         self.paddle2=paddle2
         self.canvas=canvas
         self.id=canvas.create_oval(0,0,25,25,fill="yellow")
         self.horizontal_speed=random.randrange(1,6) 
         self.vertical_speed=random.randrange(1,6)
         self.canvas.move(self.id,245,100)
         self.canvas_height=self.canvas.winfo_height()
         self.canvas_width=self.canvas.winfo_width()
         self.hit_left=False
         self.hit_right=False
      def hit_paddle1(self,position):
          paddle1_position=self.canvas.coords(self.paddle1.id)
          if position[2]>=paddle1_position[0]and position[0]<= paddle1_position[2]:
            if position[3]>= paddle1_position[1]and position[3]<=paddle1_position[3]:
                return True
                return False
      
      def hit_paddle2(self,position):
          paddle2_position=self.canvas.coords(self.paddle2.id)
         
          if position[2]>=paddle2_position[0]and position[0]<=paddle2_position[2]:
             if position[3]>=paddle2_position[1]and position[3]<=paddle2_position[3]:
                return True
                return False
            
    
      

      def ball_moves(self):
  
          global Red_balls
           
              
          self.canvas.move(self.id,self.horizontal_speed,self.vertical_speed)
          position=self.canvas.coords(self.id)
         
         
          if self.hit_paddle2(position)==True:
             self.horizontal_speed=-self.horizontal_speed

          if position[2]>=self.canvas_width:
            
            
             self.horizontal_speed=-self.horizontal_speed
             global Red_balls
             

             Red_balls-=1
            
             Red_balls_label.config(text="Balls number:"+str( Red_balls),fg="red")
     
                
          if self.hit_paddle1(position)==True:
             self.horizontal_speed=-self.horizontal_speed
             
          if position[0]<=0:
             self.hit_left=True
             self.horizontal_speed=-self.horizontal_speed
             global Blue_balls
             Blue_balls-=1
             Blue_balls_label.config(text="Balls number:"+str(Blue_balls),fg="blue")
          
          if position[3]>= self.canvas_height:
             self.vertical_speed=-self.vertical_speed
          if position[1]<=0:
             self.vertical_speed=-self.vertical_speed
      
           



class Paddle:
 def __init__(self,canvas,color,x,y,move_up,move_down):
       
       
         
         self.canvas=canvas
         self.id=canvas.create_rectangle(0,0,10,100,fill=color)
      
         self.canvas.move(self.id,x,y,)
         self.vertical_speed=0
       
         self.canvas_hight=self.canvas.winfo_height()
      
         self.canvas.bind_all(move_up,self.moveing_up)
         self.canvas.bind_all(move_down,self.moveing_down)
        
         self.hit_left=False
        
 def draw_paddle(self):
       
        self.canvas.move(self.id,0,self.vertical_speed) 
        position=self.canvas.coords(self.id)
        if position[1]<=0:
           self.vertical_speed=0
        elif position[3]>=self.canvas_hight:
             self.vertical_speed=0

 def moveing_up(self,event):
        self.vertical_speed=-2

 def moveing_down(self,event):
        self.vertical_speed=2


window=Tk()
window.title("PONG")
window.resizable(0,0)
canvas=Canvas(window,width=450,height=400,bd=0,highlightthickness=0)
canvas.pack()

window.update()
Blue_balls=int
Blue_balls=3
Red_balls=int
Red_balls=3


Blue_balls_label=Label(window,text="Blue balls number:"+str(Blue_balls),fg="blue")
Blue_balls_label.pack(side=LEFT,anchor=W)
Red_balls_label=Label(window,text="Red balls Number:"+str(Red_balls),fg="red")
Red_balls_label.pack(side=RIGHT,anchor=E)

paddle1=Paddle(canvas,"blue",30,200,"<KeyPress-w>","<KeyPress-s>")
paddle2=Paddle(canvas,"red",370,100,"<KeyPress-Up>","<KeyPress-Down>")
ball=Ball(canvas,paddle1,paddle2)
window.wm_attributes("-topmost",1)

for i in range(100000):  
    paddle1.draw_paddle()
    paddle2.draw_paddle() 
    ball.ball_moves()  
    window.update_idletasks()
    window.update()
    time.sleep(0.01)   
