import urllib.parse, re

def generateUrl(search_term):
	try:
		new_term = urllib.parse.quote(search_term)
	except Exception as msg:
		print(msg)
	else:
		return 'https://chorus.fightthe.pw/search?query='+str(new_term)

def getGoogleID(link):
	try:
		letter_count = 0
		uid= ''
		for i in link:
			if i == '/':
				letter_count = 0
				uid = ''
			else:
				letter_count += 1
				uid += i
			if letter_count == 33:
				break
	except:
		print('eer')
	else:
		return uid

def extractName(content):
	name= ''
	name_add = False
	for i in content:
		if i == '"':
			if name_add:
				name_add = False
			else:
				name_add = True
		if name_add:
			name += i
	return name.replace('"','')
