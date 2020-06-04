def testa(abc=""):
	print("testado: "+abc)
	
exec('import time')

def data():
	return time.strftime('%Y/%m/%d')

def hora():
	return time.strftime('%H:%M:%S')

def now():
	return str(time.strftime('%Y/%m/%d %H:%M:%S'))
	
def str2bool(txt):
	if txt == '':
		return False
	return txt.lower() in ("yes", "true", "t", "1","y","sim")
	
	
def log(message0='',message1='',message2='',message3='',message4='',message5=''):
	print(str(message0),str(message1),str(message2),str(message3),str(message4),str(message5), file=fileoutput)

	if not cleanoutput:
		if message0=='' and message1=='' and message2=='' and message3=='' and message4=='' and message5=='':
			print('')
		else:
			if source!='c':
				print(str(message0),str(message1),str(message2),str(message3),str(message4),str(message5))
				pass
				#print(source+': ',str(message0),str(message1),str(message2),str(message3),str(message4),str(message5))
			else:
				print(str(message0),str(message1),str(message2),str(message3),str(message4),str(message5))
			#print(str(message0),str(message1),str(message2),str(message3),str(message4),str(message5))
	else:
		#print to file
		pass


def beta():
	try:
		own = os.getenv("CREATOR")
		log("")
		log(own)
	except Exception as e:
		raise e
	

