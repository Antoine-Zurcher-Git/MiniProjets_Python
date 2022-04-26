# Avril 20 21
# ATTENTION : changement par rapport à la version S5

# Nov 20-21 : qq petite modif p/r à la version 2019
# En 20-21, l'ordre des questions a changé
# Contient le srép aux questions de la partie 2 (mais dépend de la partie 1)
#--------------------------------------------------------
# Nov 2019 : ma version de TD3 (image) séance 2
# J'ai fait qq modifs, ajouté main (bordel !)
# ET ajouté des tests pour chaque partie.
# Les résultats sont pas mal. Surtout après Ex 2.3 (lancer et regarder les prompts sur input.)

from math import sqrt, log10
from PIL import Image
from sys import argv, stdin

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import random

def put_color_into_matrice_pixels(coin_x, coin_y, width, height, color):
    global matrice_pixels # pas besoin mais pour le cas où !
    for i in range(coin_x, coin_x + width):
        for j in range(coin_y, coin_y + height):
            matrice_pixels[i, j] = color

#-----------------------------------------------------------------------
def moyenne_couleurs(coin_x, coin_y, width, height):
    global matrice_pixels # pas besoin mais pour le cas où !
    sr, sg, sb = 0, 0, 0
    for i in range(coin_x, coin_x + width):
        for j in range(coin_y, coin_y + height):
            r, g, b = matrice_pixels[i, j]
            sr += r
            sg += g
            sb += b
    a = width * height
    a+=10**-7 # ALEX pour éviter div par 0
    return sr / a, sg / a, sb / a
#-----------------------------------------------------------------------
def ecart_type_couleurs(coin_x, coin_y, width, height):
    global matrice_pixels # pas besoin mais pour le cas où !
    ar, ag, ab = moyenne_couleurs(coin_x, coin_y, width, height)
    sr, sg, sb = 0, 0, 0
    for i in range(coin_x, coin_x + width):
        for j in range(coin_y, coin_y + height):
            r, g, b = matrice_pixels[i, j]
            sr += (r - ar) ** 2
            sg += (g - ag) ** 2
            sb += (b - ab) ** 2
    a = width * height
    a+=10**-7 # ALEX pour éviter div par 0
    return sqrt(sr / a), sqrt(sg / a), sqrt(sb / a)
#===========================================================
# Exercice 2.1 (du S5 du 20-21)
#  Etendre le code de l’arbre ci-dessous afin qu’il corresponde à l’abre de la figure 2
#========================================================s===
class Noeud:
    def __init__(self, coin_x, coin_y, width, height, haut_gche, haut_dte, bas_gche, bas_dte, color):
        self.coin_x = coin_x
        self.coin_y = coin_y
        self.width = width
        self.height = height
        self.haut_gche = haut_gche # Le quart haut gauche
        self.haut_dte = haut_dte   # Le quart haut droite
        self.bas_gche = bas_gche
        self.bas_dte = bas_dte
        self.color = color # Le triplet
        enfants=[haut_gche, haut_dte, bas_gche, bas_dte]
        self.enfants=[e for e in enfants if e] # On prend les enfants := None
        self.nb_enfants=len(self.enfants)

    # renvoie une string decrivant le Noeud et tous ses enfants
    def __repr__(self , depth =0):
        tabs = "\t" * depth
        line = f"{tabs}{{x={self.coin_x}, y={self.coin_y}, w={self.width}, h={self.height}, \
            couleur={self.color}}}"
        lines = (line,*(e.__repr__(depth +1) for e in self.enfants))
        return "\n".join(lines)
 

        
"""
Version S6 : par rapport à la Version S5 du 20-21, le seule changement est 
le triplet des couleurs. Ici, le nom de la couleur.
racine = Noeud(0, 0, 4, 4, 128, 128, 128,
            Noeud(0, 0, 2, 2, 255, 255, 255, None, None, None, None),
            Noeud(2, 0, 2, 2, 128, 128, 128,
                Noeud(2, 0, 1, 1, 128, 128, 128, None, None, None, None),
                Noeud(3, 1, 1, 1, 128, 128, 128, None, None, None, None),
                Noeud(3, 0, 1, 1, 0,   0,   0,   None, None, None, None),
                Noeud(2, 1, 1, 1, 0, 0, 0, None, None, None, None)),
            Noeud(2, 2, 2, 2, 128, 128, 128,
                Noeud(2, 3, 1, 1, 128, 128, 128, None, None, None, None),
                Noeud(3, 3, 1, 1, 128, 128, 128, None, None, None, None),
                Noeud(2, 2, 1, 1, 255, 255, 255, None, None, None, None),
                Noeud(3, 2, 1, 1, 255, 255, 255, None, None, None, None)),
            Noeud(0, 2, 2, 2,0,0, 0, None, None, None, None))

"""
#===========================================================
# Exercice 2.1 (S6 du 20-21)
# En utilisant des instances de cette classe, complétez le code des 5 premiers noeuds
# ci-dessous pour décrire l’arbre représenté en figure 2.
# ............
"""
Version S5 du 20-21 : (par rapp à l aversion S6), le seule changement est le triplet des couleurs
Ici, le nom de la couleur.
racine = Node(0, 0, 4, 4, ’grey’,                                                       1
                Node(0, 0, 2, 2, ’white’, None, None, None, None),                      2
                Node(2, 0, 2, 2,’grey’,                                                 3
                    Node(2, 0, 1, 1, ’grey’, None, None, None, None),                   4
                    Node(3, 0, 1, 1, ’black’, None, None, None,None),                   5
                    Node(2, 1, 1, 1, ’black’, None, None, None, None),                  6
                    Node(3, 1, 1, 1, ’grey’, None, None,None, None)                     7
                    ), 
                Node(0, 2, 2, 2, ’black’, None, None, None, None),                      8
                Node(2, 2, 2, 2, ’grey’,                                                9
                    Node(2, 2, 1, 1, ’white’, None, None, None, None),                  10
                    Node(3, 2, 1, 1, ’white’, None, None, None, None),                  11
                    Node(2,3, 1, 1, ’grey’, None, None, None, None),                    12
                    Node(3, 3, 1, 1, ’grey’, None, None, None, None)                    13
                    )
            )

                                                      1
                            --------------------------|------------------------------
                            |                 |                 |                    |
                            2                 3                 8                    9
                                       -------|-------                         ------|-------- 
                                       |   |    |    |                         |   |    |    |      
                                       4   5    6    7                        10   11   12  13

"""
#===========================================================
# Exercice 2.2 (S6 2021)
"""
Exercice 2.2 – Créez une fonction qui récupère en entrée une portion de l’image (représentée par
un rectangle) ainsi qu’un seuil d’homogénéité, et renvoie le Noeud correspondant. Si les pixels de
la portion sont homogènes, le Noeud sera terminal (pas d’enfant) et sa couleur sera la moyenne des
pixels de la portion. S’ils ne sont pas homogènes, le Noeud aura au plus 4 enfants, résultats de
l’appel récursif de la fonction sur la quadripartition générée à l’exercice 1.5. Le Noeud sera donc
non-terminal, et sa couleur pourra être fixée à une valeur arbitraire (sans importance).
"""
#=========================================================

