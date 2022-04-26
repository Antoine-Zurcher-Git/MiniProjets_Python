

import sqlite3
import matplotlib.pyplot as plt
import numpy             as np


#DELETE * FROM *

class Pokedex:
        
    def __init__(self,nom):
        self.__conn = sqlite3.connect(nom)
        
    
    def __del__(self):
        self.__conn.close()
        
    def pokemonOfType(self,typePkm):
        """Principe : renvoie la liste du nom des pokémons du type en argument
        Argument : type recherché, par exemple 'water'"""
        if type(typePkm) != str:#Le type doit être une variable de type String
            raise TypeError
        curseur = self.__conn.cursor()
        curseur.execute("SELECT identifier FROM pokemon WHERE id IN (SELECT pokemon_id FROM pokemon_types WHERE type_id IN (SELECT id FROM types WHERE identifier = ?));",(typePkm,))#Execute la requête SQL
        return curseur.fetchall()
    
    
    
    def pokemonOfGeneration(self,gen):
        """Principe : renvoie la liste du nom des pokémons de la génération en argument
        Argument : génération recherchée, par exemple 1"""
        if type(gen) != int:#La génération doit être une variable de type Integer
            raise TypeError
        if gen < 1 or gen > len(self.allGeneration()):#Si la génération en requète n'existe pas, on renvoie une liste vide
            return []
        if gen > 1:#Si ce n'est pas la première génération
            curseur = self.__conn.cursor()
            curseur.execute("SELECT identifier FROM pokemon WHERE id IN (SELECT pokemon_form_id FROM pokemon_form_generations WHERE generation_id = ?) and id NOT IN (SELECT pokemon_form_id FROM pokemon_form_generations WHERE generation_id = ?);",(gen,gen-1))
            return curseur.fetchall()
        else:#Si c'est la première génération
            curseur = self.__conn.cursor()
            curseur.execute("SELECT identifier FROM pokemon WHERE id IN (SELECT pokemon_form_id FROM pokemon_form_generations WHERE generation_id = ?);",(gen,))
            return curseur.fetchall()
    
    def allGeneration(self):
        """Principe : renvoie la liste du nom des générations"""
        curseur = self.__conn.cursor()
        curseur.execute("SELECT identifier FROM generations")
        return curseur.fetchall()
        
    def nameType(self):
        """Principe : renvoie la liste des différents types"""
        curseur = self.__conn.cursor()
        curseur.execute("SELECT identifier FROM types")
        return curseur.fetchall()
        
        
if __name__ == '__main__':

    pokedex = Pokedex('veekun-pokedex.sqlite')#Créé un objet de type Pokedex
    
    typeCouleur = ["lightgray","brown","c","purple","saddlebrown","sandybrown","greenyellow","rebeccapurple","gray","red","royalblue","forestgreen","yellow","magenta","turquoise","darkblue","black","pink"]# Couleurs pour colorer les différents type (par exemple le type eau est en bleu)
    
    ##Camembert des types
    nomsType = pokedex.nameType()#Nom des types
    labels = []#Nom des types dans le bon format
    nbPokemon = []#Nombre de pokémon de chaque type
    for i in range(len(nomsType)-2):#-2 car 2 type sont 'spéciaux' et on ne les comptes donc pas
        nbPokemon.append(len( pokedex.pokemonOfType(nomsType[i][0]) ))#Ajoute le nombre de pokemon de ce type
        labels.append( nomsType[i][0] )#Et le nom du type

    fig1, ax1 = plt.subplots()
    ax1.pie(nbPokemon, labels=labels, startangle=90,colors = typeCouleur)#Créé le camembert
    ax1.axis('equal')
    plt.title("Répartition des types dans pokemon")#Titre
    plt.show()
    
    ##Camembert des types en génération 2
    nomsType = pokedex.nameType()#De la même manière que pour le premier Camembert
    labels = []
    nbPokemon = []
    for i in range(len(nomsType)-2):#-2 car 2 type sont 'spéciaux' et on ne les comptes donc pas
        pkmDeType = pokedex.pokemonOfType(nomsType[i][0])#Liste des pokémon du type n°i
        pkmDeGen = pokedex.pokemonOfGeneration(2)#Liste des pokémon de seconde génération
        pkmDeTypeEtDeGen = []#On créé une liste des pokémon de deuxième génération du type n°i
        for k in pkmDeType:
            if k in pkmDeGen:
                pkmDeTypeEtDeGen.append(k)
        
        nbPokemon.append(len( pkmDeTypeEtDeGen ))
        labels.append( nomsType[i][0] )

    fig1, ax1 = plt.subplots()
    ax1.pie(nbPokemon, labels=labels, startangle=90,colors = typeCouleur)
    ax1.axis('equal')
    plt.title("Répartition des types dans la génération 2")
    plt.show()
    

    ##Histogramme
    generations = pokedex.allGeneration()
    genera = []
    
    # for i in range(len(generations)):

    #     for k in range((nbPkm[i])):
    #         genera.append(i+1)
            
    plt.title("Nombre de Pokémon par génération")
    plt.xlabel("Generation")
    plt.ylabel("Nombre de Pokémon")
    plt.hist(genera,bins=[0.6,1.4,1.6,2.4,2.6,3.4,3.6,4.4,4.6,5.4,5.6,6.4])
    plt.axis([0,7,0,200])
    plt.show()
    
    ##Tests :
    
    assert pokedex.pokemonOfType("normal)); DELETE * FROM * ((") == [] #Ne supprime pas la bdd
    assert pokedex.pokemonOfType("Ceci n'est pas un type") == []
    try:
        pokedex.pokemonOfType(666)
    except TypeError as msg:
        print("Type Error")
     
    
    assert pokedex.pokemonOfGeneration(-1) == []
    try:
        pokedex.pokemonOfGeneration("Pokemon")
    except TypeError as msg:
        print("Type Error")


        
        
        