import turtle

mihir_turtle = turtle.Turtle()
# Square Shape


def square():
    mihir_turtle.fd(100)
    mihir_turtle.lt(120)
    mihir_turtle.fd(100)
    mihir_turtle.rt(60)
    mihir_turtle.bk(100)
    # mihir_turtle.lt(90)
    # mihir_turtle.fd(100)


# square()
# mihir_turtle.forward(150)
# square()

elephant = 1300
ant = 1200

if elephant > ant:
    square()
else:
    mihir_turtle.fd(200)

mihir = 'hello'
while mihir == 'hello':
    print('hey')
    break

for i in range(6):
    square()
