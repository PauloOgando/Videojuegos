"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
import math
from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circ(start, end):
    """Draw circle from start to end."""
    #Variable que calcula el radio del circulo a partir de los puntos en x y y
    rad = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)

    #Variable que guarda el centro del circulo
    center = start.y - rad

    up()
    goto(start.x, center)
    down()
    begin_fill()

    #Funcion de turtle para dibujar un circulo
    circle(rad)

    end_fill()

def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO


def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')  #Aplica el color amarillo a la figura que se realice
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circ), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
