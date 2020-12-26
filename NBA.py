import numpy as np
import pandas as pd

disease = pd.read_csv('disease.csv', delimiter=";")
symptom = pd.read_csv('symptom.csv', delimiter=";")

rand_symp = [np.random.randint(0, 2) for i in range(23)]

P_disease = []
for i in range(len(disease) - 1):
    P_disease.append(disease['количество пациентов'][i] / disease['количество пациентов'][len(disease) - 1])

P_dis_sympt = [1] * (len(disease) - 1)


p = 1
for i in range(1, 23 + 1):
    if rand_symp[i - 1] == 1:
        p *= sum(symptom.iloc[i][1:]) / 9

for i in range(len(disease) - 1):
    P_dis_sympt[i] *= P_disease[i]
    for j in range(len(symptom) - 1):
        if rand_symp[j] == 1:
            P_dis_sympt[i] *= float(symptom.iloc[j + 1][i + 1])
        P_dis_sympt[i] /= p


disease_p = {}
for i in range(len(disease) - 1):
    disease_p[disease.iloc[i][0]] = P_dis_sympt[i]

# Выводим болезни в порядке возрастания вероятностей
print("Скорее всего это: ", sorted(disease_p, key=disease_p.get)[0])
