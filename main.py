import turtle

#ventana del programa
ventana = turtle.Screen()
ventana.title("Juego de ping pong-DRDG")
ventana.bgcolor("black")
ventana.setup(width = 800, height = 600)
ventana.tracer(0)

#Marcador
marcadorA = 0
marcadorB = 0


#Jugador A
jugadorA = turtle.Turtle() #esto crea un cuadrado
jugadorA.speed(0) #esto es para que aparezca al instante de haber iniciado la ventana
jugadorA.shape("square") #especifica la forma
jugadorA.color("white") # decimos el color del cuadrado
jugadorA.penup()
jugadorA.goto(-350,0) #le decimos las coordenadas de donde queremos que vaya
jugadorA.shapesize(stretch_wid = 5, stretch_len = 1) #esto le cambia las dimensiones del cuadrado

#Jugador B
jugadorB = turtle.Turtle() #esto crea un cuadrado
jugadorB.speed(0) #esto es para que aparezca al instante de haber iniciado la ventana
jugadorB.shape("square") #especifica la forma
jugadorB.color("white") # decimos el color del cuadrado
jugadorB.penup()
jugadorB.goto(350,0) #le decimos las coordenadas de donde queremos que vaya
jugadorB.shapesize(stretch_wid = 5, stretch_len = 1) #esto le cambia las dimensiones del cuadrado

#Pelota
pelota = turtle.Turtle() #esto crea un cuadrado
pelota.speed(0) #esto es para que aparezca al instante de haber iniciado la ventana
pelota.shape("circle") #especifica la forma
pelota.color("white") # decimos el color del cuadrado
pelota.penup()
pelota.goto(0,0) #le decimos las coordenadas de donde queremos que vaya

#esto es lo que le da velocidad a la pelota
pelota.dx = 1  #esto es para el cambio en x
pelota.dy = 1 #esto es para el cambio en y


#Linea division
division = turtle.Turtle()
division.color("white")
division.goto (0,400)
division.goto (0,-400)

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador A: 0         Jugador B: 0", align= "center", font=("Watermelon Days", 24, "normal" ))


#Funciones
def jugadorA_up():
    y = jugadorA.ycor() #esto crea una variable y despues guarda el valor de la coordenada y
    y += 20
    jugadorA.sety(y) #pasa el argumento

def jugadorA_down():
    y = jugadorA.ycor() #esto crea una variable y despues guarda el valor de la coordenada y
    y -= 20
    jugadorA.sety(y) #pasa el argumento

def jugadorB_up():
    y = jugadorB.ycor() #esto crea una variable y despues guarda el valor de la coordenada y
    y += 20
    jugadorB.sety(y) #pasa el argumento

def jugadorB_down():
    y = jugadorB.ycor() #esto crea una variable y despues guarda el valor de la coordenada y
    y -= 20
    jugadorB.sety(y) #pasa el argumento

def salir():
    ventana.bye()

#Teclado
ventana.listen() # para que la ventan detecte que algo se esta haciendo en la ventana
ventana.onkeypress(jugadorA_up, "w") # asocia que al presionar la tecla de w
ventana.onkeypress(jugadorA_down, "s") # asocia que al presionar la tecla de s
ventana.onkeypress(jugadorB_up, "Up") # asocia que al presionar la tecla de arriba
ventana.onkeypress(jugadorB_down, "Down") # asocia que al presionar la tecla de abajo
ventana.onkeypress(salir, "q") # asocia que al presionar la tecla de entyer


#bucle principal del juego
while True:
    ventana.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #Bordes
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

    #Bordes izquierda/derecha
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA += 1 # Aumenta el marcador del jugadorA
        pen.clear() # esto hace que se limpie el marcador
        pen.write("Jugador A: {}         Jugador B: {}".format(marcadorA,marcadorB), align = "center", font=("Watermelon Days", 24, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1 # Aumenta el marcador del jugadorB
        pen.clear() # esto hace que se limpie el marcador
        pen.write("Jugador A: {}         Jugador B: {}".format(marcadorA,marcadorB), align = "center", font=("Watermelon Days", 24, "normal"))

    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
            and (pelota.ycor() < jugadorB.ycor() +50
            and pelota.ycor() > jugadorB.ycor() -50)):

        pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and (pelota.ycor() < jugadorA.ycor() +50
            and pelota.ycor() > jugadorA.ycor() -50)):

        pelota.dx *= -1