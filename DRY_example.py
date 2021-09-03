def soma():
    num1 = 10
    num2 = 2
    print(f'Soma = {num1 + num2}')

def subtração():
    num1 = 10
    num2 = 2
    print(f'Subtração = {num1 - num2}')

def multiplicação():
    num1 = 10
    num2 = 2
    print(f'Multiplicação = {num1 * num2}')

def divisão():
    num1 = 10
    num2 = 2
    print(f'Divisão = {num1 / num2}')

if __name__ == '__main__':
    soma()
    subtração()
    multiplicação()
    divisão()

print('========================================================================')

class teste():
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        print(f'Soma = {self.num1 + self.num2}')

    def subtração(self):
            print(f'Subtração = {self.num1 - self.num2}')

    def multiplicação(self):
            print(f'Multiplicação = {self.num1 * self.num2}')

    def divisão(self):
            print(f'Divisão = {self.num1 / self.num2}')

if __name__ == '__main__':
     classe = teste(10, 2)  
     classe.soma()
     classe.subtração()
     classe.multiplicação()
     classe.divisão()