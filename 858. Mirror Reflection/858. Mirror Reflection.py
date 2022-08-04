def mirror_reflection(p, q):
    is_left = False
    hit_distance = q
    while True:
        if hit_distance % p == 0:
            if is_left:
                return 2
            if hit_distance % (2 * p) == 0:
                return 0
            return 1
        is_left = not is_left
        hit_distance += q
