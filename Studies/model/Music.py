class Music:
    name = ''
    artist = ''
    duration = int
musica1= Music()
musica1.name = 'SLA'
musica1.artist = 'RAFAEL'
musica1.duration = 78

print(vars(musica1))
print(f'NAME {musica1.name} ARTIST {musica1.artist} DURATION{musica1.duration}')
