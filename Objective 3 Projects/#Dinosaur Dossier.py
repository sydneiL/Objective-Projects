#Dinosaur Dossier
#A database file full of information about the various theropod and sauropod dinosaur species that thrived from the Triassic to Cretaceous eras
#Built for CSC235@UAT
#Made by Sydnei Lang


import random
import pygame as pg

#Dinosaur Content
#Theropods
#Sauropods
dinosaur_database = {
    'Triassic': {              
        'Theropods': [
            {'Species': 'Herrerasaurus', 'Family': 'Herrerasauridae', 'Length': '3 meters', 'Fossils': 12},
            {'Species': 'Eoraptor', 'Family': 'Eoraptoridae', 'Length': '1 meter', 'Fossils': 18}
        ],
        'Sauropods': [
            {'Species': 'Plateosaurus', 'Family': 'Plateosauridae', 'Length': '8 meters', 'Fossils': 24}
        ]
    },
    'Jurassic': {
        'Theropods': [
            {'Species': 'Allosaurus', 'Family': 'Allosauridae', 'Length': '12 meters', 'Fossils': 32},
            {'Species': 'Dilophosaurus', 'Family': 'Dilophosauridae', 'Length': '6 meters', 'Fossils': 19}
        ],
        'Sauropods': [
            {'Species': 'Brachiosaurus', 'Family': 'Sauropodidae', 'Length': '23 meters', 'Fossils': 45},
            {'Species': 'Diplodocus', 'Family': 'Diplodocidae', 'Length': '27 meters', 'Fossils': 38}
        ]
    },
    'Cretaceous': {
        'Theropods': [
            {'Species': 'Tyrannosaurus Rex', 'Family': 'Tyrannosauridae', 'Length': '12 meters', 'Fossils': 62},
            {'Species': 'Spinosaurus', 'Family': 'Spinosauridae', 'Length': '16 meters', 'Fossils': 57}
        ],
        'Sauropods': [
            {'Species': 'Argentinosaurus', 'Family': 'Titanosauridae', 'Length': '30 meters', 'Fossils': 48},
            {'Species': 'Apatosaurus', 'Family': 'Diplodocidae', 'Length': '23 meters', 'Fossils': 41}
        ]
    }
}
#Dig For Dinos
# Function to find the species with the most excavated fossils
def find_dinosaur_with_most_fossils(database):
    most_fossils_count = 0
    most_fossils_species = ''

    for era, groups in database.items():
        for group, species_list in groups.items():
            for species_data in species_list:
                fossils = species_data['Fossils']
                if fossils > most_fossils_count:
                    most_fossils_count = fossils
                    most_fossils_species = species_data['Species']

    return most_fossils_species, most_fossils_count

#Results:
most_fossils_species, most_fossils_count = find_dinosaur_with_most_fossils(dinosaur_database)
print(f"The species with the most excavated fossils is {most_fossils_species} with {most_fossils_count} fossils.")
