def make_album(artist, album, num_of_tracks=''):
    the_album = {'artist': artist, 'album': album}

    if num_of_tracks:
        the_album['tracks'] = num_of_tracks

    return the_album

plus = make_album('ed sheeran', '+')
ten_thousand_days = make_album('tool', '10,000 Days', 11)
legend = make_album('bob marley', 'legend')

print(plus)
print(ten_thousand_days)
print(legend)