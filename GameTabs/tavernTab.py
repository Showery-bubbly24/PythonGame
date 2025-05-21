from Character import Character
from moves import switch_page, rewrite
import random

store_inventory = {
    'weapon': {
        1: [('bronze_sword', 3), 5, 5],
        2: [('silver_sword', 3), 5, 15],
        3: [('diamond_sword', 3), 5, 25],
        4: [('standard_bow', 3), 5, 30]
    },
    'armory': {
        1: [('iron_helmet', 0.8), 5, 20],
        2: [('iron_body_guard', 3), 5, 50],
        3: [('iron_pants', 1.5), 5, 30],
        4: [('standard_boots', 0.5), 5, 15]
    },
    'books': {
        1: [('intelligence_book', 3), 5, 75],
        2: [('agility_book', 3), 5, 75],
        3: [('strength_book', 3), 5, 75],
    }
}


def tavern_choose(func):
    def wrapper(self):
        func(self)

        print(f"////////////////////////////////////////")
        print(f"/ - Hello, my friend! Can I help you? //")
        print(f"////////////////////////////////////////")

        print(f"////////////////////////////////////////")
        print(f"/ 1 - Yes, I want to buy something... //")
        print(f"/ 0 - No...                           //")
        print(f"////////////////////////////////////////")
        command = int(input("Enter number: "))
        return command

    return wrapper


class Tavern:
    @tavern_choose
    def default_scene(self):
        print(f"////////////////////////////////////////")
        print(f"/////////  YOU ARE IN TAVERN  //////////")
        print(f"////////////////////////////////////////")

    @tavern_choose
    def promotion_scene(self):
        print(f"////////////////////////////////////////")
        print(f"/////////  YOU ARE LUCKY !!!  //////////")
        print(f"/// - You got 5 gold !        //////////")
        print(f"////////////////////////////////////////")

    @tavern_choose
    def hitting_scene(self):
        print(f"////////////////////////////////////////")
        print(f"////////  YOU ARE UNLUCKY !!!  /////////")
        print(f"/// - Someone hit you!        //////////")
        print(f"////////////////////////////////////////")

    @tavern_choose
    def fight_scene(self):
        print(f"////////////////////////////////////////")
        print(f"////////  YOU ARE UNLUCKY !!!  /////////")
        print(f"/// - Someone fight with you!  /////////")
        print(f"/// - You got -20 health       /////////")
        print(f"////////////////////////////////////////")

    @switch_page
    def tavernWindow(self, character: Character):
        scene_dict = {
            1: self.default_scene,
            2: self.promotion_scene,
            3: self.hitting_scene,
            4: self.fight_scene
        }
        if random_scene := random.choices([1, 2, 3, 4], weights=[80, 10, 7, 3])[0]:
            cmd = scene_dict[random_scene]()

        match cmd:
            case 1:
                self.open_buy_store(character)
            case _:
                return None

    def open_buy_store(self, character):
        try:
            print(f"\n\n////////////////////////////////////////")
            print(f"/ - Choose what you want !)    /////////")
            print(f"////////////////////////////////////////")

            def item_list(item_id, item_data):
                name, value = item_data[0]  # Unpack the tuple (name, damage/armor/stat value)
                quantity = item_data[1]
                price = item_data[2]

                print(f"////////////////////////////////////////")
                print(f"/// ID: {item_id}")
                print(f"/// Name: {name}")
                print(f"/// Value: +{value}")
                print(f"/// Quantity: {quantity}")
                print(f"/// Price: {price}")
                print(f"////////////////////////////////////////")

            # Display all items by category
            for category in store_inventory:
                print(f"\n      === {category.upper()} ===     ")
                for item_id, item_data in store_inventory[category].items():
                    item_list(item_id, item_data)

            # Получаем ввод пользователя
            print("\nEnter items to buy (format: category_id_quantity, separated by space)")
            print("Example: weapon_1_2 armory_3_1")
            purchase_input = input("Your order: ").strip()

            if not purchase_input:
                print("Purchase canceled!")
                return

            # Обрабатываем покупку
            total_cost = 0
            purchase_items = []

            # Разбиваем ввод на отдельные покупки
            for purchase in purchase_input.split():
                try:
                    category, item_id, quantity = purchase.split('_')
                    item_id = int(item_id)
                    quantity = int(quantity)

                    # Проверяем существование категории и предмета
                    if category not in store_inventory:
                        print(f"Invalid category: {category}")
                        return

                    if item_id not in store_inventory[category]:
                        print(f"Invalid item ID: {item_id} in category {category}")
                        return

                    item = store_inventory[category][item_id]
                    item_name = item[0][0]
                    available_quantity = item[1]
                    price = item[2]

                    # Проверяем количество
                    if quantity <= 0:
                        print(f"Invalid quantity for {item_name}: {quantity}")
                        return

                    if quantity > available_quantity:
                        print(f"Not enough {item_name} in stock! (Available: {available_quantity})")
                        return

                    # Добавляем к общей стоимости
                    total_cost += price * quantity
                    purchase_items.append({
                        'category': category,
                        'item_id': item_id,
                        'name': item_name,
                        'quantity': quantity,
                        'price': price,
                        'item_data': item
                    })

                except ValueError:
                    print(f"Invalid input format: {purchase}. Use format category_id_quantity")
                    return

            # Проверяем деньги
            if character['gold_value'] < total_cost:
                print(f"Not enough gold! Need: {total_cost}, Have: {character['gold_value']}")
                return

            # Подтверждение покупки
            print("\n=== Purchase Summary ===")
            for item in purchase_items:
                print(f"{item['name']} x{item['quantity']} - {item['price'] * item['quantity']} gold")
            print(f"Total: {total_cost} gold")

            confirm = input("\nConfirm purchase? (yes/no): ").lower()
            if confirm not in ['yes', 'y', '1']:
                print("Purchase canceled!")
                return

            # Совершаем покупку
            for item in purchase_items:
                # Обновляем количество в магазине
                store_inventory[item['category']][item['item_id']][1] -= item['quantity']

                # Добавляем предмет в инвентарь персонажа в нужном формате
                character['inventory'][(item['category'], item['name'])] = item['item_data'][0][1]

                print(
                    f"Purchased {item['name']} x{item['quantity']} for {item['price'] * item['quantity']} gold")

            # Обновляем золото персонажа
            character['gold_value'] -= total_cost
            print(f"\nPurchase successful! Remaining gold: {character['gold_value']}")

            # Сохраняем изменения
            rewrite(character)
        except Exception as e:
            return
