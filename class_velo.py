from class_fiets import *
from class_slot import *
from class_station import *
from class_gebruiker import *
from class_transporter import *
import json


class Velo:
    def __init__(self):
        self.stations = []
        self.fietsen = []
        self.gebruikers = []
        self.transporteurs = []

    def maak_stations_van_json(self):
        with open("velo.geojson", "r") as json_file:
            json_gegevens = json.load(json_file)

        for item in json_gegevens["features"]:
            naam = item["properties"]["Naam"]
            capaciteit = item["properties"]["Aantal_plaatsen"]
            station = Station(item["properties"]["Objectcode"], naam, capaciteit)
            station.maak_sloten()
            self.stations.append(station)

    def maak_fietsen(self):
        for i in range(1, 9950):
            fiets = Fiets(f"F{i}")
            self.fietsen.append(fiets)

    def maak_gebruikers(self):
        with open("namenlijst.json", "r") as json_file:
            json_gegevens = json.load(json_file)

        while len(self.gebruikers) < 55000:
            for index, item in enumerate(json_gegevens):
                naam = item["name"]
                gebruiker = Gebruiker(f"G{index}", naam, self)
                self.gebruikers.append(gebruiker)

    def maak_transporteurs(self):
        for i in range(1, 11):
            transporteur = Transporteur(i, self)
            self.transporteurs.append(transporteur)

    def plaats_fietsen_in_station(self):
        random.shuffle(self.stations)  # Meng de volgorde van de stations willekeurig
        random.shuffle(self.fietsen)  # Meng de volgorde van de fietsen willekeurig

        for station in self.stations:
            # Bepaal een willekeurig aantal fietsen om toe te wijzen aan dit station
            aantal_fietsen = random.randint(
                0, min(len(self.fietsen), station.aantal_beschikbare_slots())
            )

            for _ in range(aantal_fietsen):
                slot = next((s for s in station.sloten if s.beschikbaar), None)
                if slot:
                    slot.plaats_fiets(self.fietsen.pop())

    def __str__(self):
        return f"Velo heeft {len(self.stations)} stations, {len(self.fietsen)} fietsen en {len(self.gebruikers)} gebruikers."
