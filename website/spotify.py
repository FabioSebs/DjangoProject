import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Song():
    def __init__(self):
        pass
    
#for track in results['tracks'][:10]:
 #  print('audio    : ' + track['preview_url'])
 #  print('cover art: ' + track['album']['images'][0]['url'])
 
    def getSong(self, song="Blue Bird"):
        spotify = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(client_id = 'c4a27f3a84fe4b51a7f7cb2120f168f2', client_secret = '44c9944c109e4026adaaab101803bd9d'))
        
        ikomi = 'spotify:artist:5YneEA2nLtAhkD5t2769lZ'
        flow = 'spotify:artist:3w2HqkKa6upwuXEULtGvnY'
        anim = 'spotify:artist:4xJ8KBmZbjrLBagr9xNnyi'
        yui = 'spotify:artist:5WBO8UyOuJ1l7ZBqqBimpO'
        dbz = 'spotify:artist:6qTKdHuHW9MFnjfV3JYmz8'
        deathnote = 'spotify:artist:11CxpTfZC60MYKjL7HESKR'
        hunter = 'spotify:artist:2R1ubdXY4sUiDqsCtoAVUE'

        results = spotify.artist_top_tracks(ikomi)
        results2 = spotify.artist_top_tracks(flow)
        results4 = spotify.artist_top_tracks(anim)
        results5 = spotify.artist_top_tracks(yui)
        results6 = spotify.artist_top_tracks(dbz)
        results7 = spotify.artist_top_tracks(deathnote)
        results8 = spotify.artist_top_tracks(hunter)
        
        bluebird = results['tracks'][0],
        netsujo = results['tracks'][1],
        sign = results2['tracks'][0],
        again = results5['tracks'][0],
        totsegi = results4['tracks'][2],
        dbz = results6['tracks'][2],
        deathnote = results7['tracks'][0],
        departure = results8['tracks'][0]             
    
        return {
            'Blue Bird' : bluebird[0]['preview_url'],
            'Netsujo No Spectrum' : netsujo[0]['preview_url'],
            'Sign' : sign[0]['preview_url'],
            'Again' : again[0]['preview_url'],
            'Totsegi' : totsegi[0]['preview_url'],
            'DBZ' : dbz[0]['preview_url'],
            'DeathNote' : deathnote[0]['preview_url'],
            'Departure' : departure['preview_url'],
            }.get(song , 'song not available')
    
    
#swutch statement!!!
    
    
if __name__ == "__main__":
    pass
    
    