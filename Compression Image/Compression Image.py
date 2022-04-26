
from PIL import Image # importation de la librairie d’image PILLOW
from math import sqrt, log2, ceil, log10 # fonctions essentielles de la librairie math
from pprint import pprint
import time as t
import matplotlib.pyplot as plt
import os
import psutil
im = Image.open("fractale.png") # ouverture du fichier d’image
px = im.load() # importation des pixels de l’image
W, H = im.size

# Exo 1.1
def peindre(x, y, w, h, r, g, b):
	couleur = (r, g, b)
	for i in range(w):
		for j in range(h):
			px[x+i, y+j] = couleur

# Exo 1.2
def moyenne(x, y, w, h):
	sr, sg, sb = 0, 0, 0
	for i in range(w):
		for j in range(h):
			r, g, b = px[x+i, y+j]
			sr += r
			sg += g
			sb += b
	n = w * h
	return sr/n, sg/n, sb/n

# Exo 1.3
def ecart_type(x, y, w, h):
	sr, sg, sb = 0, 0, 0
	sqr, sqg, sqb = 0, 0, 0
	for i in range(w):
		for j in range(h):
			r, g, b = px[x+i, y+j]
			sr += r
			sg += g
			sb += b
			sqr += r*r
			sqg += g*g
			sqb += b*b
	n = w * h
	return 10*sqrt(sqr/n - (sr/n)**2), sqrt(sqg/n - (sg/n)**2), sqrt(sqb/n - (sb/n)**2) #L'écart type du rouge a une valeur plus importante

# Exo 1.4
def est_homogene(x, y, w, h, seuil):
	val = sum(ecart_type(x, y, w, h))/12 #Valeur de l'écrat type
	rayon = ((x-W/2)**2+(y-H/2)**2)/((H/2)**2+(W/2)**2) # rayon du pixel par rapport au centre de l'image
	val = val/(rayon+0.5) #La valeur varie par sa distance au centre
	return val <= seuil

# Exo 1.5
def partition(x, y, w, h):
	assert w>0 and h>0 and not w==h==1
	i = (w+1)//2
	j = (h+1)//2
	return (
		(x, y, i, j),
		(x+i, y, w-i, j) if w>1 else None,
		(x, y+j, i, h-j) if h>1 else None,
		(x+i, y+j, w-i, h-j) if w>1 and h>1 else None)

# Exo 2
class Noeud:
	def __init__(self, x, y, l, h, r, v, b, hg, hd, bg, bd):
		self.x = x
		self.y = y
		self.l = l
		self.h = h
		self.r = r
		self.v = v
		self.b = b
		self.hg = hg # haut-gauche
		self.hd = hd # haut-droite
		self.bg = bg # bas-gauche
		self.bd = bd # bas-droite
	
	def __repr__(self, prefix=""):
		return "\n".join((f"{prefix}({self.x},{self.y},{self.l},{self.h}) couleur ({self.r},{self.v},{self.b}) enfants :",
			self.hg.__repr__(prefix+"  ") if self.hg!=None else prefix+"  None",
			self.hd.__repr__(prefix+"  ") if self.hd!=None else prefix+"  None",
			self.bg.__repr__(prefix+"  ") if self.bg!=None else prefix+"  None",
			self.bd.__repr__(prefix+"  ") if self.bd!=None else prefix+"  None"))

# Exo 2.2
def arbre(x, y, w, h, seuil):
	r, g, b = moyenne(x, y, w, h)
	if est_homogene(x, y, w, h, seuil):
		return Noeud(x, y, w, h, r, g, b, None, None, None, None)
	else:
		hg, hd, bg, bd = partition(x, y, w, h)
		return Noeud(x, y, w, h, r, g, b,
			arbre(*hg, seuil) if hg!=None else None,
			arbre(*hd, seuil) if hd!=None else None,
			arbre(*bg, seuil) if bg!=None else None,
			arbre(*bd, seuil) if bd!=None else None)

# Exo 2.3
def compter(n):
	if n == None:
		return 0
	return 1 + compter(n.hg) + compter(n.hd) + compter(n.bg) + compter(n.bd)

# Exo 2.4
def peindre_arbre(n):
	if n == None:
		return
	if n.hg==n.hd==n.bg==n.bd==None:
		peindre(n.x, n.y, n.l, n.h, round(n.r), round(n.v), round(n.b))
	else:
		peindre_arbre(n.hg)
		peindre_arbre(n.hd)
		peindre_arbre(n.bg)
		peindre_arbre(n.bd)

