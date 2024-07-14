#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        largest = i    # Initialize largest as root
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        # Check if right child exists and is greater than root
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            
            # Heapify the root.
            self.heapify(arr, n, largest)
    
    #Function to build a Heap from array.
    def buildHeap(self, arr, n):
        # Build a max heap.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        # Build max heap.
        self.buildHeap(arr, n)
        
        # Extract elements one by one.
        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]   # Swap
            self.heapify(arr, i, 0)
