import os
from fpdf import FPDF

# Criando um PDF
# P = documento na vertical
# L = documento na horizontal
# Medidas do documento = mm, cm, in
# Formatos de documento = A3, A4, A5, Latter e Legal.
pdf = FPDF('P', 'mm', 'A4')

# Criando uma página para o PDF
pdf.add_page()

# Configurando a fonte 1
# Nome da fonte, formato (B, U, I ou '') e o tamanho
pdf.set_font('Times', '', 12)

# Adicionando nome no PDF
pdf.cell(0, 0, txt='Nome: Pedro Henrique Silva Bonfim', align="J")

# Criando uma linha (ex: ------------------------)
pdf.line(5, 15, 205, 15)

#----------------------------------------------------

# Adicionando título ao PDF
pdf.cell(-190, 20, txt='CoronaVírus e seus estragos', align= 'C')

# Adicionando texto ao PDF
pdf.cell(0, 32, txt='Como todos nós sabemos, 2020 começou com a triste notícia sobre o Covid 19 que abalou o mundo todo', align= 'J')
pdf.cell(-184, 42, txt='E todos nós tivemos que nos adaptar a rotinas e regras totalmente diferentes;', align='C')
pdf.cell(173, 52, txt='Como por exemplo o uso da máscara para poder sair de casa', align= 'C')
pdf.cell(-175, 62, txt='o que gerou muita polêmica ao longo desses 2 anos de pandemia.', align='C')
pdf.cell(191, 72, txt='com o tempo passando o que nós pensamos que seria apenas algo semelhante com a gripe,', align='C')
pdf.cell(-195, 82, txt='virou um pesadelo, fazendo com que diversas pessoas perdessem seus respectivos empregos', align='C')
pdf.cell(161, 92, txt='e outros perdessem seus entes queridos realmente bagunçando a vida de todos.', align='R')
pdf.cell(-139, 102, txt='O objetivo deste projeto é mostrar dados reais das perdas que tivemos para o CoronaVírus', align='C')

# Criando uma linha (ex: ------------------------)
pdf.line(5, 92, 205, 92)

#----------------------------------------------------

# Adicionando título dos gráficos no PDF
pdf.cell(118, 172, txt='Gráfico que nos mostra diferença de Casos de diferentes municípios', align="C")

# Adicionando as imagens dos gráfico no PDF
pdf.image(name="casos_1.png", w=210, h=100, y=102, x=5)
pdf.image(name="casos_2.png", w=210, h=100, y=202, x=5)

# Salvando o arquivo PDF
pdf.output('Covid 19.pdf')

print("O PDF foi criado com sucesso!")

os.system("pause")