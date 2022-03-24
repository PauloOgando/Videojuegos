"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#Variable que guarda los colores en un vector
colors = ['black', 'green', 'indigo', 'gold', 'slategrey']
#Elige un elemento del vector aleatoriamente
rand = randrange(0, 4)
#Asigana el color aleatorio a la variable de color de la serpiente
snake_color = colors[rand]
#Asegura que los colores de la serpiente y la fruta no sean los mismos
colors.pop(rand)
#Elige un elemento del vector aleatoriamente, sin contar el ya usado para el color de la serpiente
rand = randrange(0, 3)
#Asigana el color aleatorio a la variable de color para comida
fruit_color = colors[rand]



def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

#Funcion para mover la comida aleatoriamente
def move_food():

    #Variable que determina el movimiento de la comida evitando que se salga de los bordes
    rand_move = randrange(0, 4)

#Decisiones de movimiento basadas en la variable rand_move y la posicion de la
#comida

    if rand_move == 0:
        if food.x == 190:
            food.x -= 10
        else:
            food.x += 10
    elif rand_move == 1:
        if food.x == -180:
            food.x += 10
        else:
            food.x -= 10
    elif rand_move == 2:
        if food.y == 190:
            food.y -= 10
        else:
            food.y += 10
    elif rand_move == 3:
        if food.y == -180:
            food.y += 10
        else:
            food.y -= 10

    ontimer(move_food, 1000)  #Temporizador qe determina cada cuanto tiempo se
                              # mueve la comida con la funcion.

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9,  'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, fruit_color)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
move_food() #Llamado a la funcion de para mover la comida
done()
