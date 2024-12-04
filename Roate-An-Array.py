""""Problem: Rotate an Array
The goal is to rotate an array to the right by k steps, where the elements that go off the end reappear at the beginning. For example:

Example:
Input:
arr = [1, 2, 3, 4, 5, 6, 7], k = 3
Output:
[5, 6, 7, 1, 2, 3, 4]

Approaches:
Reversal Technique
Modular Arithmetic

Approach 1: Reversal Technique
The Reversal Technique is an efficient way to rotate an array in O(n) time with O(1) space. It involves reversing parts of the array and then the entire array.

Algorithm:
Reverse the entire array.
Reverse the first k elements.
Reverse the remaining n−k elements.
Python Code:"""
def rotateArray(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    
    # Reverse entire array
    reverse(arr, 0, n - 1)
    # Reverse the first k elements
    reverse(arr, 0, k - 1)
    # Reverse the remaining n-k elements
    reverse(arr, k, n - 1)

    return arr

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example:
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated = rotateArray(arr, k)
print("Rotated Array:", rotated)  # Output: [5, 6, 7, 1, 2, 3, 4]


"""Approach 2: Modular Arithmetic (Direct Shifting)
Using modular arithmetic, we can directly calculate the position of each element after rotation.

Algorithm:
Create a new array to store the result.
For each element at index i, calculate its new position as (i+k)%n.
Copy the rotated array back into the original array.
Python Code:"""
def rotateArray(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    rotated = [0] * n  # Create a new array of the same size
    
    for i in range(n):
        rotated[(i + k) % n] = arr[i]  # Calculate the new position
    
    return rotated

# Example:
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated = rotateArray(arr, k)
print("Rotated Array:", rotated)  # Output: [5, 6, 7, 1, 2, 3, 4]


"""Approach	             Time Complexity	Space Complexity
Reversal Technique	         O(n)	             O(1)
Modular Arithmetic	         O(n)                O(1)