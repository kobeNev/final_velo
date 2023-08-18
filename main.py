import json
import random
import time
import pickle
import os
import sys
from jinja2 import Environment, FileSystemLoader
from class_fiets import *
from class_slot import *
from class_station import *
from class_gebruiker import *
from class_velo import *
from class_log import *

class Simulatie:
    def __init__(self):
        self.log = Log("full_data.json")
        """print("Log object aangemaakt")"""
        self.velo = Velo()
        """print("Velo object aangemaakt")"""
        self.velo.maak_stations_van_json()
        """print("Stations aangemaakt")"""
        self.velo.maak_fietsen()
        """print("Fietsen aangemaakt")"""
        self.velo.maak_gebruikers()
        """print("Gebruikers aangemaakt")"""
        self.velo.plaats_fietsen_in_station()
        """print("Fietsen in stations geplaatst")"""

    def start(self):
        for gebruiker in self.velo.gebruikers:
            if random.random() < 0.5:
                station = random.choice(self.velo.stations)
                if station.aantal_beschikbare_fietsen() > 0:
                    slot = random.choice(station.sloten)
                    if not slot.beschikbaar:
                        if slot.fiets is not None:  # Check if the slot has a bike
                            fiets_id = slot.fiets.fiets_id #zodat het geen null object doorgeeft
                            gebruiker.leen_fiets(slot.fiets, station)  # Lease the bike
                            self.log.uit_fiets_gebruiker(station.naam, gebruiker.naam, fiets_id)
                            print(
                                f"Gebruiker {gebruiker.naam} leent fiets {fiets_id} uit station {station.naam}"
                            )
                            break

    def stop(self):
        for gebruiker in self.velo.gebruikers:
            if gebruiker.fiets:  # Check if the user has a bike
                if gebruiker.fiets[0] is not None:
                    fiets_id = gebruiker.fiets[0].fiets_id #zodat het geen null object doorgeeft
                    station = random.choice(self.velo.stations)
                    if station.aantal_beschikbare_slots() > 0:
                        slot = random.choice(station.sloten)
                        if slot.beschikbaar:
                            slot.plaats_fiets(gebruiker.fiets)  # Return the bike to the slot
                            self.log.in_fiets_gebruiker(station.naam, gebruiker.naam, fiets_id)
                            print(
                                f"Gebruiker {gebruiker.naam} retourneert fiets {fiets_id} bij station {station.naam}"
                            )
                            break

    def stop_velo(self):
        print("\nKeyboardInterrupt gedetecteerd. Data wordt opgeslagen...")
        with open('velo_data.pkl', 'wb') as f:
            pickle.dump(sim_program.velo, f)
        sim_program.log.opslaan_bestand()
        print("Data saved. Exiting...")
        sys.exit(0)

def generate_html(bike_movements):
    # Initialize Jinja2 environment
    bike_movements = json.load(open(bike_movements, "r"))
    env = Environment(loader=FileSystemLoader("C:/Users/koben/OneDrive/AP/2de semester/Pyhton OOP ☺/exam_prep/_site")
                      , trim_blocks=True, lstrip_blocks=True)

    output_filename = f"_site/template_output.html"

    template = env.get_template("template_home.html")

    # Render the HTML template with bike movement data
    rendered_html = template.render(bike_movements=bike_movements)

    # Write the rendered HTML to the unique file
    with open(output_filename, "w") as output_file:
        output_file.write(rendered_html)

    print(f"HTML file '{output_filename}' generated successfully.")


def clear():
    os.system("cls") # Ingesteld op Windows, voor Linux(mac): os.system("clear")


if __name__ == "__main__":
    try:
        clear()
        print("             Welkom bij Velo!")
        print("Het beste fietsverhuurbedrijf van Antwerpen!")
        input("        Druk op enter om verder te gaan.")
        clear()
        sim_program = Simulatie()

        while True:
            print("      Wat wilt u doen?:")
            print("    H: Handmatig invoeren")
            print("   S: Een simulatie starten")
            print("     G: De site genereren")
            keuze = (input("   Q: de toepassing stoppen     \n")).upper()
            if keuze == "H":
                clear()
                print("U koos voor handmatig invoeren.")
                type = input("Wilt u een fiets lenen of terugbrengen? (L/T) ").upper()
                if type == "L":
                    clear()
                    print("U koos voor een fiets lenen.")
                    persoon = input("bent u een gebruiker of een transporteur? (G/T) ").upper()
                    naam = input("Wat is uw naam? ")
                    station = input("Bij welk station bent u? [1, 311]")
                    if persoon == "G":
                      #manier om de fiets uit te lenen
                        print("U heeft de fiets uitgeleend.")
                if type == "T":
                    clear()
                    print("U koos voor een fiets terugbrengen.")
                    naam = input("Wat is uw naam? ")
                    station = input("Bij welk station bent u? [1, 311]")
                    print("U heeft de fiets teruggebracht.")
                break
            if keuze == "S":
                clear()
                voortgang = input("U koos voor een simulatie starten, wilt u verder gaan op de oude simulatie of een nieuwe starten? (O/N) ").upper()
                if voortgang == "N":
                    print("U koos voor een nieuwe simulatie.")
                    print("U kan de simulatie op elk moment stoppen door op CTRL+C te drukken.")
                    tijd = input("Hoe snel wilt u de simulatie laten lopen? [1,100] ")

                    try:
                        while True:
                            option = random.randint(1, 3)
                            time.sleep(1 / int(tijd))
                            if option == 2:
                                sim_program.start()
                            if option == 3:
                                sim_program.stop()

                    except KeyboardInterrupt:
                        sim_program.stop_velo()
                    break
                if voortgang == "O":
                    print("U koos voor verder gaan op vorige simulatie.")
                    try:
                        with open('velo_data.pkl', 'rb') as f:
                            saved_velo = pickle.load(f)
                            Velo = saved_velo
                            print("Vorige simulatie is ingeladen.")
                    except FileNotFoundError:
                        print("Geen vorige simulatiegegevens gevonden.")
            if keuze == "G":
                clear()
                print("De site word gegenereerd.")
                generate_html(bike_movements = "full_data.json")
                break
            if keuze == "Q":
                clear()
                print("De toepassing word gestopt.")
                break
            else:
                clear()
                print("U heeft geen geldige input gegeven. Probeer het opnieuw.")
            
            sim_program.stop_velo()
   
    except KeyboardInterrupt:
        sim_program.stop_velo()

#om bij te houden

#print(self.velo.fietsen[1])