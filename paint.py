#VRDL: Se importó librería Turtle para construcción de gráficos
import turtle
from turtle import *
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


def circulo(start, end):
    """Draw circle from start to end."""
    #ARCR:Función para construír un circulo relleno por un color específico 
    up() 
    goto(start.x,start.y)
    down()
    begin_fill()
    r = 50
    circle(r)
    end_fill()
    
# VRDL: Función para construír un rectángulo relleno por un color específico
def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # VRDL: Se realiza un count in range para dibujar los 4 lados:
    for count in range(4):
        if count %2 == 0:
            forward((end.x + start.x) + 10)
            left(90)
        else:
            forward((end.x -start.x)- 10)
            left(90)
    end_fill() 

# VRDL: Función para construír un triángulo relleno por un color específico
def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    forward(end.x- start.y)
    # VRDL: Nota. Esta instrucción significa girar a la izquierda 120 grados 
    # antes de dibujar el siguiente lado
    left(120)
    forward(end.x- start.y)
    left(120)
    forward(end.x- start.y)
    end_fill()


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
onkey(lambda: color('purple'),'P') #ARCR: Se añadió color morado
onkey(lambda: color('pink'),'Q') #ARCR: Se añadió color rosa  
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()