from tkinter import *
import random
from tkinter import colorchooser
import sqlite3
from formes import *
from ddb import *

class FenPrincipale(Tk):
    def __init__(self):
        
        #Initialisation des couleurs utilisées
        self.clCanvas = "#5788E8"
        self.clFormePotence = "#8E572B"
        self.clFormeHomme = "#F0B585"
        self.clFond = "#FFFFFF"
        self.clFondFenetre = "#FFFFFF"
        
        self.chargeMots()#Charge la liste des mots
        
        Tk.__init__(self)
        
        #Initialisation des variables
        self.lettresJouee =[]#Historique des lettres jouée
        self.motD = StringVar()#Mot découvert
        self.victoire = StringVar()#Texte affiché en haut (victoire/défaite/Pseudo)
        self.victoire.set("Entrez votre Pseudo : ")
        self.pseudo = StringVar()#Pseudo du joueur
        self.nVictoire = 0 # -1 --> défaite ; 0 --> partie en cours ; 1 --> victoire
        
        
        #Clavier
        self.lettres = [chr(ord('A')+i) for i in range(26)]#liste des lettres
        frameClavier = Frame(self,bg=self.clFond)
        frameClavier.rowconfigure(0, weight=1)
        frameClavier.columnconfigure(0, weight=1)
        self.btLettres = []
        for i in range(len(self.lettres)):
            self.btLettres.append( MonBoutonLettre(self,Button(frameClavier,text=self.lettres[i],width=5),self.lettres[i]))# Initalisation des boutons lettres 
            self.btLettres[i].bt.grid(row=i//7,column= i%7  )#+ (i >= 21)
            self.btLettres[i].bt.config(command=self.btLettres[i].cliquer)
        btRetourArriere = Button(frameClavier,text="<=",width=5)# Bouton retour arrière
        btRetourArriere.grid(row = 3,column=6)
        btRetourArriere.config(command=self.retourArriere)
        
        
        #Initialisation de la fenêtre
        self.za = ZoneAffichage(self,width=400,height =400,bg=self.clCanvas)
        self.restart()
        self.title("Le Pendu")
        self.configure(background=self.clFondFenetre)
        
        
        #Outils
        barreOutils = Frame(self,bg=self.clFond)
        barreOutils.pack(side = TOP,pady = 10)
        
        btNP = Button(barreOutils, text='Nouvelle Partie') #Nouvelle Partie
        btNP.pack(side=LEFT, padx=5, pady=5)
        btNP.config(command=self.restart)
        
        btCouleur = Menubutton(barreOutils,text='Couleur',relief='raised') #Couleur
        btCouleur.menu = Menu(btCouleur, tearoff=0)
        btCouleur['menu'] = btCouleur.menu
        btCouleur.menu.add_command(label='Fond Jeu',command = self.selectCouleurJeu)
        btCouleur.menu.add_command(label='Fond Fenetre',command=self.selectCouleurPrincipale)
        btCouleur.pack(side=LEFT,padx=5,pady=5)
        
        btHistorique = Button(barreOutils,text="Historique") #Historique
        btHistorique.pack(side=LEFT,padx=5,pady=5)
        btHistorique.config(command=self.affHisto)
        
        btQuitter = Button(barreOutils, text='Quitter')  #Quitter
        btQuitter.pack(side=LEFT, padx=5, pady=5)
        btQuitter.config(command=self.destroy)
        
        
        #Victoire/Defaite
        barreInter = Frame(self,bg = self.clFond)
        labelVictoire = Label(barreInter,textvariable=self.victoire,bg = self.clFond)
        labelVictoire.pack(side=LEFT,pady=10,padx=10)
        
        entrePseudo = Entry(barreInter,textvariable = self.pseudo,bg=self.clFond)
        entrePseudo.pack(side=LEFT)
        
        barreInter.pack(side = TOP,pady = 10)
        
        
        #Zone d'affichage
        self.za = ZoneAffichage(self,width=320,height =320,bg=self.clCanvas)
        self.za.pack(side=TOP,pady=10,padx=10)
        
        #Mot
        labelMot = Label(self,textvariable=self.motD,bg=self.clFond)
        labelMot.pack(side=TOP,pady=10,padx=10)
        
        #Clavier
        frameClavier.pack(side=TOP,pady=10)

    
    def affHisto(self):
        
        #Initialisation des couleurs
        clTitre = "#DEDEDE"
        cl1 = "#95BDFF"
        cl2 = "#FF6477"
        
        #Création d'une nouvelle fenetre
        win = Toplevel(self)
        win.config(bg = self.clFondFenetre)
        win.title("Le Pendu Historique")
        
        bdd = BDD("pendu.db")#Initialisation de la base de donnée
        listeBruteJoueur = bdd.retrievePseudo()#On récupère la liste des joueurs
        listeJoueur = []
        for i in listeBruteJoueur:
            listeJoueur.append(i[0])
        
        #Construction des scores moyens et maximums
        scoreMoyens=[]
        scoreMaxs=[]
        for joueur in listeJoueur:
            scoreJ = 0
            scores = bdd.retrieveScore(joueur)
            scoreMax = float(scores[0][0])
            for i in scores:
                scoreJ += float(i[0])
                if float(i[0])>scoreMax:
                    scoreMax = float(i[0])
            scoreMaxs.append(scoreMax)
            scoreMoyens.append(scoreJ/len(scores))
        
        #Affiche le Titre
        labelTitre = Label(win,text="Historique",bg =self.clFond)
        labelTitre.pack(side=TOP)
        
        
        tableau = Frame(win,bg=self.clFond)
        #Affiche les noms
        affNom = Frame(tableau,bg = self.clFond)
        Label(affNom,text="Pseudo",bg=clTitre).pack(side=TOP)
        for ijoueur in range(len(listeJoueur)):
            clAff =cl1
            if ijoueur%2 == 0:
                clAff = cl2
            Label(affNom,text=listeJoueur[ijoueur],bg=clAff).pack(side=TOP)
        affScore = Frame(tableau,bg=self.clFond)
        
        #Affiche les scores moyens
        Label(affScore,text="Score Moyen",bg=clTitre).pack(side=TOP)
        for iscore in range(len(scoreMoyens)):
            clAff =cl1
            if iscore%2 == 0:
                clAff = cl2
            scoreAff = str( int(float(scoreMoyens[iscore])*100)/100 )
            Label(affScore,text=scoreAff,bg=clAff).pack(side=TOP)
        
        #Affiche les scores max
        affScoreM = Frame(tableau,bg=self.clFond)
        Label(affScoreM,text="Score Maximum",bg=clTitre).pack(side=TOP)
        for iscoreM in range(len(scoreMaxs)):
            clAff =cl1
            if iscoreM%2 == 0:
                clAff = cl2
            scoreAff = str( int(float(scoreMaxs[iscoreM])*100)/100 )
            Label(affScoreM,text=scoreAff,bg=clAff).pack(side=TOP)
        
        
        affNom.pack(side=LEFT,padx=5)
        affScore.pack(side=LEFT,padx=5)
        affScoreM.pack(side=LEFT,padx=5)
        tableau.pack(side=TOP)
        
        
    def selectCouleurJeu(self):#Action lorsqu'on appuie sur le bouton Couleur pour le fond du Jeu
        self.clCanvas = colorchooser.askcolor()[1]
        self.za.configure(bg=self.clCanvas)
    
    def selectCouleurPrincipale(self):#Action lorsqu'on appuie sur le bouton Couleur pour le fond de la fenetre
        self.clFondFenetre = colorchooser.askcolor()[1]
        self.configure(background=self.clFondFenetre)
        
    def restart(self):#Action lorsqu'on appuie sur le bouton Nouvelle Partie
        
        for i in range(len(self.lettres)):
            self.btLettres[i].bt.config(state=NORMAL)#réinitialise les boutons lettre
        
        #Choisit un nouveau mot
        self.mot = random.choice(self.f).strip()
        self.motD.set("*"*len(self.mot))
        self.nVictoire = 0
        self.victoire.set("Entrez votre Pseudo : ")
        
        #Réinitialise la potence
        for i in range(len(self.za.lesFormes)):
            self.za.lesFormes[i].setState("hidden")
            self.za.mort= 0
        print(self.mot)
        
    def chargeMots(self):#Chargement des mots
        fichier = open('mots.txt', 'r')
        self.f = fichier.readlines()
        fichier.close()
        
    def traitement(self,lettre):#Action lorsqu'on appuie sur une lettre
        motDecouvert = self.motD.get()
        nouvMot = ""
        trouver = False
        
        #Transforme les * en la lettre dans le mot découvert, et vérifie si on a bien trouvé une lettre
        for i in range(len(self.mot)):
            if self.mot[i] == lettre:
                nouvMot += lettre
                trouver = True
            else:
                nouvMot += motDecouvert[i]
        self.motD.set(nouvMot)
        
        self.lettresJouee.append(lettre)
        if trouver == False:
            rep = self.za.echec()
            if rep == 1:
                print("défaite")
                self.victoire.set("Défaite, réponse :"+self.mot+". Dommage ")
                self.nVictoire = -1
                self.sauvegarderPartie()
        elif self.mot == nouvMot:
            print("victoire")
            self.victoire.set("Victoire ! Bravo ")
            self.nVictoire = 1
            self.sauvegarderPartie()
    
    def sauvegarderPartie(self):#Sauvegarde dans une base de donnée la partie
        print("partie sauvegardée !")
        bdd = BDD("pendu.db")
        pseudoSave = "Invite"
        if self.pseudo.get() != "":
            pseudoSave = self.pseudo.get()
        else:
            self.pseudo.set("Invite")
        bdd.addPartie(pseudoSave,self.mot,(len(self.za.lesFormes)-self.za.mort)/11),#Pseudo mot score
        del(bdd)
    
    def retourArriere(self):#Action lorsqu'on appuie sur le bouton de retour en arrière ( <= )
        if self.nVictoire == 0 and len(self.lettresJouee) > 0:
            derniereLettre = self.lettresJouee.pop()
            
            lettreTrouve = False
            md = self.motD.get()
            nouvmd = ""
            for i in range(len(md)):
                if md[i] == derniereLettre:
                    nouvmd += "*"
                    lettreTrouve = True
                else:
                    nouvmd += md[i]
            self.motD.set(nouvmd)
            
            if lettreTrouve == False: #c'est un coup raté
                self.za.recover()
            self.btLettres[self.lettres.index(derniereLettre)].bt.config(state=NORMAL)
                
                    
                
    
class MonBoutonLettre(Button):
    
    def __init__(self,parent,bouton,nom):
        self.bt = bouton
        self.lettre = nom
        self.parent = parent
        
    def cliquer(self):
        if self.parent.nVictoire == 0:
            self.bt.config(state=DISABLED)
            self.parent.traitement(self.lettre)
        
    
class ZoneAffichage(Canvas):
    
    
    
    def __init__(self, parent, *args,**kwargs):
        self.canvas = Canvas.__init__(self, parent, *args,**kwargs)
        self.lesFormes = []
        
        #Dessin du pendu
        self.lesFormes.append( Rectangle(self,20,290,130,10 ,parent.clFormePotence) )
        self.lesFormes.append( Rectangle(self,55,20,10,270 ,parent.clFormePotence) )
        self.lesFormes.append( Rectangle(self,65,20,100,10 ,parent.clFormePotence) )
        self.lesFormes.append( Rectangle(self,155,30,10,35 ,parent.clFormePotence) )
        self.lesFormes.append( Ellipse(self,160,80,20,20,parent.clFormeHomme) )
        self.lesFormes.append( Rectangle(self,155,90,10,60 ,parent.clFormeHomme) )
        self.lesFormes.append( Rectangle(self,160,110,30,10 ,parent.clFormeHomme) )
        self.lesFormes.append( Rectangle(self,130,110,30,10,parent.clFormeHomme) )
        self.lesFormes.append( Rectangle(self,140,150,40,10 ,parent.clFormeHomme) )
        self.lesFormes.append( Rectangle(self,140,160,10,30 ,parent.clFormeHomme) )
        self.lesFormes.append( Rectangle(self,170,160,10,30 ,parent.clFormeHomme) )
        
        self.mort = 0

    def echec(self):#Executer lorsqu'on selectionne une lettre qui n'est pas dans le mot mystère
        
        if self.mort < len(self.lesFormes):#Si on n'est pas pendu totalement
            self.lesFormes[self.mort].setState("normal")#Affiche la prochaine partie du pendu
            self.mort += 1#Incrémente
        
        if self.mort >= len(self.lesFormes):#Cette fonction renvoie 1 si la partie est fini (et que le pendu est donc complet), 0 sinon
            return 1
        else:
            
            return 0
    
    def recover(self):#Restore d'une étape
        self.mort -= 1
        self.lesFormes[self.mort].setState("hidden")


if __name__ == "__main__":
    fen = FenPrincipale()
    fen.mainloop()