import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate (w):
    w = w.lower()
    
    #Verifica que la palabra se encuentra en el diccionario
    if w in data:
        return data[w]
    #Verifica la palabra convirtiendo la primer letra en mayuscula
    elif w.title() in data:
        return data[w.title()]
    #Verifica la palabra convirtiendola a mayuscula
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    #utiliza la función get_close_matches para validar una posible coincidencia con la palabra ingresada
    #y regresa esa palabra aproximada ej. rainn regresa rain
    elif len(get_close_matches(w, data.keys()))>0:
        yn =input( "Did you mean %s instead? Enter Y if yes or N if no." % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn´t exist.Please double check it."
        else:
            return "We didn't understand your entry"
         
    else:
        return "The word doesn´t exist.Please double check it."

word = input("Enter word: ")
output= translate(word)

#verifica si el resultado es una lista (más de una definicion), para imprimirla en diferentes líneas
#Sí solo es una, solo la imprime.
if type(output) == list:
    for item in output:
        print(item)
else:
    print (output)
