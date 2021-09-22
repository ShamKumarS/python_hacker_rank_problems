# Enter your code here. Read input from STDIN. Print output to STDOUT
msize = input()
M = set(map(int, (input().split())))
nsize = input()
N = set(map(int, (input().split())))
# print(msize, M, nsize, N)
# print(M.difference(N))
# print(N.difference(M))
sym_diff = M ^ N
# print(sym_diff)
# print(sorted(sym_diff))
# sym_diff = sorted(sym_diff)
result = sorted(sym_diff)
for element in result:
    print(element)
