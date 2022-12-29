# import colorgram
import random as r
import turtle as t
# rgb_colors = []
# colors = colorgram.extract('hirst-1.jpeg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tup = (r, g, b)
#     rgb_colors.append(tup)
#
# print(rgb_colors)
t.colormode(255)
color_list = [(198, 159, 116), (70, 92, 129),
              (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46),
              (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42),
              (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85),
              (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

tim = t.Turtle()
# tim.shape("circle")
tim.penup()
init_x = -250
init_y = -250
curr_x = init_x
curr_y = init_y
for _ in range(10):
    tim.setpos(curr_x, curr_y)
    for _ in range(10):
        # tim.color(r.choice(color_list))
        # tim.stamp()
        tim.dot(20, r.choice(color_list))
        tim.forward(50)
    curr_y += 50
tim.hideturtle()

screen = t.Screen()
screen.exitonclick()