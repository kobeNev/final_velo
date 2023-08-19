from class_fiets import *
from class_slot import *
from class_station import *
from class_gebruiker import *
from class_log import *
from main import *

class Transporteur:
    def __init__(self, transporteur_id, velo):
        self.fietsen = []
        self.transporteur_id = transporteur_id
        self.velo = velo
        self.max_capaciteit = 20

    def neem_fietsen(self, station):
        if len(self.fietsen) < self.max_capaciteit:  # Check if capacity is not exceeded
            for slot in station.sloten:  # Iterate over slots in the given station
                if not slot.beschikbaar:
                    fiets = slot.verwijder_fiets(slot.fiets)
                    self.fietsen.append(fiets)
                    if len(self.fietsen) >= self.max_capaciteit:
                        break  # Stop adding bikes if capacity is reached
        else:
            print(f"Transporteur {self.transporteur_id} heeft al {len(self.fietsen)} fietsen.")
        print(f"Transporteur {self.transporteur_id} heeft {len(self.fietsen)} fietsen.")
        return self.fietsen

    def breng_fietsen(self, station):
        if len(self.fietsen) > 0:
            for slot in station.sloten:
                if slot.beschikbaar:
                    fiets = self.fietsen.pop()
                    slot.plaats_fiets(fiets)
                    if len(self.fietsen) <= 0:
                        break
        else:
            print(f"Transporteur {self.transporteur_id} heeft geen fietsen.")
        print(f"Transporteur {self.transporteur_id} heeft {len(self.fietsen)} fietsen afgezet.")
        return self.fietsen

    def __str__(self):
        return f"Transporteur {self.transporteur_id} heeft {len(self.fietsen)} fietsen."


    