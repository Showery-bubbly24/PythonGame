from Character import Character


class General:
    def mainWindow(self, character: Character):
        print(f"////////////////////////////////////////")
        print(f"////YOUR PERSON: {character['personName'] if character['personName'] else '?' * 16} //////")
        print(f"////YOUR ENDURANCE: {character['endurance'] if character['endurance'] else '?' * 3} ////////////////")
        print(f"////////////////////////////////////////")
        print(f"////////////YOUR//STATS/////////////////")
        print(f"///HEALTH: {character['health'] if character['health'] else 1}    //////////////////////")
        print(f"///ARMOR: {character['armor'] if character['armor'] else 0}     //////////////////////")
        print(f"///GOLD: {character['gold_value'] if character['gold_value'] else 0}       //////////////////////")
        print(f"////////////////////////////////////////")
        print(f"///STRENGTH: {character['strength'] if character['strength'] else '?' * 2}         /////////////////")
        print(f"///AGILITY: {character['agility'] if character['strength'] else '?' * 2}          /////////////////")
        print(
            f"///INTELLIGENCE: {character['intelligence'] if character['intelligence'] else '?' * 2}    /////////////////")
        print(f"////////////////////////////////////////")
        print(f"/////////////YOUR//INFO/////////////////")
        print(
            f"///SEX: {character['sex'] if character['sex'] else '?' * 6}  //////RACE: {character['race'] if character['race'] else '?' * 5}    ///")
        print(
            f"///MARRIED: {'True' if character['married'] else 'False'}  PARTNER_ID: {character['partner_id'] if character['partner_id'] else '?' * 5} ///")
