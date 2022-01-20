# entrada 1 = "DDUUUUDD" retorno 1
# entrada 2 = "UDDDUDUU" retorno 1
# entrada 3 = "UUDDDUUUDDUDDU" retorno 2

def func(steps,path):
    valles = 0
    if steps>1 and steps<(10**6)+1:
        nivel = 0   # nivel mar
        for i in path:
            if i == 'U':
                nivel += 1
            elif i == "D":
                nivel -=1
                if nivel == -1:
                    valles += 1

        return valles

entrada = "DDUUUUDD"
print("entrada 1: ",func(len(entrada),entrada))
entrada = "UDDDUDUU"
print("entrada 2: ",func(len(entrada),entrada))
entrada = "UUDDDUUUDDUDDU"
print("entrada 3: ",func(len(entrada),entrada))