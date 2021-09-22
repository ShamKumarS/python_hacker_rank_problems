# Enter your code here. Read input from STDIN. Print output to STDOUT
total = int(input())
collection = set()
for i in range(total):
    collection.add(input())
# print(total, collection)
print(len(collection))
