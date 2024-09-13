class Calculadora:
    '''Define a classe Calculadora.'''

    # Construtor da classe
    def __init__(self):
        '''Construtor da classe Calculadora.'''
        pass

    # Método para somar dois números
    def somar(self, num1, num2):
        '''Recebe dois números e retorna a soma deles.'''
        return float(num1) + float(num2)

    # Método para subtrair dois números
    def subtrair(self, num1, num2):
        '''Recebe dois números e retorna a diferença entre eles.'''
        return float(num1) - float(num2)

    # Método para multiplicar dois números
    def multiplicar(self, num1, num2):
        '''Recebe dois números e retorna o produto deles com duas casas decimais.'''
        return round(float(num1) * float(num2), 2)

    # Método para dividir dois números
    def dividir(self, num1, num2):
        '''Recebe dois números e retorna o quociente deles. Lida com divisão por zero.'''
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            return None
        else:
            return float(num1) / float(num2)

c = Calculadora()

# Soma: 8.0
print("Soma: ", c.somar(5, 3))

# Subtração: 3.0
print("Subtração: ", c.subtrair(10, 7))

# Multiplicação: 10.0
print("Multiplicação: ", c.multiplicar(4, 2.5))

# Divisão: 5.0
print("Divisão: ", c.dividir(20, 4))

# Divisão por zero: Erro: Divisão por zero não é permitida.
print("Divisão por zero: ", c.dividir(20, 0))
