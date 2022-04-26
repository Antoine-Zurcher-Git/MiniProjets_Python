**Sommaire**

[[_TOC_]]

# BE #3 : Base de données SQL



L'objectif de ce BE est d'expérimenter la manipulation (créer, lire, interroger, modifier) de bases de données relationnelles avec le langage SQL (*Structured Query Language*), à partir de _Python_. Ce BE est décomposé en trois parties:

  1. **La première partie** (durée: 45 min.) présente quelques commandes élémentaires pour interroger une base _SQL_ à partir de _Python_;
  1. **La seconde partie** (durée: 75 min.) permet de découvrir comment manipuler une base de données _SQL_ en _Python_ orienté objet. L'énoncé est rédigé sous une forme tutoriel;    
  1. **La troisième partie** (durée: 120 min. et +) vous amène à un travail plus personnalisé, pour mettre à profit vos connaissances sur la gestion des exceptions, la librairie graphique *matplotlib* et bien sûr les bases de données _SQL_.

Ce BE fera l'objet d'un compte-rendu (CR), seul ou en binôme. Avant de commencer, veuillez prendre connaissance des consignes concernant le rendu du travail (à respecter scrupuleusement) qui se trouvent dans le fichier [consignes_BE#3.md](./consignes_BE#3.md) (dans le même répertoire que cet énoncé).

--- 
## 1. Mini-tutoriel sur la base Hotellerie.db (45 min.)

Le système de gestion de base de données qui sera utilisé durant ce BE est _SQLite_. Ce système très simple fonctionne en stockant une base de données dans un fichier d'extension _.sqlite_. La base de tests utilisée dans cette partie (_hotellerie.db_) est disponible au même endroit que cet énoncé. Son schéma est le suivant :

<center><img src="figures/schema_bdd_hotellerie.png" style="width:60%"/></center>

La base est composée de 5 tables, ces tables étant composées d'un nombre variable de champs. Les champs soulignés représentent les clés primaires (ou *primary key (PK)* en anglais). En particulier, la clé primaire de la table **chambre** est composée des attributs *numchambre* et *numhotel* (cette dernière étant la clé primaire de la table **hotel**).
 

*Remarque* : Vous trouverez [ici, une vidéo](https://www.youtube.com/watch?v=VgTRNqn2fn0) qui montre comment utiliser [draw.io](https://app.diagrams.net) pour créer un diagramme entité-association. Il NE vous est PAS demandé de dessiner le diagramme de cette base de données.


### 1.1 DB browser for SQLite (30 min.)

Toutes les opérations sur une base de données de ce type peuvent être effectuées en _Python_ via les classes et les méthodes  présentes au sein du module _sqlite3_. Pour manipuler de manière interactive le contenu de la base (créer, supprimer ou modifier des tables et des enregistrements, effectuer des requêtes _SQL_...), il existe des outils adaptés. L'outil retenu dans le cadre de ce BE s'appelle ``DB Browser for SQLite``. C'est un logiciel libre qui existe pour toutes les plate-formes : Windows, MacOs, nombreuses distributions Linux et Unix...

 - Téléchargez et installez [DB Browser for SQLite](https://sqlitebrowser.org/) en suivant les instructions d'installation en fonction de votre système d'exploitation.    
 - Ouvrez la base *hotellerie.db* et naviguez dans les tables (onglet ``Structure de la Base de Données``) et les enregistrements (onglet ``Parcourir les données``) pour prendre connaissance de la base (telle qu'elle est schématisée ci-dessus).

<center><img src="figures/DBBrowser.png" style="width:75%"/></center>

 - Dans l'onglet ``Exécuter le SQL``, lancez la requête suivante   
```SQL
SELECT nom, ville
FROM hotel;
```  
La réponse apparaît sous forme de 12 lignes. Ça vous rappelle des choses ? Si non, alors voici quelques pointeurs pour vous rafraîchir la mémoire :    
    - [cours tutoriel sur SQL](https://www.1keydata.com/fr/sql/)  
    - [SQL : sélection, jointure, regroupement, filtre](http://cerig.pagora.grenoble-inp.fr/tutoriel/bases-de-donnees/chap20.htm)
    - et tant d'autres...



### 1.2 Quelques requêtes en _Python_ (15 min.)

**Attention** Avant de lancer un requête sur la bdd avec _Python_, il est fortement conseillé de fermer ``DB Browser for SQLite``, sinon vous pourriez soit avoir un plantage de votre programme, soit détruire la bdd (auquel cas il vous suffirait de la télécharger à nouveau).

Nous allons à présent chercher à reproduire la requête ci-dessus en utilisant _Python_ et le package  _sqlite3_.  C'est une librairie objet dont la [documentation](https://docs.python.org/3/library/sqlite3.html#module-sqlite3) fournit une description des classes et des méthodes disponibles. Suivez le guide...

Le squelette typique d'un tel programme s'écrit : 
```python
import sqlite3
if __name__ == '__main__':
	conn = sqlite3.connect('hotellerie.db') # connexion à la bdd
	# travail sur la bdd à partir du connecteur
	conn.commit()                           # pour enregistrer les éventuels changements 
	conn.close()                            # pour fermer proprement l'accès à la base
```

Ainsi, pour obtenir la réponse à la requête précédente :
```python
import sqlite3
if __name__ == '__main__':
	conn = sqlite3.connect('hotellerie.db')

	curseur = conn.cursor()                          # objet permettant de faire des requêtes
	curseur.execute("SELECT nom, ville FROM hotel;") # requête SQL
	ligne1 = curseur.fetchone()                      # 1ère ligne résultat de la requête
	print('ligne1 =', ligne1)
	ligneAll = curseur.fetchall()                    # toutes les lignes de la requête
	print('ligneAll =', ligneAll)

	conn.close() 
```

_Remarque_ La commande ```conn.commit()``` n'est pas nécessaire ici puisque le script ne modifie pas la base.

Copiez et exécutez ce programme ; le résultat se présente sous forme d'un tuple, ou sous forme d'une liste de tuples. Ainsi la commande suivante imprime le nom du premier hôtel qui apparaît dans la liste des résultats de la requête :
```python
print(ligneAll[0][0])
```

Voici un usage intéressant à étudier :
```python
import sqlite3
if __name__ == '__main__':
	conn = sqlite3.connect('hotellerie.db')

	curseur = conn.cursor()  
	for ligne in curseur.execute("SELECT * FROM hotel WHERE etoiles=3"):
		print('ligne=', ligne)
	
	conn.close() 
```

---
## 2. Classe HotelDB (75 min.)

Il s'agit de créer une classe **HotelDB** permettant de réaliser un certain nombre de requêtes et de mises à jour de la base *Hotellerie.db*. 

### 2.1 Requête en lecture (30 min.)

Dans un fichier *HotelDB.py*, commencez à développer la classe permettant de répondre au programme principal suivant, dont l'objectif est d'afficher le nom des hôtels 2 étoiles (notez que le nombre d'étoiles est passé en argument) :
 ```python
 if __name__ == '__main__':
	aHotelDB =  HotelDB('hotellerie.db')
	resultat = aHotelDB.get_name_hotel_etoile(2)
	print("Liste des noms d'hotel 2 étoiles : ", resultat)
 ```

Il s'agit ici de développer le constructeur (qui stockera le connecteur en tant qu'attribut) et la méthode _get_name_hotel_etoile(...)_.

*Remarque* : Pour fermer correctement l'accès à la base de donnée, pensez à implémenter la méthode ```__del__(self)``` (vue en cours), qui est appelée automatiquement par _Python_ lors de la destruction des objets de la classe. Typiquement :
```python
def __del__ (self):
	self.__conn.close() 
```

__Améliorations à implémenter__ : Comment se comporte votre programme si on insère la commande `aHotelDB.get_name_hotel_etoile(-1)` ? Et la commande `aHotelDB.get_name_hotel_etoile("Hello")`. Comment éviter que cet usage ne produise la fin brutale du programme et qu'il renvoie une liste vide tout simplement ? 


### 2.2 Requête en écriture (45 min.)

Créer une requête permettant d'ajouter un nouveau client. Si le client existe déjà (même nom ET même prénom), la méthode renverra le numéro de ce client. Si le client n'existe pas, alors la méthode créera un nouveau client, en lui adjoignant le premier numéro non encore utilisé (c'est une clé primaire !). Pour cela, renseignez-vous sur la commande ``INSERT INTO``. Vérifier que le nouveau client a bien été sauvegardé dans le fichier *Hotellerie.db* :

  - soit en consultant la base avec `DB Browser for SQLite`;
  - soit en exécutant par 2 fois le même programme, vous devriez retrouver le même numéro de client.


---
## 3. Requêtes libres (120 min. et +)

Dans cette dernière partie, nous vous invitons à imaginer et implémenter **DEUX (2)** requêtes originales à partir de la bdd *Hotellerie.db*, ou de tout autre bdd que vous aurez trouvée sur Internet. Voici quelques exemples de sites proposant des bdd _SQLite_ gratuites :

  - Le site [SQLite tutorial](https://www.sqlitetutorial.net/sqlite-sample-database/) propose un base de données appelée _chinook_ (_digital media store_), composée de 11 tables.
  - Dans le même genre, une abse de données très célèbre [Northwind](https://cs.ulb.ac.be/public/_media/teaching/infoh303/northwind_sqlite.db.zip) (8 tables)
  - Si vous êtes fan des _Pokémon_, vous pouvez décompresser la base [veekun's Pokédex](http://veekun.com/static/pokedex/downloads/veekun-pokedex.sqlite.gz) (172 tables).
  - Si vous êtes fan de musique, vous pouvez décompresser et utiliser la base [musicBrainz](https://matthieu-moy.fr/cours/infocpp-S3/TPL/musicBrainz.zip) (4 tables).
  - Une petite base concernant la peinture : [peinture.db](https://carnot.cpge.info/wp-content/uploads/2020/02/peinture.db)
  - [murder-mystery](https://forge.univ-lyon1.fr/diu-eil/bloc4/-/raw/master/3_bases_de_donnees_introduction/TP/base-sql-murder-mystery.db) (9 tables). Lire le [site original](https://github.com/NUKnightLab/sql-mysteries).
  - [postuler à Stanford](https://forge.univ-lyon1.fr/diu-eil/bloc4/-/raw/master/3_bases_de_donnees_introduction/TP/base-stanford.db) (3 tables).

Vous pouvez également transformer des données du format `.csv` (_Comma Separated Value_) vers le format `.sqlite3`, en suivant ce [tutoriel video](https://tube.ac-lyon.fr/videos/watch/85399ea5-bba0-428b-9470-2d3bb41b7de1). Toutes les données de [data.gouv.fr](https://www.data.gouv.fr/fr/), par exemple, deviennent alors exploitables pour votre CR...

Au cas où vous opteriez pour une bdd originale, n'oubliez pas d'inclure cette base dans votre archive (si elle n'est pas trop volumineuse), et de préciser dans votre rapport le chemin pour la télécharger.

**Quelques conseils**:

* Si vous optez pour la bdd `HotelDB`, n'hésitez pas à visiter un site de réservation d'hôtels pour trouver des idées de requêtes intéressantes. _Attention_ : le nom d'un hôtel n'est pas une clé primaire ! Plusieurs hôtels portent le même nom. Par contre, il n'existe pas 2 hôtels de même nom dans la même ville. Pensez-y !
* Si vous optez pour une autre base, développer une seconde classe dans un second fichier (sur le modèle de la classe **HotelDB**).

Les deux requêtes attendues doivent être relativement sophistiquées (pas de simples ``select ... from``), l'évaluation de cette partie dépendra :

 1. de l'originalité de vos requêtes,    
 1. de la valorisation graphique des résultats de vos requêtes à l'aide de la librairie **matplotlib**,   
 1. de la robustesse de vos requêtes à des usages erronés ou inattendus (usage des exceptions). _Par exemple_ : comment se comporte la requête si le nom de l'hôtel passé en argument n'existe pas dans la base ? Vous pouvez "prouver" la robustesse de vos requêtes en proposant une série de _crash-tests_.
 1. de leur présentation dans le rapport.

Votre programme principal doit contenir plusieurs appels à chaque requête (en changeant les arguments), de manière à illustrer leur robustesse dans des cas de figure différents (_p. ex._ hôtel ou ville inconnue).

**Remarques** : 

- Vous programmerez les représentations graphiques dans le programme principal (et non pas dans la méthode qui traite la requête). En effet, quand on fait une requête sur une base de données, l'affichage graphique ne doit pas être obligatoire. C'est pour cela qu'on sépare la requête de l'affichage de son résultat (qu'il soit au format texte ou au format graphique).     
- Usage de __Matplotlib__ : À titre d'exemples, vous trouverez, à côté de cet énoncé, un fichier nommé [ex_matplotlib.py](./ex_matplotlib.py). L'exécution de ce script génère 4 figures dans le sous-répertoire *figures*. Inspirez-vous largement de ce programme pour vos propres figures. *Conseil*: Évitez de vous lancer dans des requêtes avec des données géographiques, genre ```trouver tous les hôtels à moins de 5 kilomètres``` car l'usage de cartes géographiques dépasse les attentes de ce qui est demandé ici.
