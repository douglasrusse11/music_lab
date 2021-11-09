from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository
import os 

os.system('psql -d music_collection -f db/music_collection.sql')

brainbombs = Artist("Brainbombs")
artist_repository.save(brainbombs)

boy_harsher = Artist("Boy Harsher")
artist_repository.save(boy_harsher)

urge_to_kill = Album("Urge to Kill", "Noise Rock", brainbombs)
album_repository.save(urge_to_kill)

obey = Album("Obey", "Noise Rock", brainbombs)
album_repository.save(obey)

burning_hell = Album("Burning Hell", "Noise Rock", brainbombs)
album_repository.save(burning_hell)

genius_and_brutality = Album("Genius and Brutality - Taste and Power", "Noise Rock", brainbombs)
album_repository.save(genius_and_brutality)

careful = Album("Careful", "Minimal Synth", boy_harsher)
album_repository.save(careful)

country_girl_uncut = Album("Country Girl Uncut", "Minimal Synth", boy_harsher)
album_repository.save(country_girl_uncut)

yr_body_is_nothing = Album("Yr Body Is Nothing", "Minimal Synth", boy_harsher)
album_repository.save(yr_body_is_nothing)

# artist_repository.delete_all()

# album_repository.delete_all()

test_artist = artist_repository.select(brainbombs.id)
print(test_artist.__dict__)