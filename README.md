# Videojuegos
Videojuegos creados por Paulo Ogando y Christian Parrish



`Paint, for drawing shapes.   
authors: Paulo Ogando Gulias                  A01751587 
         Christian Parrish Gutiérrez Arrieta  A01751584`

 \
**Modules**

`      `
  -------------------- ----------------- ----------------- -----------------
  [math](math.html)\                                       
  -------------------- ----------------- ----------------- -----------------
 \
**Functions**

`      `
[**circ**]{#-circ}(start, end)
:   `Draw circle from start to end.`

```{=html}
<!-- -->
```

[**line**]{#-line}(start, end)
:   `Draw line from start to end.`

```{=html}
<!-- -->
```

[**rectangle**]{#-rectangle}(start, end)
:   `Draw rectangle from start to end.`

```{=html}
<!-- -->
```

[**square**]{#-square}(start, end)
:   `Draw square from start to end.`

```{=html}
<!-- -->
```

[**store**]{#-store}(key, value)
:   `Store value in state at key.`

```{=html}
<!-- -->
```

[**tap**]{#-tap}(x, y)
:   `Store starting point or draw shape.`

```{=html}
<!-- -->
```

[**triangle**]{#-triangle}(start, end)
:   `Draw triangle from start to end.`

 \
**Data**

`      `
**state** = {\'shape\': \<function line\>, \'start\': vector(18.0,
170.0)}



`Snake, classic arcade game.   
authors: Paulo Ogando Gulias                  A01751587 
         Christian Parrish Gutiérrez Arrieta  A01751584`

 \
**Functions**
`      `
[**change**]{#-change}(x, y)
:   `Change snake direction.`

```{=html}
<!-- -->
```

[**inside**]{#-inside}(head)
:   `Return True if head inside boundaries.`

```{=html}
<!-- -->
```

[**move**]{#-move}()
:   `Move snake forward one segment.`

```{=html}
<!-- -->
```

[**move\_food**]{#-move_food}()
:   `#Funcion para mover la comida aleatoriamente en los bordes`

 \
**Data**

`      `
**aim** = vector(10, 0)\
**colors** = \[\'black\', \'indigo\', \'gold\', \'slategrey\'\]\
**food** = vector(10, -10)\
**fruit\_color** = \'gold\'\
**rand** = 2\
**snake** = \[vector(100, 30), vector(110, 30)\]\
**snake\_color** = \'green\'



`Pacman, classic arcade game.   
authors: Paulo Ogando Gulias                  A01751587
         Christian Parrish Gutiérrez Arrieta  A01751584`

 \
**Functions**
`      `
[**change**]{#-change}(x, y)
:   `Change pacman aim if valid.`

```{=html}
<!-- -->
```

[**move**]{#-move}()
:   `Move pacman and all ghosts.`

```{=html}
<!-- -->
```

[**offset**]{#-offset}(point)
:   `Return offset of point in tiles.`

```{=html}
<!-- -->
```

[**square**]{#-square}(x, y)
:   `Draw square using path at (x, y).`

```{=html}
<!-- -->
```

[**valid**]{#-valid}(point)
:   `Return True if point is valid in tiles.`

```{=html}
<!-- -->
```

[**world**]{#-world}()
:   `Draw world using path.`

 \
**Data**

`      `
**aim** = vector(5, 0)\
**ghosts** = \[\[vector(20, 95), vector(0, -5)\], \[vector(20, -95),
vector(0, 5)\], \[vector(20, 0), vector(0, -5)\], \[vector(60, -75),
vector(5, 0)\]\]\
**pacman** = vector(20, -80)\
**path** = \<turtle.Turtle object\>\
**state** = {\'score\': 4}\
**tiles** = \[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, \...\]\
**writer** = \<turtle.Turtle object\>



`Cannon, hitting targets with projectiles.   
authors: Paulo Ogando Gulias                  A01751587 
          Christian Parrish Gutiérrez Arrieta  A01751584`
 \
**Functions**

`      `
[**draw**]{#-draw}()
:   `Draw ball and targets.`

```{=html}
<!-- -->
```
[**inside**]{#-inside}(xy)
:   `Return True if xy within screen.`

```{=html}
<!-- -->
```

[**move**]{#-move}()
:   `Move ball and targets.`

```{=html}
<!-- -->
```

[**tap**]{#-tap}(x, y)
:   `Respond to screen tap.`

 \
**Data**

`      `
**ball** = vector(-200, -200)\
**speed** = vector(8, 8)\
**targets** = \[vector(171.5, 49), vector(194.5, 134)\]



`Memory, puzzle game of number pairs.   
authors: Paulo Ogando Gulias                  A01751587 
          Christian Parrish Gutiérrez Arrieta  A01751584`

 \
**Functions**

`      `
[**draw**]{#-draw}()
:   `Draw image and tiles.`

```{=html}
<!-- -->
```

[**getrandbits**]{#-getrandbits}(k, /) method of [random.Random](random.html#Random) instance
:   `getrandbits(k) -> x.  Generates an int with k random bits.`

```{=html}
<!-- -->
```

[**index**]{#-index}(x, y)
:   `Convert (x, y) coordinates to tiles index.`

```{=html}
<!-- -->
```

[**random**]{#-random}() method of [random.Random](random.html#Random) instance
:   `random() -> x in the interval [0, 1).`

```{=html}
<!-- -->
```

[**square**]{#-square}(x, y)
:   `Draw white square with black outline at (x, y).`

```{=html}
<!-- -->
```

[**tap**]{#-tap}(x, y)
:   `Update mark and hidden tiles based on tap.`

```{=html}
<!-- -->
```

[**win**]{#-win}()
:   `# Function that shows the image for the end of the game`

```{=html}
<!-- -->
```

[**xy**]{#-xy}(count)
:   `Convert tiles count to (x, y) coordinates.`

 \
**Data**

`      `
**car** = r\'C:\\Python310\\Lib\\site-packages\\freegames\\car.gif\'\
**hide** = \[True, True, True, True, True, True, True, True, True, True,
True, True, True, True, True, True, True, True, True, True, \...\]\
**mark** = None\
**state** = {\'mark\': None}\
**taps** = 0\
**tiles** = \[\'🥑\', \'🥝\', \'🍒\', \'🥑\', \'🍇\', \'🥒\', \'🍕\', \'🍉\',
\'🍊\', \'🍋\', \'🍑\', \'🥐\', \'🍪\', \'🌽\', \'🥩\', \'🌶\', \'🍏\', \'🍋\',
\'🍦\', \'🥩\', \...\]\
**writer** = \<turtle.Turtle object\>
