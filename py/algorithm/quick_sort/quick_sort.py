def swap(elements, a, b):
    if a != b:
        tmp = elements[a]
        elements[a] = elements[b]
        elements[b] = tmp
        
def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements=elements, start=start, end=pi-1)
        quick_sort(elements=elements, start=pi+1, end=end)
        
def partition(elements, start, end):
    pivot_index = start
    pivot  = elements[pivot_index]
    
    while start < end:
        
        while  start < len(elements) and elements[start] <= pivot:
            start += 1
            
        while elements[end] > pivot:
            end -= 1
            
        if start < end:
            swap(elements=elements, a=start, b=end)
            
    swap(elements=elements, a=pivot_index, b=end)
    return end
    
    
if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')