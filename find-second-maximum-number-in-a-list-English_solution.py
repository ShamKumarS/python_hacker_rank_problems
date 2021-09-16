if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    winner = arr[n-1]
    for i in range(n-1, -1,-1):
        if arr[i] != winner:
            print(arr[i])
            break