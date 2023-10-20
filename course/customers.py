Clients = []
infoClient = {}

def addClient():
    
    name = input("Nom: ")
    firstName = input("Prénom: ")
    age = input("Age: ")
    email = input("Email: ")
    hobbies = input("Hobbies: ")
    
    infoClient = {
        "name": name,
        "age": age,
        "email": email,
        "hobbies": hobbies
    }
    
    Clients.append(infoClient)

addClient()

print(Clients)