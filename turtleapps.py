import turtle
import time

title = input('screen title: ')

while True:
	delayt = input('move delay: ')
	if delayt:
		delay = int(delayt)
		break
	print('requierd delay')
	time.sleep(5)


shape = input('witch shape: [cube/tringle/circle] ')

if shape == 'cube':
	t = turtle.Turtle()
	s = turtle.getscreen()
	ti = turtle.title(title)
	turtle.exitonclick()
	t.right(90)
	time.sleep(delay)
	t.forward(100)
	time.sleep(delay)
	t.left(90)
	time.sleep(delay)
	t.backward(100)
	time.sleep(delay)
	t.left(90)
	time.sleep(delay)
	t.forward(100)
	time.sleep(delay)
	t.right(90)
	time.sleep(delay)
	t.forward(100)
elif shape == 'tringle':
	t = turtle.Turtle()
	s = turtle.getscreen()
	ti = turtle.title(title)
	turtle.exitonclick()
	size = int(input('size:'))
	msize = size-size*2
	t.goto(msize, msize)
	t.goto(size, msize)
	t.goto(0, 0)
elif shape == 'circle':
	t = turtle.Turtle()
	s = turtle.getscreen()
	ti = turtle.title(title)
	turtle.exitonclick()
	t.color('black', 'white')
	t.shapesize(10)
	t.shape('circle')
else:
	pass



time.sleep(10)