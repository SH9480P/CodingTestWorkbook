from collections import abc

class Heap:
    def __init__(self):
        self.arr = [0]
        
    def size(self):
        return len(self.arr) - 1

    def push(self, item: int):
        self.arr.append(item)
        idx = len(self.arr) - 1
        while idx // 2 > 0:
            p_idx = idx // 2
            parent = self.arr[p_idx]
            if parent > self.arr[idx]:
                self.arr[idx], self.arr[p_idx] = self.arr[p_idx], self.arr[idx]
                idx = p_idx
            else:
                break
    
    def pop(self):
        if len(self.arr) < 2:
            return None
        item = self.arr[1]
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        self.arr.pop()
        idx = 1
        while idx * 2 < len(self.arr):
            c_idx = idx * 2
            child = self.arr[c_idx]
            if c_idx + 1 < len(self.arr) and child > self.arr[c_idx + 1]:
                c_idx += 1
                child = self.arr[c_idx]
            if self.arr[idx] > child:
                self.arr[idx], self.arr[c_idx] = self.arr[c_idx], self.arr[idx]
                idx = c_idx
            else:
                break
        return item

    def init(self, arr: abc.Iterable[int]):
        arr = [0] + list(arr)
        self.arr = arr
        for i in range(len(arr) - 1, 0, -1):
            idx = i
            while idx * 2 < len(self.arr):
                c_idx = idx * 2
                child = self.arr[c_idx]
                if c_idx + 1 < len(self.arr) and child > self.arr[c_idx + 1]:
                    c_idx += 1
                    child = self.arr[c_idx]
                if self.arr[idx] > child:
                    self.arr[idx], self.arr[c_idx] = self.arr[c_idx], self.arr[idx]
                    idx = c_idx
                else:
                    break
