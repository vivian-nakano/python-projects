#Simulador de dado: simular uso de dado, gerando valor de 1 até 6

import random

class SimuladorDeDado:

    def __init__ (self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Gostaria de gerar um novo valor para o dado?'