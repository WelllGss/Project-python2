from datetime import datetime

def digitsValidation(number):
    if(number.isdigit()):
        return int(number)
    return False

def decimalValidation(number):
    try:
        float(number)
        return number
    except ValueError:
        return False

def ageValidation(age):
    validAge = digitsValidation(age)
    if(not validAge):
        print('O valor informado é invalido, por favor digite apenas números!')
        return False
    
    if(validAge <= 6 or validAge >= 89):
        print('Só aceitamos cadastro de maiores de 6 anos, e menores de 89 anos')
        return False
    
    if(validAge):
        return validAge
    
def dataValidation():
    releaseDate = input('Digite a data de lançamento no formato [DD/MM/AAAA]\nData: ')
    try:
        data = datetime.strptime(releaseDate, '%d/%m/%Y')
        return releaseDate
    except ValueError:
        print(f"A data {releaseDate} não é válida. Por favor, insira uma data no formato DD/MM/AAAA.")
        input()
        return False
