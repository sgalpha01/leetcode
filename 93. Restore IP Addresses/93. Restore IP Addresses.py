def is_valid(s):
    if len(s) > 3 or len(s) == 0 or (s[0] == "0" and len(s) > 1) or int(s) > 255:
        return False
    return True


def restore_ip(s):
    if len(s) > 12:
        return []
    valid_parts = []
    for i in range(1, 4):
        for j in range(i + 1, i + 4):
            for k in range(j + 1, j + 4):
                s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:]
                if is_valid(s1) and is_valid(s2) and is_valid(s3) and is_valid(s4):
                    valid_parts.append(s1 + "." + s2 + "." + s3 + "." + s4)
    return valid_parts


s = "101023"
print(restore_ip(s))
