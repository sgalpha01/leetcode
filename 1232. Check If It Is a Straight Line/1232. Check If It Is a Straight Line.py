from math import inf


def checkStraightLine(coordinates) -> bool:
    try:
        m = (coordinates[1][1] - coordinates[0][1]) / (
            coordinates[1][0] - coordinates[0][0]
        )
    except ZeroDivisionError:
        m = inf
    for i in range(2, len(coordinates)):
        try:
            if (coordinates[i][1] - coordinates[i - 1][1]) / (
                coordinates[i][0] - coordinates[i - 1][0]
            ) != m:
                return False
        except ZeroDivisionError:
            if (coordinates[i][0] == coordinates[i - 1][0]) and m != inf:
                return False
    return True
