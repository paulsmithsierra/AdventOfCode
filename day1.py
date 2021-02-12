if __name__ == '__main__':
    fichier = open('input.txt', 'r') #open() pour ouvrir un fichier, r pour lire, w pour ecrire
    content = fichier.read() #lecture du fichier texte

    monTableau = [int(i) for i in content.split('\n')] #discomprehension pour traduire les string en int

    for monIterateur in monTableau:

        for j in monTableau:

            for k in monTableau:
                addition = monIterateur + j + k

                if addition == 2020:
                    multiplication = monIterateur * j * k
                    reponse = multiplication

    print(reponse)