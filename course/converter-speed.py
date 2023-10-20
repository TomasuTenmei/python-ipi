speed_kmh = input("Veuillez entrer une vitesse en km/h : ")

KMH_TO_MPH = 1.609
result = float(speed_kmh) / 1.609

print(f"La vitesse en miles/h est de : {result:.2f}")
