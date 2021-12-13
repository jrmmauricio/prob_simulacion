def getProbability():
     return 1/30
    

asking = False
while (asking == False):
    resp = input ('Desea conocer la probabilidad de escoger un estudiante de simulacion?(Y/N): ')
    if (resp == 'y' or resp == 'Y'):
        asking = True
        print('Existe una probabilidad de: ', getProbability())
    else:
        if (resp == 'n' or resp == 'N'):
            print('adios.')
            asking = True
    

