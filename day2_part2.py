if __name__ == '__main__':
    fichier = open('passwords.txt', 'r') #open() pour ouvrir un fichier, r pour lire, w pour ecrire
    content = fichier.read() #lecture du fichier texte

    resOK = 0

    monTableau = [i for i in content.split('\n')] #decoupage a chaque ligne

    for j in monTableau:

        decoupe = j.split(' ')                    #IL FAUT CREER UN NEW TAB pour le decouper
        min = int(decoupe[0].split('-')[0])       #decoupage a chaque '-', case 0 du nouv tab
        max = int(decoupe[0].split('-')[1])
        lettre = decoupe[1].split(':')[0]
        mdp = decoupe[2]

        compteurLettre = mdp.count(lettre)

        if mdp[min-1] == lettre: #un string est deja un tab avec une letter sur une case chacune, on peut la pointé facilement
            if mdp[max-1] != lettre:
                resOK = resOK + 1

        if mdp[max - 1] == lettre:
            if mdp[min - 1] != lettre:
                resOK = resOK + 1

    print(resOK)