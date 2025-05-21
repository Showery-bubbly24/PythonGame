# Base imports
import pickle

# GameTabs imports
from GameTabs.start import Start
from GameTabs.general import General
from GameTabs import general, homeTab, tavernTab, inventoryTab

# Moves imports
from moves import new_moves, switch_page

page_dict = {
    1: homeTab.Home().homeWindow,
    2: tavernTab.Tavern().tavernWindow,
    5: inventoryTab.Inventory().inventoryWindow
}


def start_game():
    """
    Main game logics
    :return: Nothing
    """
    try:
        with open(f'saved_data', 'rb') as file:
            person = pickle.load(file)

    except Exception as e:
        print('No saved data. Lets create your new character')
        res = Start().startWindow()

        while res is None:
            print('Try again!')
            res = Start().startWindow()

        personName, race, sex = res

        person: Character = {
            "personName": personName,
            "endurance": 100,
            "health": 100,
            "armor": 1.0,
            "gold_value": 100,
            "strength": (10 if race == '_Ogre' else 5 if race == 'Troll' else 3) + (3 if sex == '__Male' else 0),
            "agility": (10 if race == 'Troll' else 5) + 2,
            "intelligence": (10 if race == 'Human' else 5 if race == 'Troll' else 3) + (3 if sex == 'Female' else 0),
            "sex": sex,
            "race": race,
            "married": False,
            "partner_id": '_None',
            "inventory": {}
        }

        with open('saved_data', 'wb') as file:
            pickle.dump(person, file)
    finally:
        General().mainWindow(
            person
        )

        command = new_moves()

    while True:
        if 1 <= command <= 5:
            command = page_dict[command](person)
        elif command == 0:
            general.General().mainWindow(person)
            command = new_moves()
        else:
            return None


if __name__ == "__main__":
    start_game()
