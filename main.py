import webbrowser

def afficher_menu():
    print("Menu:")
    print("1. DDOS TOOLS  ")
    print("2. DOX TOOLS")
    print("3. IP LOGGER ")
    print("4. open_ai")
    print("5. Quitter")

def DDOS_TOOLS():
    webbrowser.open('https://github.com/Illegal-Services/Illegal_Services')

def DOX_TOOLS():
    webbrowser.open('https://osintframework.com/')

def IP_LOGGER():
    webbrowser.open('https://iplogger.org/fr/')

def ouvrir_openai():
    webbrowser.open('https://www.openai.com')

# Art ASCII en rouge
texte_art_ascii = "\033[91m" + """
                                                                                                                            
                                                                                                                             
    ,---,                                   ,-.                   ,---,                                              ,--,    
  .'  .' `\                             ,--/ /|                  '  .' \                                           ,--.'|    
,---.'     \                  __  ,-. ,--. :/ |                 /  ;    '.           ,---,                         |  | :    
|   |  .`\  |               ,' ,'/ /| :  : ' /                 :  :       \      ,-+-. /  |   ,----._,.            :  : '    
:   : |  '  |    ,--.--.    '  | |' | |  '  /                  :  |   /\   \    ,--.'|'   |  /   /  ' /    ,---.   |  ' |    
|   ' '  ;  :   /       \   |  |   ,' '  |  :                  |  :  ' ;.   :  |   |  ,"' | |   :     |   /     \  '  | |    
'   | ;  .  |  .--.  .-. |  '  :  /   |  |   \                 |  |  ;/  \   \ |   | /  | | |   | .\  .  /    /  | |  | :    
|   | :  |  '   \__\/: . .  |  | '    '  : |. \                '  :  | \  \ ,' |   | |  | | .   ; ';  | .    ' / | '  : |__  
'   : | /  ;    ," .--.; |  ;  : |    |  | ' \ \          ___  |  |  '  '--'   |   | |  |/  '   .   . | '   ;   /| |  | '.'| 
|   | '` ,/    /  /  ,.  |  |  , ;    '  : |--'        .'  .`| |  :  :         |   | |--'    `---`-'| | '   |  / | ;  :    ; 
;   :  .'     ;  :   .'   \  ---'     ;  |,'        .'  .'   : |  | ,'         |   |/        .'__/\_: | |   :    | |  ,   /  
|   ,.'       |  ,     .-./           '--'       ,---, '   .'  `--''           '---'         |   :    :  \   \  /   ---`-'   
'---'          `--`---'                          ;   |  .'                                    \   \  /    `----'             
                                                 `---'                                         `--`-'                     
""" + "\033[0m"  # Réinitialiser la couleur à la valeur par défaut
print(texte_art_ascii)
# Boucle principale du menu
while True:
    afficher_menu()

    choix = input("Faites votre choix (1-5): ")

    if choix == '1':
        DDOS_TOOLS()
    elif choix == '2':
        DOX_TOOLS()
    elif choix == '3':
        IP_LOGGER()
    elif choix == '4':
        open_ai()
    elif choix == '5':
        print("Merci d'avoir utilisé mon outil. À bientôt !")
        break
    else:
        print("Choix invalide. Veuillez sélectionner une option de 1 à 5.")
