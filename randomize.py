import random

import randomize_resource

allchar = randomize_resource.paff+randomize_resource.nekow+randomize_resource.robohead+randomize_resource.ivy+randomize_resource.cp+randomize_resource.miku+randomize_resource.xenon+randomize_resource.conner+randomize_resource.cherry+randomize_resource.joe+randomize_resource.sagar+randomize_resource.rin+randomize_resource.aroma+randomize_resource.nora+randomize_resource.neko

def f_allchar():
	res =random.choice(allchar)
	return ">>> **" + str(res) + "**"
def f_free():
	res =random.choice(randomize_resource.free)
	return ">>> **" + str(res) + "**"

def f_paff():
	res =random.choice(randomize_resource.paff)
	return ">>> **" + str(res) + "**"
def f_nekow():
	res =random.choice(randomize_resource.nekow)
	return ">>> **" + str(res) + "**"
def f_robohead():
	res =random.choice(randomize_resource.robohead)
	return ">>> **" + str(res) + "**"
def f_ivy():
	res =random.choice(randomize_resource.ivy)
	return ">>> **" + str(res) + "**"
def f_cp():
	res =random.choice(randomize_resource.cp)
	return ">>> **" + str(res) + "**"
	
def f_miku():
	res =random.choice(randomize_resource.miku)
	return ">>> **" + str(res) + "**"
def f_xenon():
	res =random.choice(randomize_resource.xenon)
	return ">>> **" + str(res) + "**"
def f_conner():
	res =random.choice(randomize_resource.conner)
	return ">>> **" + str(res) + "**"
def f_cherry():
	res =random.choice(randomize_resource.cherry)
	return ">>> **" + str(res) + "**"
def f_joe():
	res =random.choice(randomize_resource.joe)
	return ">>> **" + str(res) + "**"
def f_sagar():
	res =random.choice(randomize_resource.sagar)
	return ">>> **" + str(res) + "**"
def f_rin():
	res =random.choice(randomize_resource.rin)
	return ">>> **" + str(res) + "**"

def f_aroma():
	res =random.choice(randomize_resource.aroma)
	return ">>> **" + str(res) + "**"
def f_nora():
	res =random.choice(randomize_resource.nora)
	return ">>> **" + str(res) + "**"
def f_neko():
	res =random.choice(randomize_resource.neko)
	return ">>> **" + str(res) + "**"

def f_capso():
	res =random.choice(randomize_resource.capso)
	return ">>> **" + str(res) + "**"
def f_bm():
	res =random.choice(randomize_resource.bm)
	return ">>> **" + str(res) + "**"

def f_glitch():
	res =random.choice(randomize_resource.glitch)
	return ">>> **" + str(res) + "**"
def f_xv():
	res =random.choice(randomize_resource.xv)
	return ">>> **" + str(res) + "**"
def f_xiv():
	res =random.choice(randomize_resource.xiv)
	return ">>> **" + str(res) + "**"

###

def rand(selection):
	switcher = {
		"all" : f_allchar(),
		"free" : f_free(),
		"paff" : f_paff(),
		"neko" : f_nekow(),
		"robo" : f_robohead(),
		"ivy" : f_ivy(),
		"cp" : f_cp(),

		"miku" : f_miku(),
		"xenon" : f_xenon(),
		"conner" : f_conner(),
		"cherry" : f_cherry(),
		"joe" : f_joe(),
		"sagar" : f_sagar(),
		"rin" : f_rin(),

		"aroma" : f_aroma(),
		"nora" : f_nora(),
		"nekopunk" : f_neko(),

		"capso" : f_capso(),
		"bm" : f_bm(),

		"glitch" : f_glitch(),
		"15" : f_xv(),
		"14" : f_xiv(),
		
		# lmao
		"graff" : "> CAPSO isn't **\*FREE\*** :confused:",
		"graffj" : "> CAPSO isn't **\*FREE\*** :confused:"
	}
	return switcher.get(selection, "*Check your input* :thinking:")
