import urllib.parse

def generateUrl(search_term):
	try:
		new_term = urllib.parse.quote(search_term)
	except Exception as msg:
		print(msg)
	else:
		return 'https://chorus.fightthe.pw/search?query='+str(new_term)