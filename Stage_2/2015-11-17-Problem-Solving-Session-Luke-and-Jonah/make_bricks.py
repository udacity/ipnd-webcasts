
#Original, using loops
def make_bricks(small, big, goal):
    current_len = 0
    big_used = 0
    small_used = 0
    counter = 0
    while current_len < goal:
        counter += 1
        if big_used < big and current_len + 5 <= goal:
            big_used += 1
            current_len += 5
        elif small_used < small and current_len + 1 <= goal:
            small_used += 1
            current_len += 1
        elif counter >1000:
            print "infinite loop"
            break
        else:
            break
    if current_len == goal:
        return True
    return False

#Without using loops
def make_bricks(small, big, goal):
    if big * 5 + small < goal:
        return False

    max_with_big = big * 5
    if max_with_big >= goal:
        big_used = goal // 5
    else:
        big_used = big
    left = goal - big_used * 5
    if small >= left:
        return True
    return False



print make_bricks(1, 3, 7)
