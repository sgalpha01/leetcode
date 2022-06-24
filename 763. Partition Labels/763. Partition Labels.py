def partition_labels(s):
    partitions = []
    last = {c: i for i, c in enumerate(s)}
    start = 0
    while start < len(s):
        end = last[s[start]]
        i = start + 1
        while i < end:
            end = max(end, last[s[i]])
            i += 1
        partitions.append(end - start + 1)
        start = end + 1

    return partitions


s = "ababcbacadefegdehijhklij"
print(partition_labels(s))
