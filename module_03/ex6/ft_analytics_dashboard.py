class Player:
    def __init__(self, name: str, score: int) -> None:
        self.name = name 
        self.score = score

    def __repr__(self) -> str:
        return f"Player {self.name} as the scores: {self.score}"


# initialize list of playes
def init_data() -> set:
    player_set = set()
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve", 
             "Frank", "Grace", "Hank", "Ivy", "Jack"]

    for i in range(10):
        name = names[i]
        score = (i * 57) % 101
        new_player = Player(name, score)
        player_set.add(new_player)
    return player_set


if __name__ == "__main__":
    data_base = init_data()
    print(f"Database created with {len(data_base)} players:\n")
    for player in data_base:
        print(player)
    pass
