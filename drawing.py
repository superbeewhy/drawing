import turtle

def draw_star(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)  
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)  
    turtle.end_fill()

def draw_chinese_flag():
    turtle.speed(0)
    turtle.bgcolor("red")  
    turtle.hideturtle()  

    draw_star(-200, 100, 70)

    small_star_positions = [(-150, 50), (-120, 75), (-120, 110),(-150, 150)]
    for pos in small_star_positions:
        draw_star(pos[0], pos[1], 20)

    turtle.done() 

draw_chinese_flag()
