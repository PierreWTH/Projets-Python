from random import randint

# VARIABLE INTANGIBLES

menu_choice = ["1", "2"]
player_life = 50
ennemy_life = 50
potion_stock = 3

# BOUCLE PRINCIPALE

while player_life > 0 and ennemy_life > 0:

    #Variables aléatoires

    player_attack = randint(5, 10)
    ennemy_attack = randint(5, 15)
    potion_heal = randint(15, 50)
    
    #Saisie de l'utilisateur

    user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? : ")
    if user_choice not in menu_choice:
        print("Vous devez choisir entre 1 et 2.")
        continue

    # Déroulé du jeu

    elif user_choice == "1": #Choix 1
        ennemy_life -= player_attack
        player_life -= ennemy_attack
        
        if ennemy_life < 0:
            print("-" * 50)
            print(f"Vous avez infligé {player_attack} de dégats à l'ennemi. Il n'a plus de points de vie. ")
            print("Bravo ! Vous avez gagné le combat! 💪 ")
    
        elif player_life < 0:
            print("-" * 50)
            print(f"L'ennemi vous a infligé {ennemy_attack} points de dégat... Vous n'avez plus de points de vie. ")
            print("Dommage, vous êtes mort... 😢 ") 

        else: 
            print(f"Vous avez infligé {player_attack} points de dégat à l'ennemi.")
            print(f"L'ennemi vous a infligé {ennemy_attack} points de dégat. ")
            print(f"Il vous reste {player_life} points de vie. ")
            print(f"Il reste {ennemy_life} points de vie à l'ennemi. ")
            print("-" * 50)


    elif user_choice == "2": #Choix 2
        potion_stock -= 1
        
        while potion_stock < 0:
            print("Vous n'avez plus de potion 🧪 ...")
            break
            
        else: 
            player_life += potion_heal
            player_life -= ennemy_attack
            print(f"Vous récuperez {potion_heal} points de vie. {potion_stock} 🧪 restantes. ")
            print(f"L'ennemi vous a infligé {ennemy_attack} points de dégat. ")
            print(f"Il vous reste {player_life} points de vie. ")
            print(f"Il reste {ennemy_life} points de vie à l'ennemi. ")
            print("-" * 50)
            print("Vous passez votre tour")
            ennemy_attack = randint(5, 15)
            player_life -= ennemy_attack
            if player_life < 0:
                print("-" * 50)
                print(f"L'ennemi vous a infligé {ennemy_attack} points de dégat... Vous n'avez plus de points de vie. ")
                print("Dommage, vous êtes mort... 😢 ") 
            else : 
                print(f"L'ennemi vous a infligé {ennemy_attack} points de dégat. ")
                print(f"Il vous reste {player_life} points de vie. ")
                print(f"Il reste {ennemy_life} points de vie à l'ennemi. ")
                print("-" * 50)

print("Fin du jeu - Merci d'avoir joué ! ")


