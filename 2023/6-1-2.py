
example_input = """Time:      7  15   30
Distance:  9  40  200"""

full_input = """Time:        57     72     69     92
Distance:   291   1172   1176   2026"""

def serialize_string(string):
    # remove replace() for part 1
    lines = string.replace(" ", "").split("\n")
    digits = [[int(num) for num in line.split(":")[-1].strip(" ").split(" ") if num] for line in lines]
    return list(zip(*digits))

def ways_to_win(race_times):

    total_ways_to_win = 1
    for race in race_times:
        time, distance_record = race
        ways_to_win_race = 0
        for i in range(time+1):
            if i*(time-i) > distance_record:
                ways_to_win_race += 1
        
        if ways_to_win_race:
            total_ways_to_win *= ways_to_win_race
    
    return total_ways_to_win


print(serialize_string(example_input))
print(ways_to_win(serialize_string(example_input)))
print(ways_to_win(serialize_string(full_input)))