def average(array):
    # your code goes here
    arrayset = set(array)
    distinctsum = sum(arrayset)
    totalnumber = len(arrayset)
    return distinctsum/totalnumber


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
