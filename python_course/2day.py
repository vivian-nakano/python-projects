#datatypes, numbers, operations, type conversion, f-strings

#print(len(12345)) >> esse erro apresenta código pois são números e a função len comporta apenas a contagem de strings

#encontrar a letra de acordo com o numero e posição dentro da chaves
def subscript():
    print("Hello"[4])

##DataTypes, TypeErrors

def character():

    num_char = len(input("NAME?"))
    new_num_char = str(num_char)
    print("Your name has " + new_num_char + " characters.")

def analyse_datatypes():

    a = str(123)
    print(type(a))

    a = float(123)
    print(type(a))

    print(70 + float("100.5"))

    print(str(70) + str(100))

analyse_datatypes()