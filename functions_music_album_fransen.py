def make_album(artist_name, album_title, tracks=''):
    """Return a dictionary of information about a music album."""
    album = {'artist name': artist_name, 'album title': album_title}
    if tracks:
        album['number of tracks'] = tracks
    return album


music_album = make_album('fransen', 'here', tracks=12)
print(music_album)

music_album = make_album('fransen', 'there')
print(music_album)

music_album = make_album('fransen', 'void', tracks=10)
print(music_album)
