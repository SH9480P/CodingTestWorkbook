import random

arr = [random.randint(0, 20) for i in range(14)]

def merge(start, mid, end):
    idx1 = start
    idx2 = mid+1
    sub_arr = []
    while idx1 <= mid and idx2 <= end:
        if arr[idx1] < arr[idx2]:
            sub_arr.append(arr[idx1])
            idx1 += 1
        else:
            sub_arr.append(arr[idx2])
            idx2 += 1
    if idx1 <= mid:
        sub_arr.extend(arr[idx1:mid+1])
    else:
        sub_arr.extend(arr[idx2:end+1])
    arr[start:end+1] = sub_arr

def merge_sort(start, end):
    if start >= end:
        return
    mid = (start+end)//2
    merge_sort(start, mid)
    merge_sort(mid+1, end)
    merge(start, mid, end)

print(arr)
merge_sort(0, 13)
print(arr)