def print_statistics(arr):
    print(len(arr))
    if len(arr) != 0:
        print(sum(arr) / len(arr))
        print(min(arr))
        print(max(arr))
    else:
        print(0)
        print(0)
        print(0)
    arr.sort()
    if len(arr) % 2 == 1:
        print(arr[len(arr) // 2])
    else:
        if len(arr) > 0:
            print((arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2)
        else:
            print(0)
