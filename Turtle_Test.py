import turtle

#t = turtle.Pen()
#t.reset()
#t.forward(100)
#t.right(90)
#t.forward(100)
#t.right(90)
#t.forward(100)
#t.right(90)
#t.forward(100)
#t.hideturtle()

turtle.Pen()
turtle.forward(100)

class MyTurtle(turtle):
    def glow(self,x,y):
        self.fillcolor("red")
    def unglow(self,x,y):
        self.fillcolor("")


turtle = MyTurtle()
turtle.onclick(turtle.glow)
turtle.onrelease(turtle.unglow)
