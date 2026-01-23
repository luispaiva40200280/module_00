# Magic time
import psutil
import os
from time import perf_counter
import random


# FIBOONACCI GENORATER
def fibbonacci_seq(limits: int):
    a, b = 0, 1
    for _ in range(limits):
        yield a
        a, b = b, a + b


# Prime Genarator
def prime_seq(number: int):
    count = 0
    n = 2
    while count < number:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if (n % i == 0):
                is_prime = False
                break
        if is_prime:
            yield n
            count += 1
        n += 1


def game_event_genarator(limit: int):
    """Small function that generates a given number of events"""
    names = ["alice", "bob", "charlie", "dave", "eve", "filips",
             "gui", "hugo", "ines", "john", "kirk", "luis", "mario",
             "nini", "otto", "paulo", "quip", "rat", "stu", "tom",
             "uni", "volt", "watt", "xilo", "yuri", "zed"]
    actions = ["killed monster", "found treasure", "found a child",
               "leveled up", "joined guild", "got married",
               "offended a dwarf", "built a house", "found a secret"]
    for _ in range(limit):
        name = random.choice(names)
        level = random.randint(1, 15)
        action = random.choice(actions)
        yield f"Player {name} (level {level}) {action}"


def ft_data_stream(total_events: int = 1000) -> None:
    # see the memory usage at the start
    p = psutil.Process(os.getpid())
    baseline = p.memory_info().rss / 1024 / 1024
    # time of the strt of the program
    start_time = perf_counter()

    events_prossed = 0
    level_up_count = 0
    treasure_count = 0
    high_lvl_count = 0
    stream_events = game_event_genarator(total_events)
    print(
        "=== Game Data Stream Processor ===\n"
        f"\nProcessing {total_events} game events...\n"
    )
    i = 0
    iterator = iter(stream_events)
    while True:
        try:
            event = next(iterator)
            i += 1
            if i <= 3:
                print(f"event {i}: {event}")
            elif i == 4:
                print("----")
            try:
                start = event.find("(level )") + 7
                end = event.find("()")
                level = int(event[start:end])
                if level >= 10:
                    high_lvl_count += 1
            except ValueError:
                pass
            if "find treasure" in event:
                treasure_count += 1
            if "level up" in event:
                level_up_count += 1
            events_prossed += 1
        except StopIteration:
            break
    # after processor of the events
    end_time = perf_counter()
    duration = end_time - start_time
    # see the use of the memory
    mem = p.memory_info().rss / 1024 / 1024
    diff = (mem - baseline)

    print("=== Stream Analytics ===\n"
          f"Total events processed: {events_prossed}\n"
          f"High-level players (10+): {high_lvl_count}\n"
          f"Level-up events: {level_up_count}\n"
          )
    if diff == 0:
        print("\nMemory usage: Constant (streaming)\n")
    else:
        print(f"\nMemory usage: {diff} (streaming)\n")
    print(f"Processing time: {duration:.3f} seconds\n")

    fib_nunb = 10
    fib_gen = fibbonacci_seq(fib_nunb)
    itr_fib = iter(fib_gen)
    list_n_fib = []
    while True:
        try:
            list_n_fib.append(str(next(itr_fib)))
        except StopIteration:
            break

    seq_pr = 5
    prime_gen = prime_seq(seq_pr)
    prime_iter = iter(prime_gen)
    prime_results: list[str] = []
    while True:
        try:
            prime_results.append(str(next(prime_iter)))
        except StopIteration:
            break
    print("=== Generator Demonstration ===\n"
          f"Fibonacci sequence (first {fib_nunb}): {', '.join(list_n_fib)}\n"
          f"Prime numbers (first {seq_pr}): {', '.join(prime_results)}")


if __name__ == "__main__":
    ft_data_stream()
