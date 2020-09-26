def calc(p, g, b, m, tp):
	p = float(p)
	g = float(g)
	b = float(b)
	m = float(m)
	tp = float(tp)
	t = p+g+b+m
	#res = ( p*1 + g*0.3 + b*0 + m*0 - tp/100*t ) / 0.3
	#res = floor(res)
	res = 0
	while ((-30)*res > (tp+0.01)*t-100*p-30*g): 
		res = res+1

	if (p==0 and g==0 and b==0 and m==0 and tp==0.0):
		return "> No input detected. Type `?h cytus` for help :confused:"
	elif (p<0 or g<0 or b<0 or m<0 or tp<0.0 or res<0):
		return "> Wrong input :expressionless:"
	elif (res==1):
		return ">>> There was ONLY **" + str(res) + "** Lemon Perfect :pensive:"
	elif (res==0 and int(tp)==100):
		return "> You **TP100'd** :thinking:"
	else:
		return "> There were **" + str(res) + "** Lemon Perfects :neutral_face:"
