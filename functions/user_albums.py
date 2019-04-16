def make_album(artist, album, num_of_tracks=''):
    the_album = {'artist': artist.title(), 'album': album.title()}

    if num_of_tracks:
        the_album['tracks'] = num_of_tracks

    return the_album

print("\n(Enter 'q' at any time to quit)")
while True:
    artist = input("\nEnter an artist: ")
    if artist.lower() == 'q':
        break

    album = input("Enter one of their albums: ")
    if album.lower() == 'q':
        break

    the_result = make_album(artist, album)
    print(the_result)