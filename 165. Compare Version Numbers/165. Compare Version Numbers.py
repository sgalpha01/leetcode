def compare_version(ver1, ver2):
    ver1 = list(map(int, ver1.split(".")))
    ver1 += [0] * (len(ver2) - len(ver1))
    ver2 = list(map(int, ver2.split(".")))
    ver2 += [0] * (len(ver1) - len(ver2))
    return (ver1 > ver2) - (ver1 < ver2)


version1 = "1.0"
version2 = "1.0.0"
print(compare_version(version1, version2))
