import random

import randomize_resource as r

allchar = r.paff+r.nekow+r.robohead+r.ivy+r.cp+r.vanessa+r.bobo+r.miku+r.ai+r.alice+r.xenon+r.conner+r.cherry+r.joe+r.sagar+r.rin+r.aroma+r.nora+r.neko

def f_allchar():
	res =random.choice(allchar)
	return ">>> **" + str(res) + "**"
def f_free():
	res =random.choice(r.free)
	return ">>> **" + str(res) + "**"

def f_paff():
	res =random.choice(r.paff)
	return ">>> **" + str(res) + "**"
def f_nekow():
	res =random.choice(r.nekow)
	return ">>> **" + str(res) + "**"
def f_robohead():
	res =random.choice(r.robohead)
	return ">>> **" + str(res) + "**"
def f_ivy():
	res =random.choice(r.ivy)
	return ">>> **" + str(res) + "**"
def f_cp():
	res =random.choice(r.cp)
	return ">>> **" + str(res) + "**"
def f_vanessa():
	res =random.choice(r.vanessa)
	return ">>> **" + str(res) + "**"
def f_bobo():
	res =random.choice(r.bobo)
	return ">>> **" + str(res) + "**"

def f_miku():
	res =random.choice(r.miku)
	return ">>> **" + str(res) + "**"
def f_ai():
	res =random.choice(r.ai)
	return ">>> **" + str(res) + "**"
def f_alice():
	res =random.choice(r.alice)
	return ">>> **" + str(res) + "**"
def f_xenon():
	res =random.choice(r.xenon)
	return ">>> **" + str(res) + "**"
def f_conner():
	res =random.choice(r.conner)
	return ">>> **" + str(res) + "**"
def f_cherry():
	res =random.choice(r.cherry)
	return ">>> **" + str(res) + "**"
def f_joe():
	res =random.choice(r.joe)
	return ">>> **" + str(res) + "**"
def f_sagar():
	res =random.choice(r.sagar)
	return ">>> **" + str(res) + "**"
def f_rin():
	res =random.choice(r.rin)
	return ">>> **" + str(res) + "**"

def f_aroma():
	res =random.choice(r.aroma)
	return ">>> **" + str(res) + "**"
def f_nora():
	res =random.choice(r.nora)
	return ">>> **" + str(res) + "**"
def f_neko():
	res =random.choice(r.neko)
	return ">>> **" + str(res) + "**"

def f_capso():
	res =random.choice(r.capso)
	return ">>> **" + str(res) + "**"
def f_bm():
	res =random.choice(r.bm)
	return ">>> **" + str(res) + "**"

def f_glitch():
	res =random.choice(r.glitch)
	return ">>> **" + str(res) + "**"
def f_xv():
	res =random.choice(r.xv)
	return ">>> **" + str(res) + "**"
def f_xiv():
	res =random.choice(r.xiv)
	return ">>> **" + str(res) + "**"
def f_xiii():
	res =random.choice(r.xiii)
	return ">>> **" + str(res) + "**"
def f_xii():
	res =random.choice(r.xii)
	return ">>> **" + str(res) + "**"
def f_xi():
	res =random.choice(r.xi)
	return ">>> **" + str(res) + "**"
def f_x():
	res =random.choice(r.x)
	return ">>> **" + str(res) + "**"
def f_ix():
	res =random.choice(r.ix)
	return ">>> **" + str(res) + "**"
def f_viii():
	res =random.choice(r.viii)
	return ">>> **" + str(res) + "**"

### debug
'''
def f_bychar():
	return allchar
def f_bydiff():
	return r.glitch+r.xv+r.xiv+r.xiii+r.xii+r.xi+r.x+r.ix+r.viii
def f_bysong():
	return r.free+r.capso+r.bm
'''
###

def rand(selection):
	switcher = {
		"all" : f_allchar(),
		"a" : f_allchar(),
		"free" : f_free(),
		"f" : f_free(),
		
		"paff" : f_paff(),
		"neko" : f_nekow(),
		"robo" : f_robohead(),
		"robohead" : f_robohead(),
		"ivy" : f_ivy(),
		"cp" : f_cp(),
		"crystalpunk" : f_cp(),
		"punk" : f_cp(),
		"vanessa" : f_vanessa(),
		"bobo" : f_bobo(),

		"miku" : f_miku(),
		"ai" : f_ai(),
		"kizuna" : f_ai(),
		"alice" : f_alice(),
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
		"c" : f_capso(),
		"bm" : f_bm(),
		"b" : f_bm(),

		"glitch" : f_glitch(),
		"g" : f_glitch(),
		"15" : f_xv(),
		"14" : f_xiv(),
		"13" : f_xiii(),
		"12" : f_xii(),
		"11" : f_xi(),
		"10" : f_x(),
		"9" : f_ix(),
		"8" : f_viii(),
		
		# debug
		# "bychar" : f_bychar(),
		# "bydiff" : f_bydiff(),
		# "bysong" : f_bysong(),

		# lmao
		"graff" : "> CAPSO isn't **\*FREE\*** :confused:",
		"graffj" : "> CAPSO isn't **\*FREE\*** :confused:"
	}
	return switcher.get(selection, "*Check your input* :thinking:")
