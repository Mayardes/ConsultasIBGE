from questao_01.q1 import q1
from questao_02.q2 import q2
from questao_03.q3 import q3

try:
    file = open("dataset/data.txt", 'r', encoding='utf-8')

#primeira questão:
    print(q1)
    cont = 0
    total = 0.0
    for linha in file:
        valores = linha.split(';')
        if(valores[3] == 'Manaus'):
            cont = cont + 1
            total = total + float(valores[13])

    print(round(total/cont)) #arredondamento


#segunda questão:
    print(q2)

    #Rondonia
    file.seek(0,0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if(valores[1] == 'RO'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaRO = round(total/cont);
    print('RO = ', MediaRO)


    #Acre
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'AC'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaAC = round(total / cont);
    print('AC = ', MediaAC)

    # Amazonas
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'AM'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaAM = round(total / cont);
    print('AM = ', MediaAM)

    # Roraima
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'RR'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaRR = round(total / cont);
    print('RR = ', MediaRR)

    # Pará
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'PA'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaPA = round(total / cont);
    print('PA = ', MediaPA)

    # Tocantins
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'TO'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaTO = round(total / cont);
    print('TO = ', MediaTO)

    # Maranhão
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'MA'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaMA = round(total / cont);
    print('MA = ', MediaMA)

    # Piauí
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'PI'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaPI = round(total / cont);
    print('PI = ', MediaPI)

    # Ceará
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'CE'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaCE = round(total / cont);
    print('CE = ', MediaCE)

    # Rio Grande do Norte
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'RN'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaRN = round(total / cont);
    print('RN = ', MediaRN)

    # Paraíba
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'PB'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaPB = round(total / cont);
    print('PB = ', MediaPB)

    # Pernanbuco
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'PE'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaPE = round(total / cont);
    print('PE = ', MediaPE)

    # Alagoas
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'AL'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaAL = round(total / cont);
    print('AL = ', MediaAL)

    # Sergipe
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'SE'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaSE = round(total / cont);
    print('SE = ', MediaSE)

    # Bahia
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'BA'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaBA = round(total / cont);
    print('BA = ', MediaBA)

    # Minas Gerais
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'MG'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaMG = round(total / cont);
    print('MG = ', MediaMG)

    # Espírito Santo
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'ES'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaES = round(total / cont);
    print('ES = ', MediaES)

    # Rio de Janeiro
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'RJ'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaRJ = round(total / cont);
    print('RJ = ', MediaRJ)


    # São Paulo
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'SP'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaSP = round(total / cont);
    print('SP = ', MediaSP)

    # Paraná
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'PR'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaPR = round(total / cont);
    print('PR = ', MediaPR)

    # Santa Catarina
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'SC'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaSC = round(total / cont);
    print('SC = ', MediaSC)

    # Rio Grande do Sul
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'RS'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaRS = round(total / cont);
    print('RS = ', MediaRS)

    # Mato Grosso do Sul
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'MS'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaMS = round(total / cont);
    print('MS = ', MediaMS)

    # Mato Grosso
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'MT'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaMT = round(total / cont);
    print('MT = ', MediaMT)

    # Goiás
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'GO'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaGO = round(total / cont);
    print('GO = ', MediaGO)


    # Distrito Federal
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2010'):
            if (valores[1] == 'DF'):
                total = total + float(valores[13])
                cont = cont + 1

    MediaDF = round(total / cont);
    print('DF = ', MediaDF)

    # terceira questão:
    print(q3)

    #valor bruto médio do setor de serviços...(Todos os estados)
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2018'):
            total = total + float(valores[8])
            cont = cont + 1

    ValorBrutoMedio = round(total / cont);
    print('Valor Bruto Médio = ', ValorBrutoMedio)


    #valor bruto médio do estado do Amazonas
    file.seek(0, 0)
    cont = 0
    total = 0.0

    for linha in file:
        valores = linha.split(';')
        if (valores[0] == '2018'):
            if(valores[1] == 'AM'):
                total = total + float(valores[8])
                cont = cont + 1

    ValorBrutoMedioAmazonas = round(total / cont);
    print('Valor Bruto Médio Amazonas = ', ValorBrutoMedioAmazonas)


    file.close()
except:
    print("Error ao encontrar o arquivo!")

