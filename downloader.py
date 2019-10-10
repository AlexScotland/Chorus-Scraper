import urllib, urllib.request, requests, time, random, os, zipfile, sys, re ,io, smtplib, psycopg2
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode, quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from helper import *

class seleniumBrowser:
    def __init__(self):
        self.options = Options()
        self.cap = DesiredCapabilities().FIREFOX
        self.cap["marionette"] = True
        self.options.headless = True
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference('browser.download.folderList', 2) # custom location
        self.profile.set_preference('browser.download.manager.showWhenStarting', False)
        self.profile.set_preference('browser.download.dir','/home/Dug/songs_downloaded/')
        self.profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip, application/rar')
        self.profile.set_preference("pdfjs.disabled", True)
        self.profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        self.driver = webdriver.Firefox(self.profile,executable_path='/usr/share/pyshared/chorus_downloader/geckodriver', service_log_path='/dev/null',capabilities=self.cap, options=self.options)
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(2)

    def __del__(self):
        self.driver.quit()

    def quit(self):
        self.driver.quit()

    def getQuery(self,search_term):
        try:
            link=generateUrl(search_term)
            self.driver.get(link)
        except Exception as msg:
            print(msg)
        else:
            return True

    def getFirstSong(self,request):
        try:
            song_charter = []
            requested_song_name = request
            list_of_songs=self.driver.find_elements_by_class_name("Song")
            for i in list_of_songs:
                breaker = False
                song_element = i.find_element_by_class_name("Song__name")
                song_name = song_element.get_attribute("innerText")
                try:
                    song_charter= i.find_element_by_class_name('DownloadLink')
                except Exception as msg:
                    song_charter= i.find_element_by_class_name('DownloadLink--verified')
                finally:
                    link = song_charter.find_element_by_tag_name('a')
                    link=link.get_attribute('href')
                    if 'https://public.fightthe.pw' in link:
                        self.driver.get(link)
                        os.system('wget '+link+' -P /home/Dug/songs_downloaded/')
                    elif 'drive.google' in link:
                        uid = getGoogleID(link)
                        url = 'https://drive.google.com/uc?export=download&id='+str(uid)
                        r = requests.get(url)
                        if r.status_code == 404:
                            breaker = False
                        elif r.status_code == 200:
                            breaker = True
                            file_name = extractName(r.headers['Content-Disposition'])
                            urllib.request.urlretrieve(url, '/home/Dug/songs_downloaded/'+str(file_name))
                            # self.driver.get('https://drive.google.com/uc?export=download&id='+str(uid))
                    if breaker:
                        break
        except Exception as msg:
            print(msg)
        else:
            return True
