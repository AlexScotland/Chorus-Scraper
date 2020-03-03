from downloader import *
sys.path.append("/usr/share/pyshared/song_request/python-files/")
##from database import db

if __name__ == '__main__':
    song=["","Through the Fire and the Flames","DragonForce","Dug"]
    songs = song[1]
    artist = song[2]
    requester = song[3]
    song_finder = songDownloader()
    try:
        song_finder.getFirstSong(song_finder.getQuery(str(songs)+" by "+str(artist)),song)
    except Exception as msg:
        print('err')
        print(msg)
    else:
        song_finder.quit()

##    cdb = db()
##    cdb.login()
##    for i in cdb.getAllReqSongs():
##        try:
##            song = i[1]
##            artist = i[2]
##            requester = i[3]
##            song_finder = songDownloader()
##            try:
##                song_finder.getFirstSong(song_finder.getQuery(str(song)+" by "+str(artist)),song)
##            except Exception as msg:
##                print('err')
##                print(msg)
##            else:
##                song_finder.quit()
##            
##        except Exception as msg:
##            print(msg)
##        finally:
##            cdb.removeReqSongbyReq(requester)
##            cdb.logout()
