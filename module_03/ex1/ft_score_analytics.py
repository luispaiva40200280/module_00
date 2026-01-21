from sys import argv as argv


def ft_score_analytics(sys: list[tuple]) -> None:
    list_score = argv
    scores = []
    name_file = list_score.pop(0)
    if len(list_score) > 1:
        for score in list_score:
            try:
                s = int(score)
                scores.append(s)
            except ValueError:
                print("oops, I typed ’banana’ instead of ’1000’")
                return
        print("=== Player Score Analytics ===")
        print(f"Scores processed:  {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Avarege score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    else:
        print("No scores provided. "
              + f"Usage: python3 {name_file} <score1> <score2> ...")
        return


if __name__ == "__main__":
    ft_score_analytics(argv)
