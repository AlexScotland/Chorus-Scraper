from downloader import *
sys.path.append("/usr/share/pyshared/song_request/python-files/")
from database import db

if __name__ == '__main__':
    cdb = db()
    cdb.login()
    for i in cdb.getAllReqSongs():
        try:
            song = i[1]
            artist = i[2]
            requester = i[3]
            song_finder = seleniumBrowser()
            if song_finder.getQuery(str(song)+" by "+str(artist)):
                song_finder.getFirstSong(song)
                song_finder.quit()
        except Exception as msg:
            print(msg)
        finally:
            cdb.removeReqSongbyReq(requester)
            cdb.logout()
