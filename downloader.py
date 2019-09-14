import urllib.request, requests, time, wget, random, os, zipfile, sys, re ,io, smtplib, psycopg2
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode, quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from helper import *
from database import *

class seleniumBrowser:
    def __init__(self):
        self.diva_db = db()
        self.options = Options()
        self.options.headless = True
        #self.options.log.level = "trace" #other options {fatal, error, warn, info(default), config, debug, trace}
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(2)

    def __del__(self):
        self.diva_db.logout()
        self.driver.quit()

    def getQuery(self,search_term):
        try:
            link=generateUrl(search_term)
            self.driver.get(link)
        except Exception as msg:
            print(msg)
        else:
            return True