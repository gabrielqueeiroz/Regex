import re
a = 200
def galaxia(aux, destino):
    galaxias = ["ANDROMEDA", "VIA LACTEA", "TRIANGULO", "REDEMOINHO", "SOMBREIRO", "GIRASSOL", "GRANDE NUVEM DE MAGALHAES", "PEQUENA NUVEM DE MAGALHAES", "COMPASSO", "ANA DE FENIX", "MESSIER 87", "MESSIER 32", "LEO I", "MESSIER 110"]
    match = 0
    for i in galaxias:
        if aux.upper() == i or destino.upper() == i:
            match+=1
    if match == 2 and (aux.upper() != destino.upper()):
        return True
    else:
        return False
def passageiro(aux):
    cont = 0
    if len(aux) == 11:
        if re.match(r'[0-8]{3}-\d{2}-\d{4}', aux):
            for i in range(11):
                if aux[i] != '-' and aux[i] == aux[0]:
                    cont+=1
            aux = aux.split('-')
            if cont == 9:
                return False
            if aux[0].count('0') >= 3 or aux[1].count('0') >= 2 or aux[2].count('0') >= 4 or aux[0] == '666':
                return False
            if (aux[0] == '078' and aux[1] == '85' and aux[2] == '1120') or (aux[0] == '219' and aux[1] == '09' and aux[2] == '9999'):
                return False
            return True
    else:
        return False
    return False
def timestamp(aux): 
    checa = {1:31, 2:28, 3:30, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if len(aux) == 16:
        if re.match(r'(([0-2][0-9])|(3(0|1)))\/((0[1-9])|(1[0-2]))\/\d{4}\s{1}(([0|1]\d:([0-5]\d))|24:00|2[0-3]:([0-5]\d))', aux):
            aux = aux.split('/')
            if (int(aux[0]) <= checa[int(aux[1])]) :
                return True
    else:
        return False
    return False
def nave(aux):
    nave = ["NEBULA CLASS A", "NEBULA CLASS B", "INTREPID CLASS", "NIAGARIA CLASS", "WELLS CLASS", "HOLOSHIP", "RAVEN", "PEREGRINE", "DANUBE CLASS"]

    for i in nave:
        if aux.upper() == i:
            return True
    return False
def valor(aux):
    if re.match(r'(BTC (0\.\d{3}|1))|(ETH \d{1,3})|(LTC \d{2}\.\d{2})', aux):
        return True
    return False
def codigo(aux):
    if len(aux) == 12:
        upper = 0
        lower = 0
        special = 0
        digit = 0
        for i in aux:
            if re.match(r'[A-Z]', i):
                upper+=1
            elif re.match(r'[a-z]', i):
                lower+=1
            elif re.match(r'[\W]', i):
                special+=1
            elif re.match(r'[\d]', i):
                digit+=1
        if upper == 3 and lower == 3 and special == 2 and digit == 4:
            return True
    return False
def md(aux):
    cont = 0
    if len(aux) == 32:
        for i in aux:
            if re.match(r'[0-9]', i):
                cont+=1
            elif re.match(r'[a-f]', i):
                cont+=1
        if cont == 32:
            return True
    return False           


soma = [0, 0, 0]
dados = input()
while dados != 'END':
    
    dados = dados.split(',')
    if galaxia(dados[0], dados[1]) and passageiro(dados[2]) and timestamp(dados[3]) and nave(dados[4]) and valor(dados[5]) and codigo(dados[6]) and md(dados[7]):
        print("True")
        aux = dados[5].split(' ')
        if aux[0] == 'BTC':
            soma[0] += float(aux[1])
        elif aux[0] == 'ETH':
            soma[1] += float(aux[1])
        elif aux[0] == 'LTC':
            soma[2] += float(aux[1])
    else:
        print("False")
    dados = input()
print('BTC %.2f\nETH %.2f\nLTC %.2f' % (soma[0], soma[1], soma[2]))