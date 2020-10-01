import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# возраст и класс пассажиров
ages = pd.read_csv("./test.csv").Age
pclass = pd.read_csv("./test.csv").Pclass

ax = sns.histplot(x=pclass, y=ages, legend=True)
ax.set(title='Взаимосвязь класса от возраста')

plt.xlabel('Класс пассажира')
plt.ylabel('Возраст')
plt.show()