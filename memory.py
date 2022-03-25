"""Memory, puzzle game of number pairs.

authors:
Paulo Ogando Gulias                  A01751587
Christian Parrish Gutiérrez Arrieta  A01751584
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')

#Arrange of duplicated cards, we used emojies to make it easier for the player
#to find pairs
tiles = ['🍏', '🍐', '🍊', '🍋', '🍌', '🍉', '🍇', '🍓',
        '🍒', '🍑', '🍍', '🥥', '🥝', '🍅', '🥑', '🍆',
        '🌶', '🥒', '🥬', '🥦', '🌽', '🥕', '🥔', '🥐',
        '🥨', '🧀', '🥩', '🍙', '🍕', '🍩', '🍪', '🍦'
        ] * 2
state = {'mark': None}
hide = [True] * 64
#Variable saving the number of clicks/taps
taps = 0
#Turtle variable used to draw text
writer = Turtle(visible = False)


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'indigo')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global mark, taps
    # Increases the number of taps
    taps = taps + 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

# Function that shows the image for the end of the game
def win():
    clear()
    goto(0, 0)
    shape(car)
    stamp()


def draw():
    """Draw image and tiles."""
    global mark
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)


    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 6, y + 6) # Defines the position of the image on the card
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    hidden = hide.count(True) # Variable counts the number of cards missing to find
    found = 64 - hidden     # Variable with the cards found
    print("CARDS FOUND ", found) # Shows the pairs found

    # Shows the messages when you finish the game
    if hidden == 0:
        win()
        up()
        goto(-100, 80)
        color('white')
        write('NAILED IT!', font=('Times New Roman', 30, 'normal'))
        goto(-140, -150)
        color('white')
        write(f'YOU MADE {taps} CLICS', font=('Arial', 20, 'normal'))
        return

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
