import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from perceptron import Perceptron

# Leitura do arquivo csv contendo as amostras dos emails
samples = pd.read_csv("sample.csv", sep=',')

# Saida: Coluna type informa 1 (spam) 0 (no-spam)
output = samples.loc[:,('type')]

# Entrada: Colunas contendo informações sobre o email
samples.drop(['type'], axis=1, inplace=True)
features = samples

# Convertendo dataframes em numpy array
x = features.to_numpy()
y = output.to_numpy()

#Convertendo numpy array em uma lista de listas
x = x.tolist()
y = y.tolist()

# Separando amostras de dados: 60% em amostras de treino, 40% amostras de teste
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.6, test_size=0.4)

# Inicializando o neuronio
neuron = Perceptron(sample=x_train, exit=y_train, learn_rate=0.1, epoch_number=5000, erro=2.5, bias=-1)

# Treinando o neuronio: Seu retorno será o número de épocas, o erro correspondente, tempo de inicio e término do algoritmo
data_training = neuron.trannig()

# Testando neuronio com os dados de teste
y_pred = neuron.sort(x_test)

# Relatório de análise de desempenho do algoritmo
accuracy = accuracy_score(y_test,y_pred)
confusion_mat = confusion_matrix(y_test,y_pred)
specificity = confusion_mat[0][0] / (confusion_mat[0][0] + confusion_mat[0][1])
sensitivity = confusion_mat[1][1] / (confusion_mat[1][0] + confusion_mat[1][1])
print(f'Tempo de treinamento:  {round((data_training[3] - data_training[2]),3)} segundos')
print('\nQuantidade de épocas: ', data_training[0])
print(f'\nErro:  {round(data_training[1],3)}')
print('\nAcurácia: ', round(accuracy,3))
print('\nSensibilidade: ', round(sensitivity,3))
print('\nEspecificidade: ', round(specificity,3))
print('\nConfusion Matrix:\n', confusion_mat)
print(classification_report(y_test,y_pred))
