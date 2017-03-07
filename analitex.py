#-*-encoding:utf8-*-

class Analizador_Texto:

    def __init__(self):
        self.letra_actual = ''
        self.estado_actual = 0
        self.valor_lexema = ''
        self.operadores = ['+','-','E','.']
        self.punt = [',',':',';']
        self.aceptacion = True
        self.reserv = ['Teorema', 'teorema', 'Matematico', 'Matematica', 'matematico', 'matematica',
        'Hilbert', 'Turing', 'analisis', 'Analisis', 'Euler', 'Fermat', 'Pitagoras', 'automata', 'Boole', 'Cantor',
        'Experimentacion', 'experimentacion', 'Fisico', 'Fisica', 'fisico', 'fisica', 'Astronomia', 'astronomia',
        'mecanica', 'Mecanica', 'Newton', 'Einstein', 'Galileo', 'modelo', 'Modelo', 'Tesla', 'Dinamica', 'dinamica']

    def switch(self, estado):
        self.estados = {
        0: self.estado_cero,
        1: self.estado_uno,
        2: self.estado_dos,
        3: self.estado_tres,
        4: self.estado_cuatro,
        5: self.estado_cinco,
        6: self.estado_seis,
        7: self.estado_siete,
        8: self.estado_ocho,
        9: self.estado_nueve,
        10: self.estado_diez,
        11: self.estado_once,
        }
        func = self.estados.get(estado, lambda: 'No es un caracter válido')
        return func()

    def valuar_dato(self, dato):
        try:
            int(dato)
            return True
        except ValueError:
            return False

    def estado_cero(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[0] or str(self.letra_actual) == self.operadores[1]:
                self.estado_actual = 1
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            if int(self.letra_actual) > 0:
                self.estado_actual = 3
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif int(self.letra_actual) == 0:
                self.estado_actual = 4
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'Cadena no aceptada'

    def estado_uno(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) > 0:
                self.estado_actual = 3
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif int(self.letra_actual) == 0:
                self.estado_actual = 2
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'Cadena no aceptada'
        else:
            self.estado_actual = 10
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def estado_dos(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[3]:
                self.estado_actual = 5
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.aceptacion = False
            print 'Cadena no aceptada'

    def estado_tres(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[2]:
                self.estado_actual = 6
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == self.operadores[3]:
                self.estado_actual = 5
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == ' ':
                print 'Esto es un numero entero ', self.valor_lexema
                self.aceptacion = False
            elif str(self.letra_actual) in self.punt:
                print 'Esto es un numero entero ', self.valor_lexema
                self.aceptacion = False
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 3
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True

    def estado_cuatro(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[3]:
                self.estado_actual = 5
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == ' ':
                print 'Esto es un numero entero ', self.valor_lexema
                self.aceptacion = False
            elif str(self.letra_actual) in self.punt:
                print 'Esto es un numero entero ', self.valor_lexema
                self.aceptacion = False
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.aceptacion = False
            print 'Cadena no aceptada'

    def estado_cinco(self):
        if self.valuar_dato(self.letra_actual) == False:
            self.estado_actual = 10
            self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 11
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def estado_seis(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[0] or str(self.letra_actual) == self.operadores[1]:
                self.estado_actual = 7
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) in self.punt:
                print 'Esto es una cadena ', self.valor_lexema
                self.aceptacion = False
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            if int(self.letra_actual) > 0:
                self.estado_actual = 8
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif int(self.letra_actual) == 0:
                self.estado_actual = 9
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'Cadena no aceptada'

    def estado_siete(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) > 0:
                self.estado_actual = 8
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'Cadena no aceptada'
        else:
            self.estado_actual = 10
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def estado_ocho(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == ' ':
                print 'Esto es un numero en notacion cientifica ', self.valor_lexema
                self.aceptacion = False
            elif str(self.letra_actual) in self.punt:
                print 'Esto es un numero en notacion cientifica ', self.valor_lexema
                self.aceptacion = False
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 8
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True

    def estado_nueve(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == ' ':
                print 'Esto es un numero en notacion cientifica ', self.valor_lexema
                self.aceptacion = False
            elif str(self.letra_actual) in self.punt:
                print 'Esto es un numero en notacion cientifica ', self.valor_lexema
                self.aceptacion = False
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.aceptacion = False
            print 'Cadena no aceptada'

    def estado_diez(self):
        if str(self.letra_actual) == ' ':
            if self.valor_lexema in self.reserv:
                print 'Esto es una palabra reservada', self.valor_lexema
                self.actpacion = False
            elif str(self.letra_actual) in self.punt:
                print 'Esto es una cadena ', self.valor_lexema
                self.aceptacion = False
            else:
                print 'Esto es una cadena ', self.valor_lexema
                self.aceptacion = False
        else:
            self.estado_actual = 10
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True

    def estado_once(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[2]:
                self.estado_actual = 6
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == ' ':
                print 'Esto es un numero real ', self.valor_lexema
                self.aceptacion = False
            elif str(self.letra_actual) in self.punt:
                print 'Esto es un numero real ', self.valor_lexema
                self.aceptacion = False
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 11
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True

    def analizar(self, cadena):
        cadena = str(cadena)
        palabras = cadena.split()
        for i in palabras:
            self.aceptacion = True
            self.valor_lexema = ""
            self.estado_actual = 0
            i = i + ' '
            for x in i:
                if self.aceptacion == True:
                    self.letra_actual = x
                    self.switch(self.estado_actual)

Analizador_Texto().analizar(raw_input('Escriba la cadena: '))
