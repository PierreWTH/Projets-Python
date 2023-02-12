a = input("Entrez un nombre : ")
b = input("Entrez un nombre : ")

while a.isdigit() == False or b.isdigit() == False: 
    print("Veuillez entrer deux nombres valides. ")
    a = input("Entrez un nombre : ")
    b = input("Entrez un deuxième nombre : ")

else:
    print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")