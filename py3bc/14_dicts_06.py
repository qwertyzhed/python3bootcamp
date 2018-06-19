playlist = {
    'title': 'patagonia bus',
    'songs' : [
        {'title': 'song1', 'artist': ['fdgh'], 'album': 'albume', 'playtime': 2.30},
        {'title': 'dosdm', 'artist': ['floyd', 'fdgh'], 'album': 'brickinthewall', 'playtime': 10},
        {'title': 'meow', 'artist': ['garf'], 'album': 'fudl', 'playtime': 1}
    ]
}

for song in playlist['songs']:
    print(song['title'])


# name of playlist contains
    # song name
        # artist
        # album
        # playtime