def linear_search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

# Example usage
if __name__ == "__main__":
    arr = [10, 23, 45, 70, 11, 15]
    n = len(arr)
    x = 70
    result = linear_search(arr, n, x)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array")
