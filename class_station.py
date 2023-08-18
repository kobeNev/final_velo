from class_slot import *
from class_fiets import *

class Station:
    def __init__(self, station_id, naam, capaciteit):
        self.station_id = station_id
        self.naam = naam
        self.sloten = []
        self.capaciteit = capaciteit
        self.maak_sloten()

    def maak_sloten(self):
        for i in range(self.capaciteit):
            slot = Slot(f"S{i}")
            self.sloten.append(slot)

    def aantal_beschikbare_slots(self):
        return len([slot for slot in self.sloten if slot.beschikbaar])

    def aantal_beschikbare_fietsen(self):
        return len([slot for slot in self.sloten if not slot.beschikbaar])

    def __str__(self):
        return f"{self.naam} heeft {self.aantal_beschikbare_slots()} vrije plaatsen, en {self.aantal_beschikbare_fietsen()} fietsen beschikbaar."

