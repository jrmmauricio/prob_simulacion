
def getProbability(resp):
    if (resp == 'y'):
        return 1/30
    else:
        return 'adios.'

resp = input ('Desea conocer la probabilidad de escoger un estudiante de simulacion?(Y/N).')
print  (getProbability(resp))


