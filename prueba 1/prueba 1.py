# entrada = [()]{}{[()()]()} CORRECTO
# entrada = [(]) INCORRECTO

entrada = input("Ingrese una cadena: ")
pila = []
for i in entrada:
    if i == ")":
        if pila[-1] == "(":
            pila.pop()
        else:
            print("INCORRECTO")
            break
    elif i == "]":
        if pila[-1] == "[":
            pila.pop()
        else:
            print("INCORRECTO")
            break
    elif i == "}":
        if pila[-1] == "{":
            pila.pop()
        else:
            print("INCORRECTO")
            break
    else:
        pila.append(i)
else:
    print("CORRECTO")