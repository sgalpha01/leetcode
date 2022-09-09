def num_weak(properties):
    properties.sort(key=lambda x: (-x[0], x[1]))
    max_defence = 0
    weak_characters = 0
    for _, defence in properties:
        if defence < max_defence:
            weak_characters += 1
        else:
            max_defence = defence
    return weak_characters
