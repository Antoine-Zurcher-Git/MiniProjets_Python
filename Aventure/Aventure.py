print("Les fantasmagoriques aventures de John Deuf !")
print("")
print("")
rt = "5"
pageA = 0
while rt != "1":
	print("Bienvenue dans cette aventure !")
	print("")
	print("Pour répondre entrez 1 ou 2 en fonction de votre réponse !")
	print("Compris ! / pouvez-vous répéter ?")
	rt = input()
	print("")
print("Si aucune propositions ne vous est faites entrez 1")
print("Parfait l'aventure va pouvoir commencer !")
print("Un homme s'approche doucement de vous ...")
print("c'est parti / let's go")
cheatR = input()
cheat = ""
numCheat = ""
if len(cheatR) > 7:
	for i in range(7):
		cheat += cheatR[i]
	if cheat == "pélican":
		for i in range(len(cheatR)-7):
			numCheat += cheatR[i+7]
		numCheat = int(numCheat)
		pageA = numCheat


for i in range(30):
	print("")

inv = []






event = [["- Psst... psstt ... PSSTT !","- Comment est votre blanquette ?","Ma blanquette est bonne / Je suis végan"],#0
	["- Bien je vois que je ne me suis pas trompé !","- Nous allons pouvoir commencé !","c'est parti / je reste sur mon banc"],#1
	["- Ah bon ? Je me serai trompé ?","- Bon et bien excusé moi, au revoir","au revoir / non attendez"],#2
	["- Ecoutez moi attentivement !","- Votre mission va être de récupérer une arme Bactériologique qui nous a été dérobé","- Nous pensons que le voleur est Marc Assin, patron de la mafia du Vatican","Je comprends / Marcassin !?"],#3
	["- Oui Marc Assin, nous savons qu'il veut nous nuire, c'est pourquoi il est premier dans notre liste des suspect","- De plus nous avons remarqué une forte activité autour de sa villa qui est étrangement bien gardée pour une simple villa","- A propos de sa villa nous pensons qu'elle est piégée donc faites attention !","J'ai compris ! / Reprenons depuis le début"],#4
	["- Oui ?","c'est bien moi / votre moustache est horrible"],#5
	["- Vous allez être parachuté cette nuit à proximité de sa villa","- C'est une opération a haut risque, c'est pourquoi nous faisons appelle à vous !","- Avez-vous de questions ?","oui / non"],#6
	["- Bien, bien bien ...","- Vous êtes bien le célèbre aventurier John Deuf ?","oui / non : "],#7
	["- Dommage nous n'avons pas le temps","- Nous allons continuer votre briefing dans l'avion, il décolle bientôt !","ok / ça me semble trop risqué pour moi, je me retire"],#8
	["Un vrombissement  d'avion se fait entendre","Bien ! Je vois que votre combinaison vous va à ravir !","Vous allez bientôt devoir sauter, votre chute devrais durée environ 2 minutes","Sortez votre parachute proche du sol afin que personne ne vous remarque","Vous avez tout compris ?","oui, prêt au grand saut / non"],#9
	["Vous sautez","Vous sautez juste avant de finir en crêpe, à environ 450 mètres","Et vous infiltrez le repère de Marc Assin tout en évitant de vous faire repérer par ses drones","Chef oui chef ! / gneeeuuuu"],#10
	["Vous chutez de plus en plus rapidement","Un altimètre est attaché à votre main","Il va falloir choisir quand ouvrir son parachute","600m / 500m / 400m / 300m / 250m "],#11
	["Vous ouvrez votre parachute à 500 mètres d'altitude","La descente se fait sans accro et vous arrivez à atterrir en sécurité","Vous regardez autour de vous et trouvez un bâton, il pourrait vous servir pour la suite de l'aventure"],#12
	["Vous ouvrez votre parachute à 400 mètres d'altitude","La descente est rude et l'atterrissage vous secoue","Il en faut plus pour vous faire face, vous reprenez rapidement vos esprits","Et vous vous dirigez en direction de la villa de Marc Assin"],#13
	["Vous vous retrouvez à proximité de la fameuse villa, il vous semble que vous êtes à l'arrière de celle-ci","Il y a du grillage devant vous, quelques bâtiments isolé à droite et le principale bâtiment de la villa à gauche","vous :","faites le tour vers la gauche / faites le tour vers la droite / allez tout droit"],#14
	[""],#15 gauche de la villa
	["Vous vous rapproché des batîments isolé en longeant le grillage","Finalement vous trouvez une faille dans le grillage et vous arrivez à vous-y précipiter","Vous vous retrouvez dans l'enclot des chiens"],#16
	["Vous vous rapprochez du grillage","Il y a un long bâtiment devant vous avec à sa gauche se qui resseble à la villa","Il y a une porte dans le grillage vérouillée par un cadenas","Tenter d'entré / Faire demi-tour / Examiner les alentours"],#17 tout droit grillage
	["Vous prenez les devants sur les chiens et agitez le bâton comme un jouet","Vous jetez finalement le bâton loin dans la forêt","Et vous vous précipité à l'intérieur de la villa avant que les chiens ne reviennent"],#18 chien + bâton
	["Les chiens ont donnés l'alerte","Il va falloir courir vite","Plus vite","PLUS VITE !","ENCORE PLUS VITE !!!!"],#19
	["Un grand terrain vert s'étend devant vous avec quelques batîments à gauche, vous êtes caché derrière un tas de pierre","Aucun garde ne semble surveillé cet espace, ça doit être un terrain de golf","Traversé le terrain / Passer par les batîments"],#20 passé les chiens
	["BOOOOOM","","","","","Pendant le briefing, on vous avez dit qu'on pensait que la villa était piégé ?","Maintenant on sait qu'il y avait bien des mines"],#21
	["Bien le bâtiment n'est pas très large mais semble très long et relié jusqu'à la villa","Vous vous approchez d'une fenêtre pour regarder à l'intérieur","Il y a une salle qui ressemble à une salle de repos du personnel, un garde vient d'en sortir et la pièce est maintenant vide","Chercher autour des objets / Entrer par la fenêtre / Chercher une autre entrée"],#22 passé par les batiments, pas les mines
	["Il y a quelques débris qui trainent dans les alentours","Vous trouvez un vieux marteau rouillé !","Continuer à chercher / faire demi-tour"],#23 cherche obj
	[""],#24 passe par le fenêtre
	["Vous longez le bord gauche du batiement pour tenter de trouver un autre entrée","A part des fênetres il y a un porte mais qui semble régulièrement utilisée","Cependant vous apercevez un cabanon à gauche de se bâtiment","Vous pourriez l'atteindre en passant par le parking à gauche qui pourrai vous offrir une couverture","Aller vers le cabanon / Faire demi-tour / Aller vers la porte"],#25 cherche autre entrée
	["Vous vous avancez vers la porte"],#26 Tenter d'entré
	["Vous vous approchez ..."],#27 assomme sans marteau
	["Vous examinez les alentours pour trouver un objet qui pourrait vous aider","Cependant il n'y a pas grand chose dans la foret","Vous arrivez cependant à trouver une vielle lame de rasoir rouillée","Elle pourrait vous servir"],#28 exam les alentours
	["Vous arrivez à détruire le cadenas grâce au bâton que vous avez trouvez","A droite il y a un petit cabanon, surement pour ranger des outils","A gauche il y a la villa, vous pourriez vous en approcher en longeant le mur en profitant du noir de la nuit","Cabanon / Villa"],#29 milieu porte ouverte
	["La porte est cadenasser, il faudrait un outil pour l'ouvrir mais vous n'avez rien","Vous faites demi-tour"],#30 porte sans bâton
	["Vous courez jusqu'au cabanon, une petite bâtisse en bois sans fenêtre avec une unique porte","Vous ouvrez lentement la porte et passez votre tête pour voir l'intérieur","Il y a quelques outils entassé çà et là mais, il y a surtout un homme de dos en train de fouiller dans ce bazar","Vous l'assommez / refermez la porte en la bloquant / Attraper un outil"],#31 cabanon depuis la droite
	[""],#32 villa depuis grillage
	["Vous rampez le long du mur en vous cachant derrière les poubelles lorsque quelqu'un approche","Vous arrivez finalement devant la porte mais aucune fenêtre ne vous permet de savoir si la salle est vide ou non","Ouvrir la porte / faire demi-tour"],#33 porte
	["Vous prenez votre courage à deux mains et ouvrez la porte","PAF","Vous vous prenez un bouchon de bouteille dans l'oeuil et laissez échapper un cri","Les gardes qui fetaient un anniversaire ont finalement eu autre chose à faire"],#34 ouvir la porte
	["Vous faites demi-tour et repartez vers","Le cabanon / Le bout du bâtiment"],#35 demi tour
	["Vous courez de toute vos jambes en direction du cabanon","Quand soudain une puissante lumière vous éblouit, vous trébuchez sur un caillou et vous vous étalez de tout votre corps par terre"],#36 demi tour cabanon
	["Vous faites demi tour en direction du bout du bâtiment","Vous relongez le bâtiment en tentant de ne pas vous faire voir","Soudain un garde alla dans votre direction","Vous vous réfugiâtes dans le premier buisson venu","Qui aurait cru qu'un garde était en train de se vider la vessie sur ce même buisson ?"],#37 demi tour batiment
	["Vous cherchez un peu plus loin dans d'autre débris"],#38 fouille marteau continue
	["Vous prenez votre courage a deux main"],#39 Vous l'assommez
	[""],#40 refermez la porte en la bloquant
	[""],#41 Attraper un outil
	["Vous brandissez le marteau et fracassez le crâne du garde"],#42 assomme marteau
	["Vous brandissez le bâton et assénez un grand coup sur le crane du garde","Malheureusement un seul coup n'a pas suffi, et le garde se retourna après avoir repris rapidement ses esprits","Vous assénez un second coup, qui cette fois suffit à le mettre hors d'état de nuire"],#43 assomme bâton
	["Vous vous approchez du garde et tentez de lui tordre le coup","Un cri de douleur en suivant puis un soufflement de soulagement","Le garde se retourne et commence à vous remercier d'avoir régler ses problèmes de coup","En effet depuis longtemps il avait de problèmes au coup, cela remonte au jour où il est tombé d'un toit","Malheureuse chute mais nécessaire puisque par ce geste héroïque il réussit à sauver une classe d'enfant","Cette action lui permis ... EHH MAIS JE VOUS CONNAIS PAS VOUS ! ALERTE UN INTRUT !"],#44 assomme rien
	["Maintenant que la menace du garde a été écarté vous êtes seul dans le cabanon","Chercher autour / Fouiller le garde"],#45 post assomage
	[""],#46 cherche autour dans cabanon
	[""],#47 fouille garde cabanon
]

