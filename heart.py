import turtle

t = turtle.Turtle()
turtle.title("Heart")

screen = turtle.Screen()
screen.bgcolor("black")

# Rysowanie serca
t.color("red")
t.fillcolor("red")
t.begin_fill()

t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)

t.end_fill()

# pisanie tekstu
t.up()
t.setpos(-80,150)
t.down()
t.color("lightgreen")
t.write("I love you!", font=("Verdana", 20, "bold"))

t.ht()

turtle.mainloop()