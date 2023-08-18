import json

class Log:
    def __init__(self, bestand):
        self.bestand = bestand
        self.lijst = []

    def in_fiets_transporteur(self, station, aantal_fietsen, transporteur_id):
        diction = {"type": "transporteur", "actie": "in", "station": station.naam,
                   "aantal fietsen": aantal_fietsen, "id": transporteur_id}
        self.lijst.append(diction)

    def uit_fiets_transporteur(self, station, aantal_fietsen, transporteur_id):
        diction = {"type": "transporteur", "actie": "uit", "station": station.naam,
                   "aantal fietsen": aantal_fietsen, "id": transporteur_id}
        self.lijst.append(diction)

    def in_fiets_gebruiker(self, station, naam, fiets):
        fiets_id_in = str(fiets) #zodat het geen null object doorgeeft
        diction = {"type": "gebruiker", "actie": "in", "station": station, "naam": naam, "fiets_id": fiets_id_in}
        self.lijst.append(diction)

    def uit_fiets_gebruiker(self, station, naam, fiets):
        fiets_id_uit = str(fiets) #zodat het geen null object doorgeeft
        diction = {"type": "gebruiker", "actie": "uit", "station": station, "naam": naam, "fiets_id": fiets_id_uit}
        self.lijst.append(diction)

    def opslaan_bestand(self):
        with open(self.bestand, "w") as json_file:
            json.dump(self.lijst, json_file)

    def uitelezen_bestand(self):
        with open(self.bestand, "r") as json_file:
            json_gegevens = json.load(json_file)
        for item in json_gegevens:
            print(item)