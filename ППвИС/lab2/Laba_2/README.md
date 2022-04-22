tours = []

import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
 
 
for elem in root:
    newTour = Tournament()
    for subelem in elem:
        if subelem.tag == "name_tournament":
            newTour.setNameTournament(subelem.text)
        if subelem.tag == "date":
            newTour.setDate(subelem.text)
        if subelem.tag == "type_tournament":
            newTour.setTypeTournament(subelem.text)
        if subelem.tag == "fio":
            newTour.setFio(subelem.text)
        if subelem.tag == "price_tournament":
            newTour.setPriceTournament(subelem.text)
        if subelem.tag == "price_winner":
            newTour.setPriceWinner(subelem.text)
            
    tours.append(newTour)

for tour in tours:
    print(tour.getNameTournament())
    print(tour.getTypeTournament())
    print(tour.getDate())
    print(tour.getFio())
    print(tour.getPriceTournament())
    print(tour.getPriceWinner())

разница между UI IA что общего