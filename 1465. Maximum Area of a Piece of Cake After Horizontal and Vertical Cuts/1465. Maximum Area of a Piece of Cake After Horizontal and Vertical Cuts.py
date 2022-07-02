def max_area(h, w, h_cuts, v_cuts):
    h_cuts.append(0)
    h_cuts.append(h)
    v_cuts.append(0)
    v_cuts.append(w)
    h_cuts.sort()
    v_cuts.sort()
    max_h, max_v = 0, 0
    for i in range(1, len(h_cuts)):
        max_h = max(max_h, h_cuts[i] - h_cuts[i - 1])
    for i in range(1, len(v_cuts)):
        max_v = max(max_v, v_cuts[i] - v_cuts[i - 1])

    return (max_h * max_v) % (10**9 + 7)
