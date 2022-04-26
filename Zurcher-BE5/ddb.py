

import sqlite3

class BDD:
    
    def __init__(self,nom):
        self.__conn = sqlite3.connect(nom)
    
    def __del__(self):
        self.__conn.close()
    
    def addPartie(self, pseudo, mot, score):
        try:
            curseur = self.__conn.cursor()
            curseur.execute(f"SELECT jo.idjoueur FROM Joueur AS jo WHERE jo.pseudo = '{pseudo}';")
            idjoueur = 0
            l = curseur.fetchall()
            if len(l) > 0:
                idjoueur = l[0][0]
            else:
                curseur.execute(f"SELECT MAX(jo.idjoueur) FROM Joueur AS jo;")
                
                idjoueur = curseur.fetchall()[0][0]+1
                
                curseur.execute(f"INSERT INTO Joueur VALUES ({idjoueur},'{pseudo}');")
            
            curseur.execute(f"SELECT MAX(pa.idpartie) FROM Partie AS pa;")
            idpartie = curseur.fetchall()[0][0]+1
            curseur.execute(f"INSERT INTO Partie VALUES ({idpartie},{idjoueur},'{mot}',{score});")
            self.__conn.commit()
        except sqlite3.OperationalError as err:                               
            print('Erreur SQL : ', str(err))
    
    def retrieveScore(self, pseudo):
        try:
            curseur = self.__conn.cursor()
            curseur.execute(f"SELECT pa.score FROM Partie AS pa JOIN Joueur AS jo ON jo.idjoueur=pa.idjoueur WHERE jo.pseudo = ?;",(pseudo,))
            
            return curseur.fetchall()
        except sqlite3.OperationalError as err:                               
            print('Erreur SQL : ', str(err))
    def retrievePseudo(self):
        try:
            curseur = self.__conn.cursor()
            curseur.execute(f"SELECT pseudo FROM Joueur")
            return curseur.fetchall()
        except sqlite3.OperationalError as err:
            print('Erreur SQL : ',str(err))


    