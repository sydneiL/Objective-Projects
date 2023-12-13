#Bear Facts, a database dictionary where users can learn which about bears, the most dangerous land omnivores in the world
#Users can input different bears and learn about the diets,habitats, hibernation cycles, and hunting patterns specific to bears
#Built for CSC235@UAT
#Made by Sydnei Lang

#Dictionary Contents

bear_species_info = {

#polar bear info
    "Polar Bear": {
        "History": "Polar bears are native to the Arctic region.",#Polar bears are native to the Arctic region
        "Habitat": "Arctic and subarctic regions near sea ice.",#Arctic and subarctic regions near sea ice
        "Hibernation Pattern": "They don't truly hibernate but enter a state of reduced activity during winter.",#don't truly hibernate but enter a state of reduced activity during winter
        "Hunting Pattern": "Mainly seals, especially ringed and bearded seals.",#seals, especially ringed and bearded seals
        "Diet": "Mainly seals and fish.",#seals and fish
        "Behavior": "Excellent swimmers and hunters."#Excellent swimmers and hunters
    },
#grizzly bear info
    "Grizzly Bear": {
        "History": "Native to North America, they are also found in Europe and Asia.",#
        "Habitat": "Forests, mountains, and tundra.",#
        "Hibernation Pattern": "They hibernate during the winter months.",#
        "Hunting Pattern": "Berries, fish, small mammals, and carrion.",#
        "Diet": "Berries, fish, small mammals.",#
        "Behavior": "Solitary and opportunistic feeders."#
    },
#panda bear info
    "Panda Bear": {
        "History": "Found in China's mountainous regions.",#
        "Habitat": "Bamboo forests at high altitudes.",#
        "Hibernation Pattern": "They do not hibernate like other bears.",#
        "Hunting Pattern": "Primarily bamboo, occasional small rodents and birds.",#
        "Diet": "Primarily bamboo.",#
        "Behavior": "Gentle herbivores and excellent tree climbers."#
    }
}

# User Instructions
def display_intro():
    print("Welcome to the Bear Species Information Application!")
    print("This application provides detailed information about different bear species.")
    print("You can choose a bear species to learn more about or type 'exit' to quit the application.")

# Information about specific bear species
def get_bear_info(species_name):
    if species_name in bear_species_info:
        info = bear_species_info[species_name]
        print(f"\nSpecies: {species_name}")#name of bear species
        print(info["History"])#history of bear species
        print(f"Habitat: {info['Habitat']}")#habitat of bears
        print(f"Hibernation Pattern: {info['Hibernation Pattern']}")#hibernation of bears
        print(f"Hunting Pattern: {info['Hunting Pattern']}")#hunting patterns of bears
        print(f"Diet: {info['Diet']}")#diet of bears
        print(f"Behavior: {info['Behavior']}")#behavior of bears
    else:
        print("Bear species not found in the database.")#bear not found

if __name__ == "__main__":
    display_intro()#display intro
    
    while True:
        species_name = input("\nEnter the name of the bear species you want to learn about or 'exit' to quit: ")#enter name of bear species
        
        if species_name.lower() == "exit":
            print("Thank you for using the Bear Species Information Application. Goodbye!")#
            break
        else:
            get_bear_info(species_name)

#EndofBearFactsDictionary
#DictionaryClosed