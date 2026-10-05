import turtle as t
print ()
t.ht
r = 40
t.pensize(10)
t.colormode(255)
t.color (255, 165, 0)
t.fillcolor (162, 0, 255)
for r in range(40,0, -10):
    for i in range(6):
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.rt(60)
    r = r - 1
