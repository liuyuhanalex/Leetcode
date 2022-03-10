import random

direction_dict = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def once(cur_position):
    random_int = random.randint(0, 3)
    direction = direction_dict[random_int]
    return [cur_position[0] + direction[0], cur_position[1] + direction[1]]



if __name__ == '__main__':
    final_res = 0
    n = 1000000
    for i in range(n):
        start = [0, 0]
        for j in range(20):
            cur_pos = once(start)
            start = cur_pos
        if cur_pos[0] == cur_pos[1] or cur_pos[0] == -cur_pos[1]:
            final_res += 1
    print(final_res/n)
