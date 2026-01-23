from typing import Any


class Player:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score
        self.active = False
        self.achivements = []
        self.regions = {
            "basic": True,
        }

    def add_achivements(self, achivement: Any) -> None:
        try:
            if type(achivement) is not str:
                lst_achivments = iter(achivement)
                while True:
                    try:
                        achivement = next(lst_achivments)
                        self.achivements.append(achivement)
                    except StopIteration:
                        break
        except TypeError:
            self.achivements.append(achivement)

    def add_regions(self, region_name: str, status: bool = True) -> None:
        # Dictionary syntax: self.dict[key] = value
        self.regions[region_name] = status

    def __repr__(self) -> str:
        return f"Player {self.name} as the scores: {self.score}"


# initialize list of playes
def init_data() -> set:
    player_set = set()
    names = ["Alice", "Bob", "Alice", "Charlie", "Diana", "Eve",
             "Frank", "Grace", "Hank", "Ivy", "Jack"]

    for i in range(3):
        name = names[i]
        score = ((i + 1) * 57) % 101
        new_player = Player(name, score)
        if i % 2 == 0:
            new_player.active = True
            new_player.add_achivements(["boss_slayer"])
        else:
            new_player.add_achivements(["first_kill", "level_10"])
            new_player.active = False
        player_set.add(new_player)
    max_level = max(p.score for p in player_set)
    for p in player_set:
        if p.score == max_level:
            p.add_achivements("Best player")
            p.add_regions("last", False)
        p.add_regions("north", True)
        p.add_regions("south", False)
    return player_set


if __name__ == "__main__":
    data_base = init_data()
    print("=== Game Analytics Dashboard ===")
    # print(f"Database created with {len(data_base)} players:\n")
    print(f"Database created with {data_base} players:\n")

    print("\n=== List Comprehension Examples ===")
    hight_scores_name = [p.name for p in data_base if p.score > 50]
    hight_scores_double = [p.score * 2 for p in data_base if p.active]
    active_users = [p.name for p in data_base if p.active]
    print(f"High scorers (>50): {hight_scores_name}")
    print(f"Scores doubled: {hight_scores_double}")
    print(f"Active users: {active_users}")
    print()
    print("=== Dict Comprehension Examples ===")
    players_scores = {p.name: p.score for p in data_base}
    score_categories = {
        "high": len([p for p in data_base if p.score > 70]),
        "medium": len([p for p in data_base if 40 >= p.score >= 70]),
        "low": len([p for p in data_base if p.score < 40])
    }
    achivement_count = {p.name: len(p.achivements) for p in data_base}
    print()
    print(f"Player scores: {players_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achivement count: {achivement_count}")
    print()
    print("=== Set Comprehension Examples ===")
    unique_names = {p.name for p in data_base}
    unique_achievements = {ach for p in data_base for ach in p.achivements}
    active_regions = {region for p in data_base
                      for region, status in p.regions.items()
                      if status is True}
    print(f"Unique names: {unique_names}")
    print(f"Unique achivement: {unique_achievements}")
    print(f"Active regions: {active_regions}")
    print()
    print("=== Combined Analysis ===")
    print(f"Total playrs: {len(data_base)}")
    print(f"Total unique_achivements: {len(unique_achievements)}")
    print("Average score:" +
          f"{sum(p.score for p in data_base) / len(data_base):.1f}")
    max_score = max(p.score for p in data_base)    
    top_perf = [player for player in data_base if player.score == max_score]
    print(f"Top performer: {top_perf[0].name} " +
          f"({top_perf[0].score} points, " +
          f"{len(top_perf[0].achivements)} achievements)")
"""     for player in data_base:
        print(player.achivements)
    pass """
