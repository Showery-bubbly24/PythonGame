from Character import Character
from moves import switch_page, rewrite


def overSwapper(hour: int):
    def decorator(func):
        def wrapper(*args):  # Matches sleep()'s signature
            print(f"////////////////////////////////////////")
            print(f" === YOU SLEEPING: {hour} hours === ")  # Use hour from decorator
            print(f"////////////////////////////////////////")

            func(args[0])  # Call original function

            print(f" === AFTER SOME TIME... === ")
            print(f" ::: +80 endurance ::: ")

        return wrapper
    return decorator


@overSwapper(8)
def sleep(character: Character):
    if character['endurance'] <= 20:
        character['endurance'] += 80
    else:
        character['endurance'] = 100
    rewrite(character)


class Home:
    @switch_page
    def homeWindow(self, character: Character):
        print(f"////////////////////////////////////////")
        print(f"//////////  YOU ARE HOME  //////////////")
        print(f"////////////////////////////////////////")

        self.choose_sleep_time(character)
        return

    def choose_sleep_time(self, character: Character):
        sure = input("You want sleep?: ")
        match sure:
            case "Yes" | "y":
                sleep(character)
            case _:
                return
