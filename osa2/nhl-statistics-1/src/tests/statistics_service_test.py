import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytaa_pelaajan(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_palauttaa_none_jos_pelaajaa_ei_loydy(self):
        self.assertIsNone(self.stats.search("Selanne"))

    def test_team_palauttaa_joukkueen_pelaajat(self):
        players = self.stats.team("EDM")
        names = [player.name for player in players]
        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_tuntematon_joukkue_palauttaa_tyhjan_listan(self):
        self.assertEqual(self.stats.team("XXX"), [])

    def test_top_palauttaa_eniten_pisteita_tehneen_ensin(self):
        top = self.stats.top(1)
        self.assertEqual(top[0].name, "Gretzky")

    def test_top_palauttaa_pyydetyn_maaran_pelaajia(self):
        self.assertEqual(len(self.stats.top(3)), 3)