from typing import List
def heapify(a: List[int], n: int, i: int) -> None:
    largest = i
    l = 2*i + 1; r = 2*i + 2
    if l < n and a[l] > a[largest]: largest = l
    if r < n and a[r] > a[largest]: largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)
def build_max_heap(a: List[int]) -> None:
    for i in range(len(a)//2 - 1, -1, -1):
        heapify(a, len(a), i)
def heapsort(a: List[int]) -> List[int]:
    arr = list(a)
    n = len(arr)
    build_max_heap(arr)
    for end in range(n-1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0)
    return arr
if __name__ == "__main__":
    data = [4,10,3,5,1,1,20,0]
    print(heapsort(data))
