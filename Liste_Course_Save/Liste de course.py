import sys
import json
import os
from textwrap import indent


chemin_liste = "/Users/pierre/desktop/Python/COURSE_LISTE_SAVE/liste.json"

if os.path.exists(chemin_liste):
    FICHIER = open(chemin_liste, "r")

else: 
    FICHIER = open(chemin_liste, "x")

LISTE1 = []

MENU = """Choississez parmis les 5 options suivantes : 
1 : Ajouter un élément à la liste
2 : Retirer un élement de la liste
3 : Afficher la liste
4 : Vider la liste
5 : Quitter
👉 Votre choix ? : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True :
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES: 
            print("Veuillez choisir une option valide. ")

    if user_choice == "1" : #Ajouter un élement
        item = input("Entrez le nom d'un élément à ajouter à la liste de course : ")
        with open(chemin_liste, "a") as LISTE:
            json.dump(LISTE1, item)
        print(f"L'élement {item} a bien été ajouté à la liste.")

    elif user_choice == "2" : #Retirer un élement
        item = input("Entrez le nom d'un élément à retirer de la liste de course : ")
        if item in FICHIER:
            with open(chemin_liste, "a") as FICHIER:
                FICHIER.remove(item)
            print(f"L'élement {item} a bien été retiré de la liste")
        else: 
            print(f"L'élement {item} n'est pas dans la liste")

    elif user_choice == "3" : #Afficher la liste
        if os.stat(chemin_liste).st_size == 0:
            print("Votre liste ne contient aucun élément. ")

        else:
            print("Voici le contenu de votre liste : ")
            with open(chemin_liste, "r") as FICHIER:
                contenu = FICHIER.read()
                print(contenu)
            

    elif user_choice == "4":
         with open(chemin_liste, "w") as FICHIER:
            FICHIER.write("")
         print("La liste à été effacée. ")

    elif user_choice == "5" :
        print("Merci et à bientôt. ")
        sys.exit()

    print("-" * 50)


        
    

