def quick_sort(arr, start_idx, end_idx):
    if start_idx >= end_idx:
        return
    
    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx
    
    while left_idx <= right_idx:
        while left_idx <= end_idx and arr[left_idx] <= arr[pivot_idx]:
            left_idx += 1
        while right_idx > start_idx and arr[pivot_idx] < arr[right_idx]:
            right_idx -= 1
        if left_idx < right_idx:
            arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
            left_idx += 1
            right_idx -= 1
    
    arr[pivot_idx], arr[right_idx] = arr[right_idx], arr[pivot_idx]
    quick_sort(arr, start_idx, right_idx-1)
    quick_sort(arr, right_idx+1, end_idx)
    
    