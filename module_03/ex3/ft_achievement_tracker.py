
achivements = ["first_kill", "speed_demon"
               "level_10", "boss_slayer",
               "treasure_hunter", "collector"]


class Achievement:
    def __init__(self, name: str, rarity: str) -> None:
        self.name = name
        self.rarity = rarity


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.achievements = []

    def add_achievement(self, achivement: Achievement) -> None:
        self.achievements.append(achivement)

    # it retreives the name as a set of str
    def get_achive_name(self) -> set:
        achs = set()
        for ach in self.achievements:
            achs.add(ach.name)
        return achs


class AchievementTracker:
    def __init__(self):
        self.players = []

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def analyze(self) -> None:
        print("\n=== Achievement Analytics ===")

        # convert Players data into sets of str
        ach_players = []
        for player in self.players:
            ach_players.append(player.get_achive_name())

        if not ach_players:
            print("No achivements yet!!")
            return

        # Get all uniquete ach for all the players
        all_unique = set().union(*ach_players)
        print(f"Total unique achievements: {len(all_unique)}")
        print(f"All unique achievements: {sorted(list(all_unique))}")

        # find what everyone has
        common_all = ach_players[0].intersection(*ach_players[1:])
        print(f"common to all players: {common_all}")

        # Find all rare achivements "only 1 player holds it"
        rare = set()
        for ach_name in all_unique:
            count = 0
            for player_set in ach_players:
                if ach_name in player_set:
                    count += 1
            if count == 1:
                rare.add(ach_name)

        # Compare 2 players
    def compare(self, p1_name, p2_name):
        p1 = None
        for p in self.players:
            if p.name == p1_name:
                p1 = p
                break
        p2 = None
        for p in self.players:
            if p.name == p2_name:
                p2 = p
                break
        if p1 and p2:
            s1 = p1.get_achive_name()
            s2 = p2.get_achive_name()

            print(
                f"\n{p1_name} vs {p2_name} common: {s1.intersection(s2)}"
                f"{p1_name} unique: {s1.difference(s2)}"
                f"{p2_name} unique: {s2.difference(s1)}"
            )


def add_players_ach(tracker: AchievementTracker) -> None:
    players = [
        Player("Alice"),
        Player("Peitro"),
        Player("Amanda"),
        Player("Dio"),
    ]
    achivements = [
        Achievement("first_kill", "unique"),
        Achievement("level_10", "unique"),
        Achievement("boss_slayer", "rare"),
        Achievement("collector", "commun"),
    ]
    for p in players:
        tracker.add_player(p)

    for player in tracker.players:
        for ach in achivements:
            if ach.rarity == "commun":
                player.add_achievement(ach)
            if player.name == "Alice" and ach.rarity == "unique":
                player.add_achievement(ach)
            if player.name == "Peitro" and ach.rarity == "unique":
                player.add_achievement(ach)
            if player.name == "Amanda" and ach.rarity == "unique":
                player.add_achievement(ach)
            if player.name == "Dio" and ach.rarity == "rare":
                player.add_achievement(ach)


def main():
    my_tracker = AchievementTracker() 

    # 2. Pass this instance to your function
    add_players_ach(my_tracker)
    
    # 3. Analyze
    my_tracker.analyze()

    print("=== Achievement Tracker System ===")
    for p in my_tracker.players:
        print(f"Player {p.name} achivements: {p.achievements}")


if __name__ == "__main__":
    main()
