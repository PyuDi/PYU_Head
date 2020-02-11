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
		if (str(selection)=="all"):
			return f_allchar()
		elif (str(selection)=="free"):
			return f_free()
		
		elif (str(selection)=="paff"):
			return f_paff()
		elif (str(selection)=="neko"):
			return f_nekow()
		elif (str(selection)=="robo"):
			return f_robohead()
		elif (str(selection)=="ivy"):
			return f_ivy()
		elif (str(selection)=="cp"):
			return f_cp()

		elif (str(selection)=="miku"):
			return f_miku()
		elif (str(selection)=="xenon"):
			return f_xenon()
		elif (str(selection)=="conner"):
			return f_conner()
		elif (str(selection)=="cherry"):
			return f_cherry()
		elif (str(selection)=="joe"):
			return f_joe()
		elif (str(selection)=="sagar"):
			return f_sagar()
		elif (str(selection)=="rin"):
			return f_rin()

		elif (str(selection)=="aroma"):
			return f_aroma()
		elif (str(selection)=="nora"):
			return f_nora()
		elif (str(selection)=="nekopunk"):
			return f_neko()

		elif (str(selection)=="capso"):
			return f_capso()
		elif (str(selection)=="bm"):
			return f_bm()

		elif (str(selection)=="glitch"):
			return f_glitch()
		elif (str(selection)=="15"):
			return f_xv()
		elif (str(selection)=="14"):
			return f_xiv()
