def merge_alternate(list1, list2):
    merged = []
    for i in range(len(list1)):
        merged.append(list1[i])
        merged.append(list2[i])
    return merged

a = [1, 2, 3]
b = [4, 5]
print("Merged list:", merge_alternate(a, b))