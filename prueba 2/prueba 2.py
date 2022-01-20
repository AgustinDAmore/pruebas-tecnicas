# entrada = [1,2,1,2,1,3,2] retorno 2
# entrada = [1,2,1,2,1,3,2,3] retorno 3
# entrada = [4,2,1,3,5] retorno 0

def func(n,lista):
    sock = 0
    if n>0 and n<101:
        yavistos=[]
        for i in lista:
            if i in yavistos:
                continue
            else:
                yavistos.append(i)
                sock += lista.count(i)//2

        return sock

entrada = [1,2,1,2,1,3,2]
print("entrada 1: ",func(len(entrada),entrada))
entrada = [1,2,1,2,1,3,2,3]
print("entrada 2: ",func(len(entrada),entrada))
entrada = [4,2,1,3,5]
print("entrada 3: ",func(len(entrada),entrada))