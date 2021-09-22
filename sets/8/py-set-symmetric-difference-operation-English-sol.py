# Enter your code here. Read input from STDIN. Print output to STDOUT
enumber = int(input())
eset = set(map(int, input().split()))
fnumber = int(input())
fset = set(map(int, input().split()))

print(len(eset ^ fset))
