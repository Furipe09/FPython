# -*- coding: utf-8 -*-
arquivo = open("BRASILEIRO 2019 – RESULTADOS FINAIS.txt")
linhas = arquivo.readlines()
print(linhas)

for linha in linhas:
    print (linha)

texto_completo = arquivo.read()
print(texto_completo)