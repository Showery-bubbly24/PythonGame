from Character import Character
from moves import switch_page


class Inventory:
    @switch_page
    def inventoryWindow(self, character: Character):
        print(f"////////////////////////////////////////")
        print(f"/////////  YOUR INVENTORY  /////////////")
        print(f"////////////////////////////////////////")

        for category, item_data in character['inventory'].items():
            print(f" +++  {category}: {item_data}  +++ ")

        print(f"////////////////////////////////////////")