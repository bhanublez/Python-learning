# See the first question.

# DIRECTIONS FOR THIS PROBLEM:

# Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule. [The primary motivation behind this rule is to do a little bit of extra work to get much better performance on input arrays that are nearly sorted or reverse sorted.] In more detail, you should choose the pivot as follows. Consider the first, middle, and final elements of the given array. (If the array has odd length it should be clear what the "middle" element is; for an array with even length 2k, use the kth element as the "middle" element. So for the array 4 5 6 7, the "middle" element is the second one ---- 5 and not 6!) Identify which of these three elements is the median (i.e., the one whose value is in between the other two), and use this as your pivot. As discussed in the first and second parts of this programming assignment, be sure to implement Partition exactly as described in the video lectures (including exchanging the pivot element with the first element just before the main Partition subroutine).

# EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since 4 is the median of the set {1,4,8}, you would use 4 as your pivot element.

# SUBTLE POINT: A careful analysis would keep track of the comparisons made in identifying the median of the three candidate elements. You should NOT do this. That is, as in the previous two problems, you should simply add m−1 to your running total of comparisons every time you recurse on a subarray with length m.

def firstElemPivot(arr, l, r):
    i = l + 1
    for j in range(l + 1, r):
        if(arr[j] < arr[l]):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[l], arr[i-1] = arr[i-1], arr[l]
    return i-1


def lastElemPivot(arr, l, r):
    arr[l], arr[r-1] = arr[r-1], arr[l]
    return firstElemPivot(arr, l, r)

def medianOf3Pivot(arr, l, r):
    if (r-l) == 1:
        return firstElemPivot(arr, l, r)
    mid = int((r-l)/2) + l
    mid += 0 if (r-l) % 2 else -1
    candidates = [arr[l], arr[mid], arr[r-1]]
    candidates.sort()
    median = l
    if arr[mid] == candidates[1]:
        median = mid
    elif arr[r-1] == candidates[1]:
        median = r-1
    arr[l], arr[median] = arr[median], arr[l]
    return firstElemPivot(arr, l, r)


def QuickSort(arr, l, r):
    if(l >= r):
        return 0
    m = r - l -1
    pivotIdx = medianOf3Pivot(arr, l, r)
    m += QuickSort(arr, l, pivotIdx)
    m += QuickSort(arr, pivotIdx+1, r)
    return m

with open("QuickSort.txt") as f:
    content = f.readlines()
content = [int(l.strip()) for l in content]
# content = [8, 2, 4, 5, 7, 1]
print(QuickSort(content, 0, len(content)))
# for x in content:
#     print(x)
# 138382