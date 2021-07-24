current_height = 100
hit_count = 0
while hit_count < 10:
    hit_count += 1
    current_height *= 3 / 5
    print(hit_count, round(current_height, 4))
