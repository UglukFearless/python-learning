n = int(input())

resolves = []

count = 0
while count < n:
    count += 1
    resolves.append(input().lower())

l = int(input())

count = 0
errors = []
while count < l:
    count += 1
    line = input().lower().split()

    for word in line:
        if word not in resolves and word not in errors:
            errors.append(word)


for word in errors:
    print(word)