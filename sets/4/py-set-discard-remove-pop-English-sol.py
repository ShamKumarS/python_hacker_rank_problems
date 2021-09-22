n = int(input())
s = set(map(int, input().split()))
number = int(input())
for i in range(number):
    line = input().split()
    command = line[0]
    if command == 'remove':
        element = int(line[1])
        s.remove(element)
    elif command == 'discard':
        element = int(line[1])
        s.discard(element)
    else:
        s.pop()
print(sum(s))
