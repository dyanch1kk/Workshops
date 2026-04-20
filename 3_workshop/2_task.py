class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] > self.heap[i]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[i]
                self.heap[i] = temp
                i = parent
            else:
                break

    def pop(self):
        temp = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap[-1] = temp
        min_val = self.heap[-1]
        self.heap = self.heap[:-1]
        i = 0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            temp = self.heap[i]
            self.heap[i] = self.heap[smallest]
            self.heap[smallest] = temp
            i = smallest

        return min_val

def find_kth_largest(nums, k):
    heap = MinHeap()
    for i in range(len(nums)):
        heap.push(nums[i])
        if len(heap.heap) > k:
            heap.pop()
    return heap.heap[0]

print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))