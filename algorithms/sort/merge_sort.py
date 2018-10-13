##############################
# Merge Sort
# Type: "divide and conquer"
#
# Time: O(n*log n)
# Space: O(n)
##############################

def merge_sort(list):

    # First part: Splitting
    if len(list) < 2:
        return

    middle = len(list) // 2

    left = list[:middle]
    right = list[middle:]

    merge_sort(left)
    merge_sort(right)

    # Second part: Merging
    i = 0
    j = 0
    k = 0

    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            list[k] = left[i]
            i = i+1
        else:
            list[k] = right[j]
            j = j+1
        k = k+1

    while (i < len(left)):
        list[k] = left[i]
        i = i+1
        k = k+1

    while (j<len(right)):
        list[k] = right[j]
        j = j+1
        k = k+1

l = [54,26,93,17,77,31,44,55,20]
merge_sort(l)
print(l)
