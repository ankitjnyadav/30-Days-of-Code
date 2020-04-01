'''
Problem Statement - https://www.hackerrank.com/challenges/30-sorting/problem
'''
import sys

'''
for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
'''
def BubbleSort(arr,n):
    count=0
    for i in range(n):
        numberOfSwaps = 0
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j + 1] = arr[j+1],arr[j]
                numberOfSwaps=numberOfSwaps+1

        if numberOfSwaps == 0:
            break
        count = count + numberOfSwaps
    print('Array is sorted in {} swaps.'.format(count))
    print('First Element:',arr[0])
    print('Last Element:',arr[n-1])

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
BubbleSort(a,n)
# Write Your Code Here3
