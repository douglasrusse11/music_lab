import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    def test_artist_has_name(self):
        self.artist = Artist("Brainbombs")
        self.assertEqual("Brainbombs", self.artist.name)

    def test_artist_id_is_None(self):
        self.artist = Artist("Brainbombs")
        self.assertIsNone(self.artist.id)

    @unittest.skip('')
    def test_artist_has_id(self):
        self.artist = Artist("Brainbombs", 1)
        self.assertEqual(1, self.artist.id)