import urllib, urllib.request, requests, time, random, sys, os, zipfile, re ,io, smtplib, psycopg2
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode, quote_plus
from bs4 import BeautifulSoup
from helper import *
from webpageLoader import render
class songDownloader:
    def __del__(self):
        self.driver.quit()

    def getQuery(self,search_term):
        try:
            link=generateUrl(search_term)
        except Exception as msg:
            print(msg)
        else:
            print(link)
            return link

    def getFirstSong(self,link,request):
        try:
            song_charter = []
            requested_song_name = request
            html_raw = render(link)
            scraper=BeautifulSoup(html_raw)
            list_of_songs= scraper.findAll("div", {"class": "Song"})
            for i in list_of_songs:
                breaker = False
                song_element = i.findAll("div", {"class": "Song__name"})
                print(song_element)
                song_name = song_element[0].text
                print(song_name)
##                try:
##                    song_charter= i.find_element_by_class_name('DownloadLink')
##                except Exception as msg:
##                    song_charter= i.find_element_by_class_name('DownloadLink--verified')
##                finally:
##                    link = song_charter.find_element_by_tag_name('a')
##                    link=link.get_attribute('href')
##                    if 'https://public.fightthe.pw' in link:
##                        self.driver.get(link)
##                        os.system('wget '+link+' -P /home/Dug/songs_downloaded/')
##                    elif 'drive.google' in link:
##                        uid = getGoogleID(link)
##                        url = 'https://drive.google.com/uc?export=download&id='+str(uid)
##                        r = requests.get(url)
##                        if r.status_code == 404:
##                            breaker = False
##                        elif r.status_code == 200:
##                            breaker = True
##                            file_name = extractName(r.headers['Content-Disposition'])
##                            urllib.request.urlretrieve(url, '/home/Dug/songs_downloaded/'+str(file_name))
##                            # self.driver.get('https://drive.google.com/uc?export=download&id='+str(uid))
##                    if breaker:
                        break
        except Exception as msg:
            print(msg)
        else:
            return True
