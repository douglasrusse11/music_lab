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