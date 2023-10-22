val = input("Entrer un nombre: ")

def multiplicationTable(value):
    
    modTable = []
    
    for i in range(1, 11):
        
        result = value * i
        print(value, "x", i, "=", result)
        
        if result % 3 == 0:
            
            modTable.append(result)
            
    print("liste des nombres multiple de 3 dans ", value, ":", modTable)
        
multiplicationTable(int(val))