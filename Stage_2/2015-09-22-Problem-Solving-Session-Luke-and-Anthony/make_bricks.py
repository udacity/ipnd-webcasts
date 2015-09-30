#Anthony's Solution

import random
​
def makebricks (small, large, goal):
    sm = 0
    lg = 0
    while goal > 0:
        if large > 0 and goal >= 5:
            lg += 1
            goal -= 5
            large -= 1
        elif small > 0:
            sm += 1
            goal -= 1
            small -= 1
        elif goal > 0:
            return "Not possible"
    return "small: " + str(sm) + " large: " + str(lg)
​
print makebricks(3, 5, 8)
print makebricks(0, 5, 8)
print makebricks(0, 5, 5)
print makebricks(20, 4, 4)
print makebricks(10, 5, 28)
​
# def shuffle(words):
#     words = words.split()
#     for i in range(len(words)-1, 0, -1):
#         j = random.randint(0, i)
#         words[i], words[j] = words[j], words[i]
#     return " ".join(words)
​
# print shuffle("1 2 3 4 5 6 7")
# print shuffle("a b c d e f g")

#Luke's Solution
small_brick_size = 1
large_brick_size = 5

def make_bricks(target_len, supply_small_bricks, supply_large_bricks):
    can_make_bricks = supply_small_bricks*small_brick_size + supply_large_bricks*large_brick_size >= target_len
    if not can_make_bricks:
        return False
    len_so_far = 0
    large_bricks_to_buy = 0
    small_bricks_to_buy = 0
    while large_bricks_to_buy < supply_large_bricks and len_so_far + large_brick_size <= target_len:
        large_bricks_to_buy += 1
        len_so_far += large_brick_size
    while small_bricks_to_buy < supply_small_bricks and len_so_far + small_brick_size <= target_len:
        small_bricks_to_buy += 1
        len_so_far += small_brick_size
    if len_so_far != target_len:
        return False
    return small_bricks_to_buy, large_bricks_to_buy


print make_bricks(6, 100, 100)
