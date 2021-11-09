import unittest
from models.album import Album
from models.artist import Artist

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Brainbombs")
        self.album_1 = Album("Urge to Kill", "Noise Rock", self.artist)
        self.album_2 = Album("Obey", "Noise Rock", self.artist, 1)
        
    def test_album_has_title(self):
        self.assertEqual("Urge to Kill", self.album_1.title)

    def test_album_has_genre(self):
        self.assertEqual("Noise Rock", self.album_1.genre)

    @unittest.skip('')
    def test_album_has_artist(self):
        self.assertEqual(self.artist, self.album_1.artist)

    @unittest.skip('')
    def test_album_1_id_is_None(self):
        self.assertIsNone(self.album_1.id)

    @unittest.skip('')
    def test_album_2_has_id(self):
        self.assertEqual(1, self.album_2.id)