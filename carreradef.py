import turtle
import random 
class Circuito():
    corredores = []
    __posStrartY = [-30, -10, 10, 30]
    __colorturtle = ("green", "red", "black", "blue")
    def __init__(self, width, heigth):
        self.__Screen = turtle.Screen()
        self.__Screen.setup(width, heigth)
        self.__Screen.bgcolor("yellow")
        self.__startline = -width/2 + 20
        self.__finishline = width/2 -20
        self.__createrunners()
    def __createrunners(self):   
        for i in range(4):
            newturtle = turtle.Turtle()
            newturtle.shape("turtle")
            newturtle.color(self.__colorturtle[i])
            newturtle.penup()
            newturtle.setpos(self.__startline, self.__posStrartY[i])
            self.corredores.append(newturtle)
            
    def competir(self):
        hayganador = False
        velocidades = (10, 15, 20, 25, 30, 35)
        while not hayganador:
            for tortuga in self.corredores:
                avance = velocidades[random.randint(0,5)]
                tortuga.fd(avance)
                if tortuga.position()[0] >= self.__finishline:
                    hayganador = True
                    print("la tortuga de color {} ha ganado".format(tortuga.color()[0]))
                    break
            
            
if __name__ == "__main__":
    circuito = Circuito(1000, 480)
    circuito.competir()

