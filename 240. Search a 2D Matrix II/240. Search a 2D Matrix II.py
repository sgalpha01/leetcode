def searchMatrix(matrix, target: int) -> bool:
    if target < matrix[0][0] or target > matrix[-1][-1]:
        return False
    beg, end = 0, len(matrix) - 1
    while beg <= end:
        mid = beg + (end - beg) // 2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            beg = mid + 1
        else:
            end = mid - 1
    for r in range(mid + 1):
        beg, end = 0, len(matrix[0]) - 1
        while beg <= end:
            mid = beg + (end - beg) // 2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] < target:
                beg = mid + 1
            else:
                end = mid - 1
    return False


print(searchMatrix([[-1, 3]], 3))
