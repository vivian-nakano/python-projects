# Lógica para verificar presença de números em uma string

str1 = "python3"
if any(map(str.isdigit, str1)) == True:
    print("Possui número na string em alguma posição.")
    #raise ValueError("Possui número na string em alguma posição.") - estoura uma exceção.

str2 = "12python"
if len(str2) >= 2 and str2[0].isdigit() and str2[1].isdigit():
    print('Possui número em alguma das duas primeiras casas.')