def creation_regions_V1(coin_x, coin_y, width, height, seuil):
    global nb_regions

    #nb_regions=nb_regions+1-1 # pour manipuler la variable (l'initialiser une var globale)
    #if width == 0 or height == 0:
        #return None
    if width*height < 4 :
        nb_regions += 1
        return
    
    elif sum(ecart_type_couleurs(coin_x, coin_y, width, height))/3 < seuil:
        nb_regions += 1
        return Noeud(coin_x, coin_y, width, height, None, None, None, None, 
                     tuple(map(int, moyenne_couleurs(coin_x, coin_y, width, height))))
    else:
        nb_regions += 4
        haut_gche = creation_regions_V1(coin_x, coin_y, width // 2, height // 2, seuil)
        haut_dte = creation_regions_V1(coin_x + width // 2, coin_y, width - width // 2, height // 2, seuil)
        bas_gche = creation_regions_V1(coin_x, coin_y + height // 2, width // 2, height - height // 2, seuil)
        bas_dte = creation_regions_V1(coin_x + width // 2, coin_y + height // 2, width - width // 2, 
                                      height - height // 2, seuil)
        return Noeud(coin_x, coin_y, width, height, haut_gche, haut_dte, bas_gche, bas_dte, None)
#------------------------------------------
# Cette version est comme creation_regions_V1 mais renvoie en plus nb_regions créés (plus de nb_regions en globale)
def creation_regions_V1_renvoie_nb_regions(coin_x, coin_y, width, height, seuil):

    #if width == 0 or height == 0:
        #return None
    if width*height < 4 :
         return None,1
    
    elif sum(ecart_type_couleurs(coin_x, coin_y, width, height))/3 < seuil:
        return Noeud(coin_x, coin_y, width, height, None, None, None, None, 
                     tuple(map(int, moyenne_couleurs(coin_x, coin_y, width, height)))),1 # 1 pour nb_regions
    else:
        haut_gche, nb_reg1 = creation_regions_V1_renvoie_nb_regions(coin_x, coin_y, width // 2, height // 2, seuil)
        haut_dte, nb_reg2 = creation_regions_V1_renvoie_nb_regions(coin_x + width // 2, coin_y, width - width // 2, height // 2, seuil)
        bas_gche, nb_reg3 = creation_regions_V1_renvoie_nb_regions(coin_x, coin_y + height // 2, width // 2, height - height // 2, seuil)
        bas_dte, nb_reg4 = creation_regions_V1_renvoie_nb_regions(coin_x + width // 2, coin_y + height // 2, width - width // 2, 
                                      height - height // 2, seuil)
        return Noeud(coin_x, coin_y, width, height, haut_gche, haut_dte, bas_gche, bas_dte, None),\
            nb_reg1+nb_reg2+nb_reg3+nb_reg4

#===============================================================================
# Exercice 2.4 (20-21)
# Parcourt les enfants de node, et peint sur l'image "im" tous les noeuds terminaux
#===========================================================
def apply_node_color_to_his_region_in_mat_pixels(node):
    if not node :
         return
    if node.color != None:
        put_color_into_matrice_pixels(node.coin_x, node.coin_y, node.width, node.height, node.color)
    else:
        apply_node_color_to_his_region_in_mat_pixels(node.haut_gche)
        apply_node_color_to_his_region_in_mat_pixels(node.haut_dte)
        apply_node_color_to_his_region_in_mat_pixels(node.bas_gche)
        apply_node_color_to_his_region_in_mat_pixels(node.bas_dte)

#===========================================================
# Exercice 2.4 ? (20-21)
# Parcourt les enfants de node, et peint en couleur  chaque noeud terminal

# 20 x 20 x 20 fait du gris .....?
#===========================================================
def apply_a_color_aux_noeuds_terminaux_de_l_arbre(color_to_apply, node):
    if not node :
         return    
    #light_gray=128 #211
    
    if node.color != None:
        r,g,b=color_to_apply
        #put_color_into_matrice_pixels(node.coin_x, node.coin_y, node.width, node.height, (facteur * depth, facteur * depth, facteur * depth))
        print('on applique la couleur à W x H : ', node.width, node.height)
        put_color_into_matrice_pixels(node.coin_x, node.coin_y, node.width, node.height, color_to_apply)
    else:
        apply_a_color_aux_noeuds_terminaux_de_l_arbre(color_to_apply, node.haut_gche)
        apply_a_color_aux_noeuds_terminaux_de_l_arbre(color_to_apply, node.haut_dte)
        apply_a_color_aux_noeuds_terminaux_de_l_arbre(color_to_apply, node.bas_gche)
        apply_a_color_aux_noeuds_terminaux_de_l_arbre(color_to_apply, node.bas_dte)
#===========================================================
# Exercice 2.5 ? (20-21)
# Parcourt les enfants de node, et peint en niveaux de gris la profondeur de chaque noeud terminal
# 20 x 20 x 20 fait du gris .....?
#===========================================================
def apply_a_color_a_la_matrice_selon_niveau_de_l_arbre(color_to_apply, node, depth):
    if not node :
         return    
    #light_gray=128 #211
    
    if node.color != None:
        r,g,b=color_to_apply
        #put_color_into_matrice_pixels(node.coin_x, node.coin_y, node.width, node.height, (facteur * depth, facteur * depth, facteur * depth))
        print('on applique la couleur à W x H : ', node.width, node.height)
        put_color_into_matrice_pixels(node.coin_x, node.coin_y, node.width, node.height, ((r*depth) % 255, (g*depth)%255 , (g*depth)%255))
    else:
        apply_a_color_a_la_matrice_selon_niveau_de_l_arbre(color_to_apply, node.haut_gche, depth + 1)
        apply_a_color_a_la_matrice_selon_niveau_de_l_arbre(color_to_apply, node.haut_dte, depth + 1)
        apply_a_color_a_la_matrice_selon_niveau_de_l_arbre(color_to_apply, node.bas_gche, depth + 1)
        apply_a_color_a_la_matrice_selon_niveau_de_l_arbre(color_to_apply, node.bas_dte, depth + 1)
#===========================================================
# Exercice 2.6  (2021)
#===========================================================
def Err_quadratique(node):
    global matrice_pixels # pas besoin mais pour le cas où !
    if not node :
         return 0    
    if node.color != None:
        sum = 0
        r, g, b = node.color
        for coin_x in range(node.coin_x, node.coin_x + node.width):
            for coin_y in range(node.coin_y, node.coin_y + node.height):
                r0, g0, b0 = matrice_pixels[coin_x, coin_y]
                sum += (r - r0)**2 + (g - g0)**2 + (b - b0)**2
        return sum
    else:
        return Err_quadratique(node.haut_gche) + Err_quadratique(node.haut_dte) + \
               Err_quadratique(node.bas_gche) + Err_quadratique(node.bas_dte)

def PSNR(node):
    #print(f"PSNR : Err_quadratique(node) : {Err_quadratique(node)}, node.width : {node.width}, node.height : {node.height}")
    print(f"Dans PSNR : Err_quadratique(node) : {Err_quadratique(node)}")

    # ALEX : j'ajoute 10**-6 au cas où EQ=0 qui posera pb avec log 
    return 20 * log10(255) - 10 * log10((Err_quadratique(node)+10**-6) / 3 / node.width / node.height)

#===========================================================
# Exercice ??
# Parcourt les enfants de node, et fait un print pour chaque noeud terminal
#===========================================================
def tracer(node, niveau):
    if not node :
         return    
    if node.color != None:
        color = node.color
        print(' '*niveau, niveau, ' : ', node.coin_x, node.coin_y, node.width, node.height, color[0], color[1], color[2])
    else:
        tracer(node.haut_gche, niveau+1)
        tracer(node.haut_dte, niveau+1)
        tracer(node.bas_gche, niveau+1)
        tracer(node.bas_dte, niveau+1)


#===========================================================
# Exercice 2.3 bis
# Renvoie la racine d'une quadripartition englobant la zone donnee, avec une
# limite de noeuds terminaux. A chaque etape on repartit les noeuds a allouer
# en fonction de la complexite de chaque quart
#===========================================================
def creation_regions_V2(coin_x, coin_y, width, height, limite_nb_feuilles):
    # TRACE : 
    # print(coin_x, coin_y, width, height)
    if limite_nb_feuilles < 4 or width == 1 or height == 1:
        return Noeud(coin_x, coin_y, width, height, None, None, None, None, 
                     tuple(map(int, moyenne_couleurs(coin_x, coin_y, width, height))))
    else:
        deviation_haut_gche = max(sum(ecart_type_couleurs(coin_x, coin_y, width // 2, height // 2)), 0.001)
        deviation_haut_dte = max(sum(ecart_type_couleurs(coin_x + width // 2, coin_y, width - width // 2, height // 2)), 0.001)
        deviation_bas_gche = max(sum(ecart_type_couleurs(coin_x, coin_y + height // 2, width // 2, height - height // 2)), 0.001)
        deviation_bas_dte = max(sum(ecart_type_couleurs(coin_x + width // 2, coin_y + height // 2, width - width // 2, 
                                         height - height // 2)), 0.001)
        nb_feuilles_haut_gche = min(max(int(round(limite_nb_feuilles * deviation_haut_gche / 
                                (deviation_haut_gche + deviation_haut_dte + deviation_bas_gche + deviation_bas_dte))), 1), 
                                    limite_nb_feuilles - 3)
        limite_nb_feuilles -= nb_feuilles_haut_gche
        nb_feuilles_haut_dte = min(max(int(round(limite_nb_feuilles * deviation_haut_dte / 
                                (deviation_haut_dte + deviation_bas_gche + deviation_bas_dte))), 1), 
                                   limite_nb_feuilles - 2)
        limite_nb_feuilles -= nb_feuilles_haut_dte
        nb_feuilles_bas_gche = min(max(int(round(limite_nb_feuilles * deviation_bas_gche / 
                                (deviation_bas_gche + deviation_bas_dte))), 1), limite_nb_feuilles - 1)
        nb_feuilles_bas_dte = limite_nb_feuilles - nb_feuilles_bas_gche
        haut_gche = creation_regions_V2(coin_x, coin_y, width // 2, height // 2, nb_feuilles_haut_gche)
        haut_dte = creation_regions_V2(coin_x + width // 2, coin_y, width - width // 2, height // 2, nb_feuilles_haut_dte)
        bas_gche = creation_regions_V2(coin_x, coin_y + height // 2, width // 2, height - height // 2, nb_feuilles_bas_gche)
        bas_dte = creation_regions_V2(coin_x + width // 2, coin_y + height // 2, width - width // 2, 
                          height - height // 2, nb_feuilles_bas_dte)
        return Noeud(coin_x, coin_y, width, height, haut_gche, haut_dte, bas_gche, bas_dte, None)

#================================
# Utilitaires
# Compte le nombre de noeuds terminaux
def count(node):
    if not node :
         return 0
    return 1 if node.color != None else \
           count(node.haut_gche) + count(node.haut_dte) + count(node.bas_gche) + count(node.bas_dte)

def Not_used_modifier_mat_pixels_et_refaire_l_image(node):
    global matrice_pixels # pas besoin mais pour le cas où !
    if not node :
         return    
    if node.color != None:
        for i in range(node.coin_x, node.coin_x + node.width):
            for j in range(node.coin_y, node.coin_y + node.height):
                matrice_pixels[i,j]=(node.color[0], node.color[1], node.color[2])
    else:
        modifier_mat_pixels_et_refaire_l_image(node.haut_gche)
        modifier_mat_pixels_et_refaire_l_image(node.haut_dte)
        modifier_mat_pixels_et_refaire_l_image(node.bas_gche)
        modifier_mat_pixels_et_refaire_l_image(node.bas_dte)
#=====================================================================


    
def OK_test_3d_juste_pour_tester_3d() :    
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt

    Max_range=20*5  # nb totale tentatives
    range_seuil_=range(Max_range)
    nb_sous_seuils=5 # on ajoutera 5 fois +0.2
    #tab_nb_sous_regions_decoupees= [random.randint() for i in range(Max_range+10)]
    tab_nb_sous_regions_decoupees=[i for i in range(10000, 70000, 600)]
    #tab_distorsion=[for s in range(Max_range)] # 10 ?? sécu. On stock les PSNRs
    tab_distorsion=[0 for i in range(Max_range)]
    for i in range(Max_range) :
        tab_distorsion[i]=50.0-i*(0.4*random.random())
    print(tab_distorsion)
    X = np.array(range_seuil_)
    print(X.shape)
    Y = np.array(tab_nb_sous_regions_decoupees[:Max_range])
    print(Y.shape)
    Z = np.array(tab_distorsion)
    print(Z.shape)
    
    x = np.reshape(X, (10, Max_range//10))
    y = np.reshape(Y, (10, Max_range//10))
    z = np.reshape(Z, (10, Max_range//10))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #ax.scatter(x, y, z, c='y', marker='o')
    ax.plot_surface(x, y, z)

    ax.set_xlabel('seuil')
    ax.set_ylabel('nb_sous régions')
    ax.set_zlabel('PSNR')

    plt.show()
#---------------------------------------
def OK_test_3d_avec_animation_juste_pour_tester_3d() :    
    Max_range=20*5  # nb totale tentatives
    range_seuil_=range(Max_range)
    nb_sous_seuils=5 # on ajoutera 5 fois +0.2
    #tab_nb_sous_regions_decoupees= [random.randint() for i in range(Max_range+10)]
    tab_nb_sous_regions_decoupees=[i for i in range(10000, 70000, 600)]
    #tab_distorsion=[for s in range(Max_range)] # 10 ?? sécu. On stock les PSNRs
    tab_distorsion=[0 for i in range(Max_range)]
    for i in range(Max_range) :
        tab_distorsion[i]=50.0-i*(0.4*random.random())
    print(tab_distorsion)
    X = np.array(range_seuil_)
    print(X.shape)
    Y = np.array(tab_nb_sous_regions_decoupees[:Max_range])
    print(Y.shape)
    Z = np.array(tab_distorsion)
    print(Z.shape)
    
    x = np.reshape(X, (10, Max_range//10))
    y = np.reshape(Y, (10, Max_range//10))
    z = np.reshape(Z, (10, Max_range//10))

    fig = plt.figure()
    ax = Axes3D(fig)
     
    ax = fig.add_subplot(111, projection='3d')

    #ax.scatter(x, y, z, c='y', marker='o')
    ax.plot_surface(x, y, z)

    ax.set_xlabel('seuil')
    ax.set_ylabel('nb_sous régions')
    ax.set_zlabel('PSNR')

    plt.show()
    
    def init():
        # Plot the surface.
        ax.plot_surface(x, y, z, cmap=cm.coolwarm, inewidth=0, antialiased=False)
        return fig,

    def animate(i):
        # elevation angle : -180 deg to 180 deg
        ax.view_init(elev=(i-45)*4, azim=10)
        return fig,

    # Animate
    print("On y va ...")
    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=50, blit=True)

    """
    ax = fig.add_subplot(111, projection='3d')

    #ax.scatter(x, y, z, c='y', marker='o')
    ax.plot_surface(x, y, z)

    ax.set_xlabel('seuil')
    ax.set_ylabel('nb_sous régions')
    ax.set_zlabel('PSNR')

    plt.show()
    """
#---------------------------------------    
# Fonction plot 3D, on passe les paramètres : c'est comme ci-dessus sauf que cette fonc est appelée
# pour faire la courbe 3D pour un jeu de données donné.
def plot_3d_juste_pour_tester_3d(For_Y_tab_nb_sous_regions_decoupees, \
                                        For_Z_tab_distorsion, For_X_Max_range=120,nb_sous_seuils=4) :     
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt


    print("On  a recu Max_range (For_X_Max_range)= ", For_X_Max_range); input("Max_range ?")
    Max_range=For_X_Max_range  # nb totale tentatives
    range_seuil_=range(Max_range)
    #nb_sous_seuils=5 # on ajoutera 5 fois +0.2
    #tab_nb_sous_regions_decoupees= [random.randint() for i in range(Max_range+10)]
    tab_nb_sous_regions_decoupees=[i for i in range(10000, 70000, 500)]
    #tab_distorsion=[for s in range(Max_range)] # 10 ?? sécu. On stock les PSNRs
    #tab_distorsion=[0 for i in range(Max_range)]
    #for i in range(Max_range) :
        #tab_distorsion[i]=50.0-i*(0.4*random.random())
    #print(tab_distorsion)
    X = np.array(range_seuil_)
    print(X.shape)
    Y = np.array(tab_nb_sous_regions_decoupees[:Max_range])
    print(Y.shape)
    Z = np.array(tab_distorsion[:For_X_Max_range])
    print(Z.shape)
    
    
    factor_division=int(np.sqrt(For_X_Max_range))
    x = np.reshape(X, (factor_division, Max_range//factor_division))
    y = np.reshape(Y, (factor_division, Max_range//factor_division))
    z = np.reshape(Z, (factor_division, Max_range//factor_division))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, c='y', marker='o')
    # OK ax.plot_surface(x, y, z)

    ax.set_xlabel('seuil')
    ax.set_ylabel('nb_sous régions')
    ax.set_zlabel('PSNR')

    plt.show()
#---------------------------------------    
# Fonction plot 3D, on passe les paramètres : c'est comme ci-dessus sauf que cette fonc est appelée
# pour faire la courbe 3D pour un jeu de données donné.
# Je 

def OK_but_not_used_test_plot_3d_avec_animation_juste_pour_tester_3d() :     
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt

    Max_range=20*5  # nb totale tentatives
    range_seuil_=range(Max_range)
    #nb_sous_seuils=5 # on ajoutera 5 fois +0.2
    #tab_nb_sous_regions_decoupees= [random.randint() for i in range(Max_range+10)]
    tab_nb_sous_regions_decoupees=[i for i in range(10000, 70000, 600)]
    assert(len(tab_nb_sous_regions_decoupees) == Max_range) # Il faut cette égalité sinon err sur Y
    #tab_distorsion=[for s in range(Max_range)] # 10 ?? sécu. On stock les PSNRs
    tab_distorsion=[0 for i in range(Max_range)]
    for i in range(Max_range) :
        tab_distorsion[i]=50.0-i*(0.4*random.random())
    #print(tab_distorsion)
    X = np.array(range_seuil_)
    print(X.shape)
    Y = np.array(tab_nb_sous_regions_decoupees[:Max_range])
    print(Y.shape)
    Z = np.array(tab_distorsion[:Max_range])
    print(Z.shape)
    
    
    factor_division=int(np.sqrt(Max_range))
    x = np.reshape(X, (factor_division, Max_range//factor_division))
    y = np.reshape(Y, (factor_division, Max_range//factor_division))
    z = np.reshape(Z, (factor_division, Max_range//factor_division))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlabel('seuil')
    ax.set_ylabel('nb_sous régions')
    ax.set_zlabel('PSNR')

    # OK ax.scatter(x, y, z, c='y', marker='o')
    # OK ax.plot_surface(x, y, z)
    
    ax.plot_wireframe(x, y, z, rstride=5, cstride=5)
    #plt.show()
    
    # rotate the axes and update
    for angle in range(0, 360):
        ax.view_init(30, angle)
        plt.draw()
        plt.pause(.001)
        
    #plt.show()
#-----------------------------------
def un_autres_test_3d() :
    import chart_studio.plotly as py
    import plotly.graph_objects as go

    import numpy as np

    s = np.linspace(0, 2 * np.pi, 240)
    t = np.linspace(0, np.pi, 240)
    tGrid, sGrid = np.meshgrid(s, t)

    r = 2 + np.sin(7 * sGrid + 5 * tGrid)  # r = 2 + sin(7s+5t)
    x = r * np.cos(sGrid) * np.sin(tGrid)  # x = r*cos(s)*sin(t)
    y = r * np.sin(sGrid) * np.sin(tGrid)  # y = r*sin(s)*sin(t)
    z = r * np.cos(tGrid)                  # z = r*cos(t)

    surface = go.Surface(x=x, y=y, z=z)
    data = [surface]

    layout = go.Layout(
        title='Parametric Plot',
        scene=dict(
            xaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            yaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            zaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            )
        )
    )

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='jupyter-parametric_plot')
# ------------------------------------------------------------------    
def tests_plot_3D() :
    OK_but_not_used_test_plot_3d_avec_animation_juste_pour_tester_3d()
    
    # TESTS PLOT 3D 
    # OK_test_3d_juste_pour_tester_3d(); quit()
    # No work test_3d_juste_pour_tester_3d_old(); quit()
    OK_test_3d_avec_animation_juste_pour_tester_3d()
    OK_test_3d_juste_pour_tester_3d()
    un_autres_test_3d()
# ==========================================================================
# Réponses aux exercices 
# ------------------------------------------------------------------    
# exercice 1.1 : peindre une région avec une couleur donnée
# Nous avons la matrice des pixels, on définit une région et on la peint
def exercice_1_1():
    put_color_into_matrice_pixels(0,0, 100,150, (100,100,100))
    im.show()
# ------------------------------------------------------------------  
# exercice 1.2 : calcul de la moyenne des couleurs d'une région
def exercice_1_2():
    print("Moyenne des couleurs : ", moyenne_couleurs(0,0, 100,150))
    # Pour l'image : 'Elena.png'
    # Moyenne des couleurs :  (126.98666666582008, 63.752533332908314, 49.690133333002066)
# ------------------------------------------------------------------  
# exercice 1.3 : calcul de l'écart type des couleurs d'une région
def exercice_1_3():
    print("écart type des couleurs : ", ecart_type_couleurs(10,10, 120,250))
    # Pour l'image : 'Elena.png'
    # écart type des couleurs :  (41.31083514196415, 25.186264425544366, 19.91842280856832)
#------------------------------------------
# exercice 1.4 : Homogénéïtée des couleurs d'une région
def exercice_1_4(seuil=10.0):
    print("Homogénéité des couleurs : ")
    #seuil = 3.0
    std= ecart_type_couleurs(10,30, 140,250)
    if sum(std)/3 < seuil:
        print("Région Homogène ")
        return True
    else :
        print("Région Non Homogène ")
        return False
    # Pour l'image : 'Elena.png'
    # Non homogène
#------------------------------------------
# exercice 1.5 : division d'une région
def exercice_1_5(W,H):
    # Ces données sont connues en lecture : 
    # W, H , matrice_pixels via les instructions du "main"
    x=0; y=0; w=W; h=H
    if True : # Plus tard, un test de homogénéïté permet (ou pas) de découper en 4. 
        return  ((x, y, w//2, h//2) ,
                 (x + w//2, y, w - w//2, h//2) ,
                 (x, y + h//2, w//2, h - h//2) ,
                 (x + w//2, y + h//2, w - w//2, h - h//2)
                 )
    
#------------------------------------------
# exercice 2.1 : classe Noeud
# Si  la classe Noeud est définie, alors le dict interne contiendra : 
# (<class '__main__.Noeud'>, <class 'type'>), 

def exercice_2_1() :
    if "Noeud" in globals().keys():
        print("La classe Noeud est définie ")
    else :
        print("La classe Noeud NON définie ")
    return

    # On peut tout afficher (tout ce qui est défini)

    #print(globals()) # un dico de tout ce qui est défini
    for key,val in globals().items() :
        print(key , " :: ", val)
        print("--------------------------------------")
        print([k for k in globals().keys()])
        print("--------------------------------------")
        print([k for k in globals().values()])
        print("--------------------------------------")
        input("0 ? ")
    """
    Donne : les keys 
   ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', 
   '__file__', '__cached__', 'sqrt', 'log10', 'Image', 'argv', 'stdin', 'np', '__warningregistry__', 
   'plt', 'animation', 'Axes3D', 'cm', 'random', 'put_color_into_matrice_pixels', 'moyenne_couleurs', 
   'ecart_type_couleurs', 'Noeud', 'creation_regions_V1', 'apply_node_color_to_his_region_in_mat_pixels',
    'apply_a_color_aux_noeuds_terminaux_de_l_arbre', 'Err_quadratique', 'PSNR', 'tracer', 
    'creation_regions_V2', 'count', 'Not_used_modifier_mat_pixels_et_refaire_l_image', 
    'OK_test_3d_juste_pour_tester_3d', 'OK_test_3d_avec_animation_juste_pour_tester_3d', 
    'plot_3d_juste_pour_tester_3d', 'OK_but_not_used_test_plot_3d_avec_animation_juste_pour_tester_3d', 
    'what', 'tests_plot_3D', 'exercice_1_2', 'exercice_1_3', 'exercice_1_4', 'exercice_1_5', 'exercice_2_1', 
    'exercice_2_2', 'exercice_2_3', 'im', 'W', 'H', 'matrice_pixels']

    et les valeurs correspondantes :
    ['__main__', pour __name ..
    bcp de None où il n'y a pas de déf
    pour file : '/home/alex/ECL-20-21/1A-20-21/S6/TC1/BE3-Image/BE3-mOI/OK-td3-ma-version-20-21.py', 
    argv ? : ['/home/alex/ECL-20-21/1A-20-21/S6/TC1/BE3-Image/BE3-mOI/OK-td3-ma-version-20-21.py'], 
    <module 'random' from '/usr/lib/python3.8/random.py'>, 
    <function put_color_into_matrice_pixels at 0x7f7710347430>, 
    <function moyenne_couleurs at 0x7f770a9d05e0>, 
    .. les autres fonctions (dans key, on a le nom de chaque fonction et dans value ci-dessus : )
    Pour la classe Noeud, on a la clé "Noeud" et dans value, on a  <class '__main__.Noeud'>, 
    ...
    """
#------------------------------------------
""" Version S6 du 2021
Exercice 2.2 – Créez une fonction qui récupère en entrée une portion de l’image (représentée par
un rectangle) ainsi qu’un seuil d’homogénéité, et renvoie le Noeud correspondant. Si les pixels de
la portion sont homogènes, le Noeud sera terminal (pas d’enfant) et sa couleur sera la moyenne des
pixels de la portion. S’ils ne sont pas homogènes, le Noeud aura au plus 4 enfants, résultats de
l’appel récursif de la fonction sur la quadripartition générée à l’exercice 1.5. Le Noeud sera donc
non-terminal, et sa couleur pourra être fixée à une valeur arbitraire (sans importance).

"""
def exercice_2_2(coin_x, coin_y, width, height, seuil=20) :
    return creation_regions_V1(coin_x, coin_y, width, height, seuil)
#------------------------------------------
"""
Exercice 2.3 – Proposez une fonction récursive, qui permet de compter le nombre d’enfants (sous-
enfants, sous-sous-enfants, etc.) d’un Noeud, en le comptant également. Pour la racine de la figure 2
elle renverrait par exemple 13.
"""
def exercice_2_3(noeud) :
    return count(node)
#------------------------------------------
# Exercice 2.4 – Proposez une fonction récursive qui parcourt l’arbre depuis sa racine, et peint
# chaque noeud terminal selon la couleur qui lui a été assignée.

# Version S6 20-21
def exercice_2_4(root):
    # Test Ex 2.4 
    color_to_apply=12,25,65  #0,0,0 #12,25,65 # arbitraire
    apply_a_color_aux_noeuds_terminaux_de_l_arbre(color_to_apply, root)

#------------------------------------------
# Exercice 2.5 – Écrivez une fonction récursive qui peint les noeuds terminaux d’un arbre d’une
# couleur proportionnelle à leur profondeur dans l’arbre.

# Version S6 20-21
def exercice_2_5(seuil=10):
    # Test Ex 2.5 
    # On reconstitue l'image (sa matrice de pixels) d'origine car la matrice a été modifiée
    global matrice_pixels # pas besoin mais pour le cas où !
    matrice_pixels = im.load()
    width, height= im.size  # n'ont pas changé
    coin_x, coin_y = 0,0 
    root=creation_regions_V1(coin_x, coin_y, width, height, seuil)
    color_to_apply=12,25,65#0,0,0 #12,25,65 # arbitraire
    apply_a_color_a_la_matrice_selon_niveau_de_l_arbre(color_to_apply, root, 1)

#------------------------------------------
# Exercice 2.6 – Pour évaluer la qualité visuelle de l’image dégradée par rapport à l’originale, on
# utilise une mesure de distorsion qui va nous permettre de comparer les résultats de différents critères
# de compression. Écrivez une fonction qui calcule la mesure Peak Signal to Noise Ratio (P SN R)
# pour l’image complète, en calculant l’Erreur Quadratique (EQ) de manière récursive :

# Version S6 20-21
def exercice_2_6(seuil=10):
    # Test Exo 2.6
    # On reconstitue l'image (sa matrice de pixels) d'origine car la matrice a été modifiée
    global matrice_pixels # pas besoin mais pour le cas où !
    matrice_pixels = im.load()
    width, height= im.size # n'ont pas changé
    coin_x, coin_y = 0,0 
    root=creation_regions_V1(coin_x, coin_y, width, height, seuil)
    Distorsion = PSNR(root)
    
#------------------------------------------
import multiprocessing
from os import getpid, getppid


#---------------------------------
def decouper_image_version_parallele(seuil=30) :
    global matrice_pixels # Ici global est nécessaire
    matrice_pixels = im.load()   
    W,H=im.size
    
    root, nb_regions = creation_regions_V1_renvoie_nb_regions(0, 0, W, H, seuil)
    print("découpage pour le seuil ", seuil, " nb_regions = ", nb_regions) 
    return PSNR(root), nb_regions
# ---------------
def Creation_tab_distortion_et_plot_PARALLELE() :
    
    print("Début Grid search pour la courbe seuil vs PSNR (LONG !!) .. attendre l'affichage de la courbe  ")
    im = Image.open("Two_Men.png")
    im = Image.open("petite-image.png")
    W, H = im.size
    #matrice_pixels = im.load()    
    limite_seuil=30
    nb_sous_seuils=4 # on ajoutera 4 fois +0.25
    surplus_de_securite=10 # pour des dépassements !!??
    Max_range=limite_seuil*nb_sous_seuils  # nb totale tentatives
    range_seuil_=range(Max_range)

    tab_nb_sous_regions_decoupees=[0 for i in range(Max_range+surplus_de_securite)]
    tab_distorsion=[0 for s in range(Max_range+surplus_de_securite)] #   sécu. On stock les PSNRs 
 
    # ??nb_regions=0
    
    for seuil_ in range(limite_seuil) : # range_seuil_ :
        s=seuil_
        lst=[seuil_+i/nb_sous_seuils   for i in range(nb_sous_seuils)]
        #print("lst : ", lst)
        pool = multiprocessing.Pool(processes=4)
        liste_retours_couples_PSNR_nb_reg= pool.map(decouper_image_version_parallele, lst)
        #print(liste_retours_couples_PSNR_nb_reg); quit()
        for i, (psnr, nb_reg) in enumerate(liste_retours_couples_PSNR_nb_reg) :
            #print("Pour seuil_ = ", seuil_, " et i= ", i)
            # print("seuil_*nb_sous_seuils+i = ", seuil_*nb_sous_seuils+i, "taille tab = ", len(tab_distorsion))
            tab_distorsion[seuil_*nb_sous_seuils+i]=psnr
            tab_nb_sous_regions_decoupees[seuil_*nb_sous_seuils+i]=nb_reg

    print(tab_distorsion[:50])
    plt.plot(range_seuil_,tab_distorsion[:Max_range])
    plt.xlabel("Seuil ")
    plt.ylabel("PSNR")
    plt.show()
    int(input("Fin courbe seuil vs PSNR, continuer ? ")) # conversion en int pour pouvoir planter (ne pas aleer +loin)
#------------------------------------------

#------------------------------------------
#------------------------------------------
#------------------------------------------
#------------------------------------------
#------------------------------------------
# ==========================================================================
if __name__ == "__main__" :
    global matrice_pixels,nb_regions # pas besoin mais pour le cas où !
    #### ------- Debut traitements -------------
    ### On peut lire le nom png au clavier ###
    # im = Image.open(stdin.buffer) # appelé par "python td3-2.py < Image10.bmp"
    
    """
    Une autre méthode pour ouvrir le fichier image donné en ligne de commande : 
    Trop vieux : StringIO.StringIO(...)
    Pour Python 2.x : Takes a byte string or Unicode string. 
    If byte string, returns a byte stream. If Unicode string, returns a Unicode stream.

    # im = Image.open(StringIO.StringIO(png))
    """
    
    # Je simplifie l'ouverture de l'image
    #im = Image.open('Image10.bmp') # OK
    nom_fic='Elena.png'
    nom_fic='Elena.png'
    #nom_fic="petite-image.png"
    im = Image.open(nom_fic)

    print("On a ouvert le fichier ", nom_fic)
    W, H = im.size
    matrice_pixels = im.load()    
    seuil=10
    im.show() # Image d'origine
    
    #--- exercice 1.1 : --------
    #  peindre une région avec une couleur donnée
    print("exercice 1.1 : peindre une région avec une couleur donnée")
    # OK testé : 
    # exercice_1_1(); quit()
    
    #----exercice 1.2 : --------
    # la moyenne de couleur d'une région
    print("exercice 1.2 : Moyenne des couleurs d'une région")
    # OK tetsté :
    # exercice_1_2(); quit()
    
    #----exercice 1.3 : --------
    # la moyenne de couleur d'une région
    print("exercice 1.3 : écart type des couleurs d'une région")
    # OK tetsté :
    # exercice_1_3(); quit()
        
    #----exercice 1.4 : --------
    print("exercice 1.4 : Homogénéïté des couleurs d'une région")
    # Testé OK : 
    # exercice_1_4(seuil); quit()
    
        
    #----exercice 1.5 : --------
    print("exercice 1.5 : Division d'une région")
    # Testé OK : 
    # exercice_1_5(W,H); quit()
    
    #----exercice 2.1 (S6 du 20-21): --------
    print("exercice 2.1 : Classe Noeud")
    # OK : exercice_2_1(); quit()

    print("exercice 2.2 : Découpage")
    # Pour les questions de  la partie 2.xx
    nb_regions=0
    # Test Ex 2.2
    seuil=10 # ca fait pas mal d'enfants d'enfants
    root = exercice_2_2(0, 0, W, H, seuil)
    # OK : trop de données pour ce seuil : 
    # print(root) # Appele la fonction __str__
    # Donne l'arbre (pour une seul de 44):
    """
    {x=0, y=0, w=326, h=374,             couleur=None}
        {x=0, y=0, w=163, h=187,             couleur=(128, 69, 57)}
        {x=163, y=0, w=163, h=187,             couleur=None}
                {x=163, y=0, w=81, h=93,             couleur=None}
                        {x=163, y=0, w=40, h=46,             couleur=(175, 117, 101)}
                        {x=203, y=0, w=41, h=46,             couleur=(134, 70, 56)}
                        {x=163, y=46, w=40, h=47,             couleur=(202, 151, 139)}
                        {x=203, y=46, w=41, h=47,             couleur=None}
                                {x=203, y=46, w=20, h=23,             couleur=(208, 168, 158)}
                                {x=223, y=46, w=21, h=23,             couleur=None}
                                        {x=223, y=46, w=10, h=11,             couleur=None}
                                                {x=223, y=46, w=5, h=5,             couleur=(85, 46, 37)}
    .......
    """

    # Non nedd pour l'instant
    # apply_node_color_to_his_region_in_mat_pixels(root)    
    # quit()

    print("exercice 2.3 : comptage des enfants")
    print(count(root)) # root est défini ci-dessus
    # Affiche 52 pour "root" ci-dessus pour Elena
    # quit()

    print("exercice 2.4 : peindre les noeuds terminaux")
    exercice_2_4(root)
    im.show()    
    int(input('Fin Ex 2.4 : On continue ?')) # appuyer sur "entrée" pour planter = ne pas continuer !

    print("exercice 2.5 : peindre les noeuds terminaux selon la profondeur")  
    exercice_2_5(seuil)
    im.show()   
    int(input('Fin Ex 2.5 : On continue ?')) # appuyer sur "entrée" pour planter = ne pas continuer !
    #quit()
    #=================================================================

    # Test Exo 2.6
    # On reconstituera l'image d'origine car la matrice a été modifiée 
    print("exercice 2.6 : PSNR")     
    exercice_2_6(seuil)
    int(input("Fin exo_2_6, continuer ? ")) # conversion en int pour pouvoir planter (ne pas aleer +loin)
    #################### Un ex plot 3D pris sur le WEB #######################""
    """
    Ex plot 3d vu sur le WEB
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm
    import matplotlib.pyplot as plt
    # Ceci a donné qq chose mais pas top
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = L_synapse0_0; y = L_synapse0_1;
    X, Y = np.meshgrid(x, y)
    Z= np.array(err)
    ax.plot_surface(X, Y, Z)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()
    """
    
    
    ######################  GRID SEARCH : courbe seuil vs PSNR ################ 
    # Grid search sur "Two_Men.png" pour trouver les combinaisons seui vs PSNR et faire une courbe 2D
    Creation_tab_distortion_et_plot_PARALLELE()
    int(input(" Fin de  pool, continuer  ??? "))


    print("Début Grid search pour la courbe 2D seuil vs PSNR .. attendre l'affichage de la courbe 2D")
    #im = Image.open("Two_Men.png")
    im = Image.open("petite-image.png")
    W, H = im.size
    matrice_pixels = im.load()    
    limite_seuil=30 # 20 pour Two_Men
    nb_sous_seuils=4 # on ajoutera 4 fois +0.25
    surplus_de_securite=10 # pour des dépassements !!??
    Max_range=limite_seuil*nb_sous_seuils  # nb totale tentatives
    range_seuil_=range(Max_range) # mm si commencer à seuil=0 n'est pas intéressant. on découpe rien

    tab_nb_sous_regions_decoupees=[0 for i in range(Max_range+surplus_de_securite)]
    tab_distorsion=[0 for s in range(Max_range+surplus_de_securite)] #   sécu. On stock les PSNRs 
 
    #nb_regions=0
    # On va couvrir les seuls de 0 .. 40 avec un pas de 0.25
    for seuil_ in range(limite_seuil) : # range_seuil_ :        
        s=seuil_
        for i in range(nb_sous_seuils) :
            s=seuil_+i/nb_sous_seuils          
            matrice_pixels = im.load()    
            nb_regions=0
             
            root=creation_regions_V1(0, 0, W, H, s)
            print("seuil_ = ", seuil_,  " i= ", i, " découpage pour seuil = ", s, " nb_reg = ", nb_regions)
            tab_distorsion[seuil_*nb_sous_seuils+i]= PSNR(root) # =Distorsion  ??
            tab_nb_sous_regions_decoupees[seuil_*nb_sous_seuils+i]=nb_regions
            # print("On a écrit dans TAB[", seuil_*nb_sous_seuils+i,']')
            
    print(tab_distorsion[:50])
    plt.plot(range_seuil_,tab_distorsion[:Max_range])
    plt.xlabel("Seuil ")
    plt.ylabel("PSNR")
    plt.show()
    int(input("Fin courbe 2D seuil vs PSNR, continuer ? ")) # conversion en int pour pouvoir planter (ne pas aleer +loin)

    ############## Plot 3D, OK, X=seuil, y=tab_distorsion, z=nb_sous_regions ########
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = range_seuil_; y = tab_distorsion[:Max_range]
    X, Y = np.meshgrid(x, y)
    
    Z=np.zeros((len(x),len(y))) # Z doit être 2d
    Z[:,]= tab_nb_sous_regions_decoupees[:len(x)]
    ax.plot_surface(X, Y, Z)
    ax.set_xlabel('seuil')
    ax.set_ylabel('PSNR')
    ax.set_zlabel('nb sous régions')
    plt.show()
    int(input("Fin courbe 3D seuil vs PSNR, continuer ? ")) # conversion en int pour pouvoir planter (ne pas aleer +loin)
    ###################### Fin plot 3d OK ##############################
    
    
    ################# 2e Plot 3D mais on inverse Y et Z ##################
    # Inverser Y et Z
    plot_3d_juste_pour_tester_3d(For_Y_tab_nb_sous_regions_decoupees=tab_nb_sous_regions_decoupees,\
        For_Z_tab_distorsion=tab_distorsion, For_X_Max_range= Max_range,nb_sous_seuils=nb_sous_seuils) 
    
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    #x = range_seuil_; y = tab_distorsion[:Max_range]
    #X, Y = np.meshgrid(x, y)
    
    #Z=np.zeros((len(x),len(y))) # Z doit être 2d
    #Z[:,]= tab_nb_sous_regions_decoupees[:len(x)]
    #ax.plot_surface(X, Y, Z)
    #ax.set_xlabel('seuil')
    #ax.set_ylabel('PSNR')
    #ax.set_zlabel('nb sous régions')
    #plt.show()
    int(input("Fin 2e plot 3D, continuer ? ")) # conversion en int pour pouvoir planter (ne pas aleer +loin)
    ###################### Fin 2e plot 3d OK ##############################
        
        
    #################### Plot 3d comme ci-dessus mais avec animation ########
    # Avoir, S6 20-21 ???
    # OK_but_not_used_test_plot_3d_avec_animation_juste_pour_tester_3d()
    # For_Y_tab_nb_sous_regions_decoupees=tab_nb_sous_regions_decoupees,For_Z_tab_distorsion=tab_distorsion, For_X_Max_range=Max_range,nb_sous_seuils=4) 
    ################ Fin plot avec animation ###################
    #print("Distorsion avec le seuil ", seuil, "= ", Distorsion)
    #int(input('Fin Ex ???  : On continue ?'))
    
    # Test Ex ??
    tracer(root,0)
    input('Fin Ex 2.5 (trace) : On continue ?')
    
    # Test Ex ?? : modifier_mat_pixels_et_refaire_l_image(root)
    im.show()
    root = creation_regions_V2(0, 0, W, H, 10000)
    #tracer(root,0)
    
    # qq tests en rapport avec 2.6
    apply_node_color_to_his_region_in_mat_pixels(root)    
    # modifier_mat_pixels_et_refaire_l_image(root)
    im.show()
    int(input('Fin paint_children : On continue ?')) # Planter le code ici en appuyant sur "entrée"
    
    # On a modifié mat_pixels et root
    matrice_pixels = im.load()
    root = creation_regions_V2(0, 0, W, H, 10000)
    color_to_apply=12,25,65#0,0,0 #12,25,65 # arbitraire
    apply_a_color_aux_noeuds_terminaux_de_l_arbre(color_to_apply, root)
    # modifier_mat_pixels_et_refaire_l_image(root)
    im.show()    
    print('Fin paint_children_in_color ... on va manger ?')


    # D'autres tests de plots
    tests_plot_3D() 
    
