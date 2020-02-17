def calc(p, g, b, m, tp):
	p = float(p)
	g = float(g)
	b = float(b)
	m = float(m)
	tp = float(tp)
	t = p+g+b+m
	res = ( p*1 + g*0.3 + b*0 + m*0 - tp/100*t ) / 0.3
	res = round(res)

	if (p==0 and g==0 and b==0 and m==0 and tp==0.0):
		return "> No input detected. Type `?h cytus` for help :pensive:"
	elif (res==1):
		return ">>> There were ONLY **" + str(res) + "** Lemon Perfect :sweat: \nYou can do it :mechanical_arm:"
	elif (res<0):
		return "> Are you SURE? Check the input :thinking:"
	elif (res==0 and int(tp)==100):
		return "> You **TP100'd** :thinking:"
	else:
		return "> There were **" + str(res) + "** Lemon Perfects :neutral_face:"
