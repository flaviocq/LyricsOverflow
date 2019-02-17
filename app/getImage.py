


root_url = 'http://ws.audioscrobbler.com/2.0/'
API_KEY = '629789f756dd4b11673cd0988dbc9f96'
API_SECRET = '5545c2f0a4b176bac320b466faafa814'

import pylast


username = 'LeinadSN'
password_hash = pylast.md5("59!!colts")

def get_lastFM_info(artist_name):
    
    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, username=username, password_hash=password_hash)
    artist = network.get_artist(str(artist_name))
    
    
    artist_image = artist.get_cover_image()
    
    return artist_image
    