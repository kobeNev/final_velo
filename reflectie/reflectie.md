# Besluit velo systeem

# beschrijving

### gebruik

Wanneer je de applicatie opstart, kun je ervoor kiezen om dit te doen met het argument -s. In dat geval zal het programma meteen vragen of je verder wilt gaan met de vorige simulatie of een nieuwe wilt starten. Als je de applicatie opstart zonder argument, verschijnt er een menu in de terminal. Vanaf hier kun je kiezen uit de vier mogelijke opties: handmatig invoeren, simulatie starten, site genereren of de applicatie afsluiten.

### handmatig

Het systeem kan ook handmatig worden bediend door deze optie te kiezen. Eerst wordt gevraagd of je een fiets wilt lenen of terugbrengen. Dit geef je aan door middel van toetsenbordinvoer. Vervolgens moet je aangeven of je een transporteur of een gebruiker bent, en tot slot welk station. Dan wordt de actie uitgevoerd.

### simulatie

Het programma zal eerst vragen of je verder wilt gaan met de oude gegevens of een nieuwe simulatie wilt starten. Als je kiest voor een nieuwe simulatie, begint het programma met het uitlenen en terugbrengen van fietsen op de verschillende stations. En voor de oude laad het eerst de oude gegevens in en gaat het verder met de simulatie.

### argument

Je kan ook ervoor kiezen om -s erbij te typen bij start. Dan zal het programma rechtstreeks beginnen met de simulatie en slaag je het hele start scherm over.

### site genereren

De website is gegenereerd met behulp van Jinja en Markdown en heeft hiervoor een template. Om de site te bekijken, moet je het bestand 'template_output.html' openen met een live server. Hier vind je een overzicht van alle voorbije acties. Bij de transporteur komen het aantal fietsen erop ipv het id en de naam is de nummer die deze transporter heeft.

### afsluiten

Om het programma af te sluiten, moet je de optie "afsluiten" selecteren. Vervolgens zal het programma zich afsluiten en de gegevens opslaan in de JSON- en Pickle-bestanden.

# problemen

Het juist koppelen van alle principes heb ik het meeste moeite mee gehad. Want apart kon ik alles gemakelijk programeren. Maar vanaf dat ik het wou toevoegen aan het groter geheel kreeg ik al snel veel foutmeldingen. Bijvoorbeeld het juist toekennen van classes aan andere classes en deze vervolgens loggen.

### planning

Tijdens het jaar heb ik mij een beetje laten overrompelen door de mogelijkheden van Phyton.

Het is een taal die zo veel mogelijkheden heeft dat het voor mij moeilijk was om in eerste intstantie de structuur te doorzien.

Deze zomer ben ik echt opnieuw gestartt met het kijken van de lesvideo’s en het analyseren van de opdracht.

Het inzicht krijging in de taal heeft opnieuw tijd gevraagd maar ik heb de indruk dat door de aanmoedingingen van mijn omgeving, het automatiseren steeds beter gaat.

### complexiteit

Gedurende het jaar verliep het begrijpen van de opdracht behoorlijk moeizaam, wat resulteerde in minder succes. Gelukkig heb ik tijdens de herkansing veel extra inspanningen geleverd. Naarmate de tijd vorderde, begon ik de opdracht steeds beter te begrijpen en lukte het me om geleidelijk aan vooruitgang te boeken.

### nieuwe talen

Ik  zelf had wat moeite met het begrijpen van Jinja, Pickle en Markdown. Na het bekijken van voorbeelden en het uitvoeren van veel tests, was ik in staat om een website te maken die alle logs weergeeft op een mooie HTML-pagina. Hierbij heb ik veel foutmeldingen moeten oplossen.


- bestanden
    - [_site](https://github.com/kobeNev/final_velo/tree/main/_site)
        
        **[template_home.html](https://github.com/kobeNev/final_velo/blob/main/_site/template_home.html)**
        
        **[template_output.html](https://github.com/kobeNev/final_velo/blob/main/_site/template_output.html)**
        
    
    [class_fiets.py](https://github.com/kobeNev/final_velo/blob/main/class_fiets.py)
    
    [class_gebruiker.py](https://github.com/kobeNev/final_velo/blob/main/class_gebruiker.py)
    
    [class_log.py](https://github.com/kobeNev/final_velo/blob/main/class_log.py)
    
    [class_slot.py](https://github.com/kobeNev/final_velo/blob/main/class_slot.py)
    
    [class_station.py](https://github.com/kobeNev/final_velo/blob/main/class_station.py)
    
    [class_transporter.py](https://github.com/kobeNev/final_velo/blob/main/class_transporter.py)
    
    [class_velo.py](https://github.com/kobeNev/final_velo/blob/main/class_velo.py)
    
    [main.py](https://github.com/kobeNev/final_velo/blob/main/main.py)
    
    [namenlijst.json](https://github.com/kobeNev/final_velo/blob/main/namenlijst.json)
    
    [requirements.txt](https://github.com/kobeNev/final_velo/blob/main/requirements.txt)
    
    [velo.geojson](https://github.com/kobeNev/final_velo/blob/main/velo.geojson)