raccord = {
	"01":7,
	"02":-1,
	"11":3,
	"12":2,
	"21":-1,
	"22":5,
	"31":6,
	"32":4,
	"41":6,
	"42":3,
	"51":1,
	"52":-1,
	"61":8,
	"62":9,
	"71":1,
	"72":2,
	"81":9,
	"82":-1,
	"91":11,
	"92":10,
	"101":11,
	"102":9,
	"111":-1,
	"112":12,
	"113":13,
	"114":-1,
	"115":-1,
	"121":14,
	"131":14,
	"141":15,
	"142":16,
	"143":17,
	"161":-1,
	"171":26,
	"172":14,
	"173":28,
	"181":20,
	"191":-1,
	"201":21,
	"202":22,
	"211":-1,
	"221":23,
	"222":24,
	"223":25,
	"231":38,
	"232":22,
	"252":22,
	"251":31,
	"253":33,
	"281":14,
	"291":31,
	"292":32,
	"301":17,
	"331":34,
	"332":35,
	"341":-1,
	"351":36,
	"352":37,
	"361":-1,
	"371":-1,
	"381":21,
	"421":45,
	"431":45,
	"441":-1,
	"451":46,
	"452":47,
}

inventaire = {
	12:"bâton",
	28:"lame de rasoir",
	23:"marteau",
	42:"alarme garde",
	43:"alarme garde",
}

