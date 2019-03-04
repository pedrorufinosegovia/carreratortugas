class termometro():
    def __init__:(self):
        self.__unidadmedida = "C"
        self.__temperaura = 0
    
    def conversor(self, temperatura, unidad):
        if unidad.upper == "C":
           return "{} F".format(temperatura *9/5 + 32)
        elif unidad.upper == "F":
            return "{} C".format((temperatura -32)* 5/9)
        else:
            return "unidad incorrecta"
        
    def unidadmedia(self, uniM=None):
        if uniM == None:
            return self.__unidadmedida
        else:
            if uniM = "C" or uniM = "F":
                self.__unidadmedida = uniM
    
    def temp(self, temperatura = None):
        if temperatura == None
        