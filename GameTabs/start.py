class Start:
    def startWindow(self):
        try:
            # Выбор имени
            print(f"////////////////////////////////////////")
            name = str(input("Enter name of your character: "))
            name = "_" * (16 - len(name)) + name
            print(f"////YOUR//NAME: {name} /////\n\n")

            # Выбор расы
            print(f"////////////RACE TYPES/////////////////////")
            print(f"////////////HUMAN: 1  /////////////////////")
            print(f"/Strength: 3 /Agility: 5 /Intelligence: 10/")
            print(f"///////////////////////////////////////////")
            print(f"////////////TROLL: 2  /////////////////////")
            print(f"/Strength: 5 /Agility: 10 /Intelligence: 5/")
            print(f"///////////////////////////////////////////")
            print(f"////////////_OGRE: 3  /////////////////////")
            print(f"/Strength: 10 /Agility: 5 /Intelligence: 3/")
            print(f"///////////////////////////////////////////")
            print(f"///////////////////////////////////////////")
            race = int(input("Enter number of race: "))
            match race:
                case 1:
                    race = 'Human'
                case 2:
                    race = 'Troll'
                case _:
                    race = '_Ogre'
            print(f"////YOUR//RACE: {race} /////\n\n")

            # Выбор пола
            print(f"////////////SEX TYPES//////////////////////")
            print(f"////////////MALE: 1////////////////////////")
            print(f"/Strength: +3 ///// Intelligence: -3///////")
            print(f"////////////Agility: +2////////////////////")
            print(f"///////////////////////////////////////////")
            print(f"////////////SEX TYPES//////////////////////")
            print(f"////////////FEMALE: 2//////////////////////")
            print(f"/Strength: -3 ///// Intelligence: +3///////")
            print(f"////////////Agility: +2////////////////////")
            print(f"///////////////////////////////////////////")
            print(f"///////////////////////////////////////////")
            gender = int(input("Enter number of gender: "))
            match gender:
                case 1:
                    gender = '__Male'
                case 2:
                    gender = 'Female'
            print(f"////YOUR//SEX: {gender} /////\n\n")

            # Концовка
            print(f"///////////////////////////////////////////")
            print(f"/////// !!! THANKS FOR PLAYING !!!  ///////")
            print(f"///////////////////////////////////////////\n\n\n")

            return name, race, gender
        except Exception as e:
            print('Wrong input!')
            return None
