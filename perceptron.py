import random
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt
import time

class Perceptron:

    # Inicializacao do objeto Perceptron
    def __init__(self, sample, exit, learn_rate, epoch_number, erro, bias):
        self.sample = sample
        self.exit = exit
        self.learn_rate = learn_rate
        self.epoch_number = epoch_number
        self.erro_min = erro
        self.bias = bias
        self.number_sample = len(sample)
        self.col_sample = len(sample[0])
        self.weight = []

    # Funcao de Treinamento do Perceptron (Metodo Gradiente Descendente)
    def trannig(self):
        # Marca o tempo de início do algoritmo
        start = time.time()

        for sample in self.sample:
            sample.insert(0, self.bias)
        
        # Inicializa os pesos w aleatoriamente
        for i in range(self.col_sample):
           self.weight.append(random.random())

        # Insere peso da entrada de polarizacao(bias)
        self.weight.insert(0, self.bias)

        epoch_count = 0

        # Vetor responsável por montar o gráfico para análise
        errors = []

        # Vetor responsável por armazenar o retornar a quantidade de épocas e o erro do treinamento
        data_training = []

        # Metodo do Gradiente Descendente para ajuste dos pesos do Perceptron
        while True:
            erro = 0

            # Vetor responsável por armazenar a saida treinada
            y_trained = []

            for i in range(self.number_sample):
                u = 0
                for j in range(self.col_sample + 1):
                    u = u + self.weight[j] * self.sample[i][j]
                y = self.sign(u)
                # Armazena as saidas em um vetor para verificação do erro ao final da época
                y_trained.append(y)
                if y != self.exit[i]:
                    for j in range(self.col_sample + 1):
                        self.weight[j] = self.weight[j] + self.learn_rate * (self.exit[i] - y) * self.sample[i][j]

            # Calcula a entropia cruzada do erro para verificar a qualidade da métrica
            erro = log_loss(self.exit, y_trained)

            # Adiciona o erro correspondente a sua época
            errors.append(erro)

            print('Epoca/Erro: \n',epoch_count, erro)
            epoch_count = epoch_count + 1


            #Para o algoritmo se alcançar a marca de épocas estipuladas
            if epoch_count == self.epoch_number:
                # Marca o tempo final de treinamneto do algoritmo
                end = time.time()
                print('\nEpocas alcançadas: ', epoch_count)
                print('------------------------\n')
                self.makegraph(epoch_count,errors)
                data_training.append(epoch_count)
                data_training.append(erro)
                data_training.append(start)
                data_training.append(end)
                break
                

            # Para o algoritmo se alcançar a marca de erro desejada
            if erro <= self.erro_min:
                # Marca o tempo final de treinamneto do algoritmo
                end = time.time()
                print(('\nEpocas alcançadas:\n', epoch_count))
                print('------------------------\n')
                self.makegraph(epoch_count,errors)
                data_training.append(epoch_count)
                data_training.append(errors)
                data_training.append(start)
                data_training.append(end)
                break

        return data_training

    # Função responsável por montar o gráfico de saída do Erro x Épocas
    def makegraph(self, epoch_count, errors):

        plt.plot(range(epoch_count), errors)
        plt.title('Erros X Epocas')
        plt.xlabel('Epocas')
        plt.ylabel('Erros')
        fig = plt.gcf()
        plt.show()
        fig.savefig('ErroxEpoca.png', format='png')

    def sort(self, sample):

        output = []
        for i in range(len(sample)):
            sample[i].insert(0, self.bias)

        for i in range(len(sample)):
            u = 0
            for j in range(self.col_sample + 1):
                u = u + self.weight[j] * sample[i][j]

            # Chama função para classificar o email
            y = self.sign(u)
            # Armazena o resultado de saida no vetor output
            output.append(y)

        return output

    # Funcao de Ativacao
    def sign(self, u):
        # 1 Spam | 0 No-Spam
        return 1 if u >= 0 else 0