besoin = {
	16:["bâton",18,19],
	26:["bâton",29,30],
	39:["marteau",42,27],
	27:["bâton",43,44],
}
invVide = []

def bes(page):
	Npage = page
	stop = False
	if page in besoin:
		for obj in inv:
			if besoin[page][0] == obj:
				Npage = besoin[page][1]
				stop = True
			elif stop == False:
				Npage = besoin[page][2]
	if inv == invVide:
		Npage = besoin[page][2]
	return Npage

def hist(page):
	for i in range(len(event[page])):
		print(event[page][i])
	rep = ""
	while rep == "":
		rep = str(page)+input(">>> ")
	return rep

def ajoutInv(page):
	if page in inventaire:
		inv.append(inventaire[page])
		print("Nouvel objet : "+inventaire[page])

boucle = True
while boucle:
	r = "skregneugneu"
	while r not in raccord:
		r = hist(pageA) #affiche l'histoire
		ajoutInv(pageA)
		if pageA in besoin:
			#print("page num "+str(pageA))
			pageA = bes(pageA)
		else:
			try:
				pageA = raccord[r] 
				#ancien ajout inv 
			except:
				print("Je ne comprend pas ce que vous dîtes (EN CONSTRUCTION)")
		if r[len(r)-1] == "i":
			print("Votre inventaire : "+str(inv))
		print("")
	#print("page num "+str(pageA))
	if pageA < 0:
		boucle = False

for i in range(30):
	print("")
print("Aïe aïe aïe,")
print("Vos choix vous ont mené vers la fin de cette aventure")
print("Mais tout n'est pas fini ! Vous pouvez encore réécrire l'histoire")
input()