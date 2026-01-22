from sys import argv as argv


class Item:
    def __init__(self, name_item: str, count: int = 1) -> None:
        self.name = name_item
        self.count = count

    def get_name(self) -> str:
        return self.name

    # This decides what shows up in the print output
    def __repr__(self):
        return f"{self.name} : {self.count}"


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.inventory = {
            "Sword": Item("Sword"),
            "Potion": Item("Postion", 3),
        }  # You can even put a dict inside the class!

    @property
    def count_all_items(self) -> int:
        count = 0
        for item in self.inventory.values():
            count += item.count
        return count

    def add_item(self, item: Item) -> Item:
        item_name = item.name.capitalize()
        if item_name in self.inventory:
            self.inventory[item_name].count += item.count
        else:
            self.inventory[item_name] = item
        return item

    def __repr__(self) -> str:
        return f"<Player {self.name} as {self.inventory}"


class GameWorld:
    def __init__(self) -> None:
        # THIS IS IT: A dictionary where the Value is a Class Instance
        self.players = {}

        # We create the object AND put it in the dict at the same time
    def add_player(self, name: str) -> Player:
        new_player = Player(name)
        self.players[name] = new_player
        return new_player

    def get_player(self, name: str) -> None:
        return self.players.get(name)


def inicialize_world() -> GameWorld:
    my_word = GameWorld()

    # add players
    player1 = my_word.add_player("Ana")
    player2 = my_word.add_player("Duda")
    player3 = my_word.add_player("test")
    # add an iventory
    # playr 1
    player1.add_item(Item("Sword", 3))
    player1.add_item(Item("Shield", 3))
    player1.add_item(Item("Potion", 3))
    # playr 2
    player2.add_item(Item("Sword", 1))
    player2.add_item(Item("Shield", 5))
    player2.add_item(Item("Potion", 10))
    # playr 3
    player3.add_item(Item("Shield", 3))
    player3.add_item(Item("Potion", 3))
    player3.add_item(Item("Helmet", 1))
    return my_word


def main(argv) -> None:
    world = inicialize_world()

    if len(argv) > 1:
        player = world.add_player("_USER_")
        for arg in argv[1:]:
            parts = arg.split(":")
            if len(parts) == 2:
                name = parts[0].capitalize()
                count = int(parts[1])
                new_item = Item(name, count)
                player.add_item(new_item)

    for player in world.players.values():
        print(f"=== Inventory System Analysis for {player.name}===")
        player_total = 0
        for item in player.inventory.values():
            player_total += item.count
        print(f"List of items : {player.inventory.keys()}")
        print(f"Total items in inventory: {list(player.inventory.values())}")
        print(f"Total items in inventory: {player_total}")
    print("-" * 45 + "\n")

    items_all = set()
    for player in world.players.values():
        for name_item in player.inventory.values():
            items_all.add(name_item.get_name())
    print(f"All Items in the game: {items_all}")
    print(f"Number of all Items: {len(items_all)}")
    print("-" * 45 + "\n")

    for player in world.players.values():
        print(f"=== Inventory System Analysis for {player.name} ===")
        total_items_player = player.count_all_items
        for item in player.inventory.values():
            item_percentege = (item.count / total_items_player) * 100
            print(f"{item} unites ({item_percentege:.1f}%)")
        print(f"\n=== Inventory Statistics for {player.name} ===")
        
        print(max(set(player.inventory.values().count)))
        

    print()
    pass


if __name__ == "__main__":
    main(argv)
