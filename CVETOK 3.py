import turtle as t

r = 40

t.pensize(10)
t.color(255. 165. 0)
t.fillcolor(162. 0. 255)
for j in range(4):
    for i in range (6):
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.rt(60)
    r = r - 10