#Biblioteca para criar um dataframe (Planilha) dentro do python
import pandas as pd

#Biblioteca para plotar os gráficos
import seaborn as sns
import matplotlib.pyplot as plt


covid = pd.read_csv('MUNICÍPIO.csv', sep = ';', encoding='latin-1')


covid.head()


#municipios = covid.query('Município == "Barueri" | Município == "Cotia"')
municipios = covid.query('Município == "Barueri" | Município == "Cotia"')


fig, (axis1) = plt.subplots(1, 1, figsize=(15, 5))
axis1 = sns.barplot(x = 'Município', y = 'Mun_Total de casos', data = municipios, ax = axis1, palette = 'mako')
axis1.set_title('Casos da Covid 19 por Municipios vizinhos', fontsize=25, pad=25)
axis1.set_ylabel("Total de Casos", fontsize=18)
axis1.set_xlabel("Município", fontsize=18)

plt.show()