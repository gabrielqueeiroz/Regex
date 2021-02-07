import re
import sys
import os

file = open(input(), "r")
#ver = file.readlines()is None
#print(ver)
texto = file.readlines()

if len(texto) != 0:
    def validaCab(texto):
        name = re.search(r"[A-z][A-z, ]{1,50}", texto[0])is None
        if name:
            print("CABECALHO INVALIDO")
            sys.exit(0)
        cpf = re.search(r"\s\d{3}\.\d{3}\.\d{3}-\d{2}$", texto[1])is None
        if cpf:
            print("CABECALHO INVALIDO")
            sys.exit(0)
        cpf2 = re.search(r"\s\d{3}\.\d{3}\.\d{3}-\d{2}$", texto[1])
        cpf1 = re.search(r"[\d.]+-", texto[1])
        aux = cpf1.group()
        armazenaCpf = cpf2.group()
        matricula = re.search(r"\s[0-9]{10}$", texto[2])is None
        if matricula:
            print("CABECALHO INVALIDO")
            sys.exit(0)
        separador = re.search(r"-{20}$", texto[3])is None
        if separador:
            print("CABECALHO INVALIDO")
            sys.exit(0)
        def verificaCpf(vet, cont):
            a = 0
            for i in vet:
                a += i * cont
                cont -= 1

            if (a % 11) < 2:
                dig = 0
            else:
                dig = 11 - (a % 11)
            vet.append(dig)

            return vet
        vetor = []
        cont = 0
        for i in aux:
            if i != '.' and i != '-':
                vetor.append(int(aux[cont]))
            cont += 1

        dig1 = verificaCpf(vetor, 10)
        dig2 = verificaCpf(dig1, 11)
        if str(dig2[9]) == armazenaCpf[13] and str(dig2[10]) == armazenaCpf[14]:
            print("CABECALHO VALIDO")
        else:
            print("CABECALHO INVALIDO")
            sys.exit(0)
    validaCab(texto)
    linhasinv = []
    creditosT = 0
    somaV = 0
    notaAux = ''
    for i in range(4, len(texto)):
        captura = re.search(r"\d{4}/((1-1)|(2-2))\sEST(LIC|BSI|BAS|ECP)\d{3}\s\"[A-z][A-z, ]{1,}\d{0,1}\"\s(ECP|BSI|LIC|ENG)(TFP|\d{2})_T\d{2}\s\d,\d{2}\s\d{1,2}.\d{2}\sAPROVADO|REPROVADO", texto[i])is None
        if captura != False:
            linhasinv.append(i)
        else:
            nota = re.search(r"\d{1,2}\.\d{2}", texto[i])
            nota = nota.group()
            status = re.search(r"APROVADO|REPROVADO", texto[i])
            status = status.group()
            creditos = re.search(r"\d,\d{2}", texto[i])
            creditos = creditos.group()

            for k in nota:
                if k == '.':
                    break
                else:
                    notaAux += k

            if int(notaAux) >= 6 and status == 'REPROVADO' or int(notaAux) < 6 and status == 'APROVADO' or int(notaAux) > 10:
                linhasinv.append(i)
            else:
                creditosT += int(creditos[0])
                somaV += int(notaAux) * int(creditos[0])
            notaAux = ''

    if len(linhasinv) != (len(texto)-4):
        if linhasinv:
            print('LINHAS INVALIDAS:')
            for j in linhasinv:
                print('LINHA %02d' % (j-3))
    if creditosT == 0:
        creditosT = 1
    #print(len(linhasinv))
    if creditosT > 10:
        print('CRE: %.2f' % (somaV/creditosT))
    else:
        print('CRE: %.2f' % 0)
else:
    print("CABECALHO INVALIDO")
file.close()