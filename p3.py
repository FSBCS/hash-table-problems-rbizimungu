def count_subarrays_with_sum(arr, sum):
    initial_sum = {0:1}
    result = 0
    current_sum = 0
    arr = arr[::-1]

    for val in arr:
        current_sum += val
        if (current_sum - sum) in initial_sum:
            result += initial_sum[current_sum - sum]
        initial_sum[current_sum] = initial_sum.get(current_sum, 0) + 1
    return result