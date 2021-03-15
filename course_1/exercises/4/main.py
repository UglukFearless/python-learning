def execute(point, command):
    if command[0] == 'север':
        point[1] += int(command[1])
    elif command[0] == 'юг':
        point[1] -= int(command[1])
    elif command[0] == 'восток':
        point[0] += int(command[1])
    else:
        point[0] -= int(command[1])

n = int(input())

count = 0

point = [0, 0]

while count < n:
    count += 1
    execute(point, input().lower().split())

print(*point)