from Character import Character
import pickle


def rewrite(character: Character):
    with open('saved_data', 'wb') as file:
        pickle.dump(character, file)


def new_moves():
    print(f"////////////////////////////////////////")
    print(f"////////////////////////////////////////")
    print(f"////////////COMMAND///TYPES/////////////")
    print(f"/// 9 - Go to general screen  //////////")
    print(f"/// 0 - Exit from game  ////////////////")
    print(f"/// 1 - Go home         ////////////////")
    print(f"/// 2 - Go to tavern    ////////////////")
    print(f"/// 5 - Show inventory  ////////////////")
    print(f"////////////////////////////////////////")
    print(f"////////////////////////////////////////")
    command = int(input("Choose your move: "))

    return command


def switch_page(func):
    def wrapper(self, character: Character):
        func(self, character)
        return new_moves()

    return wrapper