# Exo 2.5
def peindre_profondeur(n, p=0):
	if n == None:
		return
	if n.hg==n.hd==n.bg==n.bd==None:
		m = ceil(log2(max(W, H)))
		peindre(n.x, n.y, n.l, n.h, 255*p//m, 255*p//m, 255*p//m)
	else:
		peindre_profondeur(n.hg, p+1)
		peindre_profondeur(n.hd, p+1)
		peindre_profondeur(n.bg, p+1)
		peindre_profondeur(n.bd, p+1)

# Exo 2.6
def EQ(n):
	if n == None:
		return 0
	if n.hg==n.hd==n.bg==n.bd==None:
		eq = 0
		for i in range(n.x, n.x+n.l):
			for j in range(n.y, n.y+n.h):
				r, g, b = px[i, j]
				eq += (r-n.r)**2 + (g-n.v)**2 + (b-n.b)**2
		return eq
	else:
		return EQ(n.hg) + EQ(n.hd) + EQ(n.bg) + EQ(n.bd)

def PSNR(n):
	return 20 * log10(255) - 10 * log10(EQ(n) / 3 / n.l / n.h)

# Exo 3.1
# Pour le noeud n, son fils i (i de 0 à 3) est à la position : 4*n+i+1
# Pour le noeud n, son parent est à la position : round((n-1)/4)

#Exo 3.2
class Noeud2:
	def __init__(self, x, y, l, h, r, v, b):
		self.x = x
		self.y = y
		self.l = l
		self.h = h
		self.r = r
		self.v = v
		self.b = b

def arbre2(x, y, w, h, seuil):
	r, g, b = moyenne(x, y, w, h)
	homogene = False 
	arbreL = [Noeud2(x,y,w,h,r,g,b)]#On initialise l'arbre avec comme premier noeud l'image entiere
	profondeur = 0 #Profondeur de l'arbre lors de sa construction
	while not(homogene):#Tant qu'il y a des noeuds qui ne sont pas homogène on continue de diviser
		fils = []#Liste des fils de cette profondeur
		hom = True
		for i in range(4**profondeur):#Pour chaque père
			if (arbreL[-1-i] == None):
				for l in range(4):
						fils.append(None)
			else:
				if(est_homogene(arbreL[-1-i].x,arbreL[-1-i].y,arbreL[-1-i].l,arbreL[-1-i].h,seuil)):#Si le père est homogène, ses fils seront identique
					for l in range(4):
						fils.append(None)
				else:#Si le père n'est pas homogène, il faut encore le diviser
					hom = False
					xb = arbreL[-1-i].x
					yb = arbreL[-1-i].y
					wb = arbreL[-1-i].l
					hb = arbreL[-1-i].h

					hg, hd, bg, bd = partition(xb, yb, wb, hb)
					if hg !=None:
						r, g, b = moyenne(*hg)#haut gauche
						fils.append(Noeud2(*hg,r,g,b))
					else:
						fils.append(None)

					if bg != None:
						r, g, b = moyenne(*bg)#bas gauche
						fils.append(Noeud2(*bg,r,g,b))
					else:
						fils.append(None)

					if hd != None:
						r, g, b = moyenne(*hd)#haut droite
						fils.append(Noeud2(*hd,r,g,b))
					else:
						fils.append(None)
					
					if bd != None:
						r, g, b = moyenne(*bd)#bas droite
						fils.append(Noeud2(*bd,r,g,b))
					else:
						fils.append(None)
				
		if hom:#Si tout les fils sont homogène, on arrête de diviser
			homogene = True
		else:#Sinon on enregistre les fils et on recommence
			for i in fils:
				arbreL.append(i)
		profondeur += 1
	return arbreL

def peindre_arbre2(liste):
	for n in liste:
		if n != None:
			peindre(n.x, n.y, n.l, n.h, round(n.r), round(n.v), round(n.b))

def divise_rectangle(x,y,w,h=0):
	if h == 0:
		h = w
	if w == 1 and h == 1:
		return [(x,y,w,h)]
	
	if w == 1:
		y1,y2 = y,y+h//2
		h1,h2 = h//2, h-h//2
		r1 = (x,y1,w,h1)
		r2 = (x,y2,w,h2)
		return [r1,r2]
	
	if h == 1:
		x1,x2 = x,x+w//2
		w1,w2 = w//2, w-w//2
		r1 = (x1,y,w1,h)
		r2 = (x2,y,w2,h)
		return [r1,r2]
	
	y1,y2 = y,y+h//2
	h1,h2 = h//2, h-h//2
	x1,x2 = x,x+w//2
	w1,w2 = w//2, w-w//2
	
	r1 = (x1,y1,w1,h1)
	r2 = (x2,y1,w2,h1)
	r3 = (x1,y2,w1,h2)
	r4 = (x2,y2,w2,h2)
	return [r1,r2,r3,r4]

class Noeud3:
	def __init__(self, x, y, w, h, r, g, b):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.r = r
		self.g = g
		self.b = b
	
	def infos(self):
		return self.x, self.y, self.w, self.h, (self.r, self.g, self.b)
	
	def peindre(self):
		peindre(self.x, self.y, self.w, self.h,round(self.r), round(self.g), round(self.b))

	def get_couleur(self):
		return self.r, self.g, self.b
	
	def set_couleur(self,r,g,b):
		self.r = r
		self.g = g
		self.b = b
	
	def intensite(self):
		s = 0
		for i in range(self.w):
			for j in range(self.h):
				r,g,b = px[self.x+i, self.y+j]
				s += (self.r - r)**2
				s += (self.g - g)**2
				s += (self.b - b)**2
		return s
		
def arbre3(x, y, w, h, seuil):
	
	def aux(x, y, w, h, seuil, indice, liste_tas):
		
		if len(liste_tas) < indice+1:
			liste_tas += [None]*(indice+1)
		
		if est_homogene(x, y, w, h, seuil):
			r,g,b = moyenne(x,y,w,h)
			liste_tas[indice] = Noeud3(x, y, w, h, r, g, b)
		
		else:
			liste_tas[indice] = Noeud3(x, y, w, h, -1, -1, -1)
			i = 0
			for x1,y1,w1,h1 in divise_rectangle(x,y,w,h):
				liste_tas = aux(x1, y1, w1, h1, seuil, 4*indice+i, liste_tas)
				i += 1
				
		return liste_tas
		
	return aux(x, y, w, h, seuil, 0, [])

def peindre_arbre3(arbre):
	arbre += [None]*3*len(arbre)
	
	def aux(indice):
		
		if arbre[4*indice+1] == None:
			arbre[indice].peindre()
			return 
		
		for i in range(4):
			if arbre[4*indice + i+1] != None:
				aux(4*indice + i+1)
	aux(0)


def estimationTempsEspace():
	seuil=[j for j in range(1,5)]
	for j in range(1,10):
		seuil.append(5*j)
	process = psutil.Process(os.getpid())
	
	valeur=[]
	cout=[]
	for i in seuil:
		x=t.time()
		racine = arbre(0, 0, W, H, i)
		#peindre_arbre(racine)
		y=t.time()
		valeur.append(y-x)
		process = psutil.Process(os.getpid())
		cout.append(process.memory_info().rss)
		
	valeur2=[]
	cout2=[]
	for i in seuil:
		x=t.time()
		racine = arbre2(0, 0, W, H, i)
		#peindre_arbre2(racine)
		y=t.time()
		valeur2.append(y-x)
		process = psutil.Process(os.getpid())
		cout2.append(process.memory_info().rss)
		
	valeur3=[]
	cout3=[]
	for i in seuil:
		x=t.time()
		racine = arbre3(0, 0, W, H, i)
		#peindre_arbre3(racine)
		y=t.time()
		valeur3.append(y-x)
		process = psutil.Process(os.getpid())
		cout3.append(process.memory_info().rss)
		
	
	plt.figure('temps')
	plt.plot(seuil,valeur,label = "Méthode explicite")
	plt.plot(seuil,valeur2,label = "Méthode implicite itérative")
	plt.plot(seuil,valeur3,label = "Méthode implicite récursive")
	plt.legend()
	plt.show()
	
	plt.figure('place')
	plt.plot(seuil,cout,label = "Méthode explicite")
	plt.plot(seuil,cout2,label = "Méthode implicite itérative")
	plt.plot(seuil,cout3,label = "Méthode implicite récursive")
	plt.legend()
	plt.show()

if __name__ == "__main__":
	
	
	racine = arbre(0,0,W,H,20)
	#racine = arbre(0, 0, W, H, 5)
	print(PSNR(racine))
	peindre_arbre(racine)
	#peindre_arbre(racine)
	#im.save("reponse-1-rien.png")
	im.show()