from sys import stdin

N = int(stdin.readline().rstrip())

lst = [0]*N

for i in range(N) :
    lst[i] = int(stdin.readline().rstrip())
    
output_lst = []

if lst[0] > lst[1] :
    output_lst.append(lst[1])
    output_lst.append(lst[0])
else :
    output_lst.append(lst[0])
    output_lst.append(lst[1])

for i in range(2, N) :
    if lst[i] < output_lst[0] :
        output_lst = [lst[i]] + output_lst
    elif lst[i] > output_lst[-1] :
        output_lst = output_lst + [lst[i]]
    else :
        for j in range(len(output_lst)-1) :
            if (output_lst[j] < lst[i]) and (output_lst[j+1] > lst[i]) :
                output_lst = output_lst[:j+1] + [lst[i]] + output_lst[j+1:]
                break

for i in range(N) :
    print(output_lst[i])
    
    
## Heap Sorting


## 힙 구현
def heappush(heap, data) :
    heap.append(data)
    current = len(heap) - 1  ## last element current index
    
    while current > 0 :
        parent = (current - 1)//2  ## parent index
        
        if heap[parent] > heap[current] :
            heap[parent], heap[current] = heap[current], heap[parent]  ## index swift
            current = parent
        else :
            break  ## loop breaking
        
        
import heapq
h1 = [3, 4, 6, 8, 5, 7]
h2 = [3, 4, 6, 8, 5, 7]
heappush(h1, 2)
heapq.heappush(h2, 2)
print(f"힙 {h1}에 2를 추가한 결과")
print("구현한 함수의 결과: ", h1)
print("heapq 메서드의 결과:", h2)
print()
heappush(h1, 3)
heapq.heappush(h2, 3)
print(f"힙 {h1}에 3을 추가한 결과")
print("구현한 함수의 결과: ", h1)
print("heapq 메서드의 결과:", h2)


def heapify(unsorted, index, heap_size):
  largest = index
  left = 2 * index + 1
  right = 2 * index + 2
  
  if left < heap_size and unsorted[right] > unsorted[largest]:
    largest = left
    
  if right < heap_size and unsorted[right] > unsorted[largest]:
    largest = right
    
  if largest != index:
    unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
    heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
  n = len(unsorted)
  
  for i in range(n // 2 - 1, -1, -1):
    heapify(unsorted, i, n)
    
  for i in range(n - 1, 0, -1):
    unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
    heapify(unsorted, 0, i)

  return unsorted