import __future__
import os
import pickle as pik
import random as rand
import time as t
from   visual import *

L, H, W = 2, 2, 2
fps = 75

scene = display(title='MON MINECRAFT', x=75, y=45,
	width=840, height=680,
	center=(0,1,0), background=(0,1,1),
	userzoom=True, userspin=True)

#materials.rough
#materials.shiny
#materials.chrome
#materials.bricks
#materials.wood

carre    = []
todo     = []
liste_corresp = {
		'0' : materials.bricks,
		'1' : materials.shiny,
		'2' : materials.chrome,
		'3' : materials.wood,
		'4' : materials.rough,}
x, y, z  = 0, 0, 0
location = 0
matos    = materials.bricks
nb_bloc  = '0'
actual_material = materials.wood

if not os.path.exists("save.pkl"):
	for i in range(-16, 16, 2):
		for j in range(-16, 16, 2):
			k = rand.randrange(0, 4, 2)
			carre.append([(i, k, j), '0'])
			todo.append(box(pos=(i, k, j), length=L, height=H, width=W, material=materials.bricks))
else:
	todo = []
	with open("save.pkl", "rb") as save:
		unpickle = pik.Unpickler(save)
		carre = unpickle.load()
		for index, pos_carre in enumerate(carre):
			if carre[index][1] == '0':
				matos = materials.bricks
			if carre[index][1] == '1':
				matos = materials.shiny
			if carre[index][1] == '2':
				matos = materials.chrome
			if carre[index][1] == '3':
				matos = materials.wood
			if carre[index][1] == '4':
				matos = materials.rough
			todo.append(box(pos=carre[index][0], length=L, height=H, width=W, material=matos))

with open("save.pkl", "wb") as save:
	pickler = pik.Pickler(save)
	pickler.dump(carre)

while 1:
	rate(fps)
	if scene.kb.keys:
		key = scene.kb.getkey()
		if key == 'escape':
			with open("save.pkl", "wb") as save:
				pickler = pik.Pickler(save)
				for index, nombre in liste_corresp.items():
					if actual_material == nombre:
						nb_bloc = index
				carre.append([(x // 2 * 2, y // 2 * 2, z // 2 * 2), nb_bloc])
				pickler.dump(carre)
			exit()
	elif scene.mouse.clicked:
		"""mouse = scene.mouse.getclick()
		location = mouse.pos
		xs, ys, zs = location
		cam_dir = scene.mouse.camera
		xcam, ycam, zcam = location"""
		x, y, z = scene.mouse.ray
		print(x, y, z)
		#todo.append(box(pos=(x // 2 * 2, y // 2 * 2, z // 2 * 2), length=L, height=H, width=W, material=actual_material))
