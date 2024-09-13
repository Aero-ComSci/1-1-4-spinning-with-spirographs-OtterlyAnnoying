#   a114_nested_loops_4.py 
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.goto(-200, 0)
painter.pendown()

while True:
  for i in range(2):
    x = -200
    y = 0
    move_x = 1
    move_y = 1*(-1)**i
    while (x < 1):
    
      while (y < (-100*i + 100)):
        x = x + move_x
        y = y + move_y
        painter.goto(x,y)
      move_y = -1
      
      while (y > -100*i):
        x = x + move_x
        y = y + move_y
        painter.goto(x,y)
      move_y = 1
  
      painter.penup()
      painter.goto(-200,i*-100)
      painter.pendown()
  wn = trtl.Screen()
  wn.mainloop()

#This code has some errors and doesn't properly do the mirrored pattern, any ideas on fixing it?
