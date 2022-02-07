#Chute um número até acertar

import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
        self.tentativa = 0  #conta em quantas chances acertou

    #Função principal do jogo
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentar_novamente == True:
                if (self.valor_do_chute) > self.valor_aleatorio:
                    print('Chute um valor mais baixo!')
                    self.PedirValorAleatorio()
                    self.tentativa += 1
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print('Chute um valor mais alto!')
                    self.PedirValorAleatorio()
                    self.tentativa += 1
                if self.valor_do_chute == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print(f"Parabéns, você acertou em {self.tentativa} chances!!")
        except:
            print('Digite apenas números!!')
            self.Iniciar()

    #Método para pedir um número ao jogador
    def PedirValorAleatorio(self):
        self.valor_do_chute = int(input('Chute um numero: '))

    #Método para gerar um número aleatório
    def GerarNumeroAleatorio(self):
         self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)



chute = ChuteONumero()
chute.Iniciar()

