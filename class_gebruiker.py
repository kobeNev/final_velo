from class_fiets import *
from class_slot import *
from class_station import *
import random

class Gebruiker:
    def __init__(self, gebruiker_id, naam, velo):
        self.gebruiker_id = gebruiker_id
        self.naam = naam
        self.max_capaciteit = 1
        self.fiets = []
        self.velo = velo

    def leen_fiets(self, fiets, station):
        if len(self.fiets) < self.max_capaciteit:
            random_fiets = random.choice(station.sloten)
            self.fiets.append(random_fiets.fiets)
            fiets_slot = None
            for station in self.velo.stations:
                for slot in station.sloten:
                    if slot.fiets == random_fiets.fiets:
                        fiets_slot = slot
                        break
                if fiets_slot:
                    fiets_slot.verwijder_fiets(random_fiets.fiets)
                    """print(
                        f"Fiets {fiets.fiets_id} geleend door {self.naam} uit slot {fiets_slot.slot_id}"
                    )"""
                else:
                    """print(f"Fiets {fiets.fiets_id} kon niet worden geleend.")"""
        else:
            """print(f"Gebruiker {self.naam} heeft al een fiets geleend.")"""
        return self.fiets

    def retourneer_fiets(self, fiets):
        if fiets in self.fiets:
            self.fiets.remove(fiets)
            for slot in random.choice((self.velo.stations).sloten):
                if slot.beschikbaar:
                    slot.plaats_fiets(fiets)
                    """print(
                        f"Fiets {fiets.fiets_id} teruggebracht door {self.naam} in slot {slot.slot_id}"
                    )"""
                    break
            else:
                """print(
                    f"Geen beschikbare sloten om de fiets {fiets.fiets_id} terug te brengen."
                )"""
        else:
            """print(f"Gebruiker {self.naam} heeft deze fiets niet geleend.")"""
