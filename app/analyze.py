from musixmatch import Musixmatch
import re

def filter(t_lyrics):
    t_lyrics.pop('the', None)
    t_lyrics.pop('i', None)
    t_lyrics.pop('me', None)
    t_lyrics.pop('you', None)
    t_lyrics.pop('it', None)

    for letter in 'bcdefghijklmnopqrstuvwxyv':
        t_lyrics.pop(letter, None)

    return t_lyrics


def tokenize_song(song_lyrics, total_lyrics):
    for token in re.finditer('[a-z0-9]+', song_lyrics.lower()):
        token = token.group(0)
        if not re.match('(fuck.*)|(bitch)|(ass)|(nigga.*)', token):
            if token in total_lyrics:
                total_lyrics[token] += 1
            else:
                total_lyrics[token] = 1
    return total_lyrics


def rateEgo(total_lyrics):
    numerator = 0
    i_count = total_lyrics.get('i')

    if not i_count is None:
        numerator = i_count


    me_count = total_lyrics.get('i')

    if not me_count is None:
        numerator += me_count
    if numerator != 0:
        return int(100 * numerator/sum(total_lyrics.values()))
    else:
        return -1


def analyze_artist(artist_name):
    total_lyrics = dict()
    musixmatch = Musixmatch('25673f45b7887c52d089ab463d1b7562')
    search_term = artist_name

    result = (musixmatch.artist_search(search_term, 1, 5, 0, 0))
    # print(result)
    artist = result['message']['body']['artist_list'][0]['artist']

    #print(artist['artist_name'])
    artist_id = artist['artist_id']
    artist_name = artist['artist_name']
    albums = musixmatch.artist_albums_get(artist_id, 1, 15, 1, 'desc')['message']['body']['album_list']
    try:
        genre = albums[0]['album']['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name_extended']
    except IndexError:
        genre = 'N/A'
    for album in albums:
        album_id = album['album']['album_id']
        # try:
        # print('\t' + album['album']['album_name'])
        # except:
        # pass
        track_list = musixmatch.album_tracks_get(album_id, 1, 25, '')['message']['body']['track_list']

        for track in track_list:
            track_id = track['track']['track_id']
            # try:
            # print('\t\t' + track['track']['track_name'])
            # except:
            #    pass
            track_lyrics = musixmatch.track_lyrics_get(track_id)['message']['body']['lyrics']['lyrics_body']
            total_lyrics = tokenize_song(track_lyrics, total_lyrics)

    ego_rating = rateEgo(total_lyrics)

    unique_word_count = len(total_lyrics.keys())
    #print(unique_word_count)
    top_fifteen = sorted(filter(total_lyrics).items(), key=lambda t: (-t[1], t[0]))[0:15]

    return (artist_name, unique_word_count, genre, top_fifteen, ego_rating, total_lyrics)
    '''print('Unique words in vocabulary:' + str(unique_word_count))
    print('Top 15 most commonly used words of ' + artist['artist_name'] + ':')
    for k, v in sorted(filter(total_lyrics).items(), key=lambda t: (-t[1], t[0]))[0:15]:
        try:
            print(k + ': ' + str(v))
        except:
            pass
    '''
