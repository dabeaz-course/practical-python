# bounce.py
#
# Exercise 1.5
cur_height = 100
bounce_ratio = 3/5
bounce_cnt = 0
while bounce_cnt < 10:
    cur_height *= bounce_ratio
    bounce_cnt += 1
    print(bounce_cnt, round(cur_height, 4))
