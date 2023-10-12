def max_diff(arr, n):
    subset_sum_1 = 0
    subset_sum_2 = 0
    
    for i in range(n):
        is_single_occurrence = True
        
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                is_single_occurrence = False
                arr[i] = arr[j] = 0
                break
        
        if is_single_occurrence:
            if arr[i] > 0:
                subset_sum_1 += arr[i]
            else:
                subset_sum_2 += arr[i]
    
    return abs(subset_sum_1 - subset_sum_2)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = max_diff(arr, n)
    print("Maximum Difference =", result)

if __name__ == "__main__":
    main()
