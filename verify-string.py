# Lógica para verificar presença de números em uma string

str1 = "python3"
if any(map(str.isdigit, str1)) == True:
    print("Possui número na string em alguma posição.")
    #raise ValueError("Possui número na string em alguma posição.") - estoura uma exceção.

str2 = "11python"
if len(str2) >= 2 and str2[0].isdigit() and str2[1].isdigit():
    print('Possui número nos dois primeiros caracteres.')

#verifica se a primeiro ou segundo caracter é número
str3 = "texto"
if str3[0].isdigit() or str3[1].isdigit():
  print("Possui número em alguma das duas primeiras casas.")