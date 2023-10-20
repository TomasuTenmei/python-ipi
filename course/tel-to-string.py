telInt = input("Entrer un numéro de téléphone : ")
dictNum = {"0":"Zero", "1":"Un", "2":"Deux", "3":"Trois", "4":"Quatre", "5":"Cinq", "6":"Six", "7":"Sept", "8":"Huit", "9":"Neuf"}

telString = str(telInt)
telString = list(telString)

for value in telString:
    
    if value == '+':
        
        print("Plus", end=" ")
    
    else:
        
        print(dictNum[value], end=" ")