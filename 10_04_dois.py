# -*- coding: utf-8 -*-
"""10.04 - dois.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PENl7bwWNX2_tI6Q3jCOZ2jIb5X1oNS1

#Bibliotecas
"""

import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from pandas.core.internals.base import Index
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

"""##Base"""

from google.colab import drive
drive.mount('/content/drive')

train = pd.read_csv('./drive/MyDrive/FATEC/treino.csv')
test = pd.read_csv('./drive/MyDrive/FATEC/teste.csv')

"""###CÓDIGO ⬇️"""

acertos = 0
erros = 0
GG = []
AA = []
GE = []
AE = []

x = train.drop('TargetClass', axis=1)  # Selecionando as colunas de atributos
y = train['TargetClass']  # Selecionando a coluna alvo

x_test = test.drop('TargetClass', axis=1)  # Selecionando as colunas de atributos
y_test = test['TargetClass'] # Selecionando a coluna alvo

# Definindo o modelo Gaussian Naive Bayes
gnb = GaussianNB()

# Ajustando o modelo aos dados de treinamento
gnb.fit(x, y)

# Fazendo previsões nos dados de teste
y_pred = gnb.predict(x_test)

# Avaliando o desempenho do modelo
GaussianNB()

for i in range(len(y_test)):
  if(y_test[i] == y_pred[i]):
    if(y_test[i] == 1):
      GG.append(y_test[i])
    else:
      AA.append(y_test[i])
    acertos += 1
  else:
    if(y_test[i] == 1):
      AE.append(y_test[i])
    else:
      GE.append(y_test[i])
    erros += 1

"""##Resultados 😊🙌"""



print('Acertos: ', acertos, ' Erros: ', erros, ' Total: ', len(y_pred))
print('Acurácia:', accuracy_score(y_test, y_pred))
print('\nMATRIZ DE CONFUSÃO:\n')
print('      Anã | Gigante')
print('Anã: ', len(AA), '|', len(AE))
print('Gig: ', len(GE), ' |' , len(GG))

"""##Gráfico ❤️"""

# Dados de exemplo
x = ['Acertos', 'Erros']
y = [acertos, erros]

# Criando o gráfico
fig, ax = plt.subplots()
ax.bar(x, y)

# Personalizando o gráfico
ax.set_title('Acertos X Erros')
ax.set_xlabel('Categorias')
ax.set_ylabel('Valores')

# Exibindo o gráfico
plt.show()