# 1.Classe Bola: Crie uma classe que modele uma bola:
#   a.Atributos: Cor, circunferência, material
#   b.Métodos: trocaCor e mostraCor

class bola():

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
    
    def trocaCor(self):
        print("azul")
    
    def mostraCor(self):
        print(cor)


# 2.Classe Quadrado: Crie uma classe que modele um quadrado:
#   a.Atributos: Tamanho do lado
#   b.Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado():

    def __init__(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado
    
    def mudaValorLado(self, mudaValorLado):
        self.mudaValorLado = mudaValorLado
        return f'Valor do lado {tamanhoLado + 1}'

    # def retornaValorLado(self, retornaValorLado):
    #     self.retornaValorLado = retornaValorLado
    #     print(tamanhoLado)
    #     print(f'{tamanhoLado * 2 }cm²')

t1 = Quadrado(3)
t1.mudaValorLado(5)
# t1.retornaValorLado(10)

print(t1)




