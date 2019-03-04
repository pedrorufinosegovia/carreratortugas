import turtle

class Circuito():
    corredores = []
    __posStrartY = [-30, -10, 10, 30]
    __colorturtle = ("green", "orange", "black", "blue")
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
            

if __name__ == "__main__":
    circuito = Circuito(640, 480)

