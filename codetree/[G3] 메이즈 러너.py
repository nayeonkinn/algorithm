import sys, copy

sys.stdin = open('input/메이즈 러너-3.txt')  # 7 1 1, 63 2 1, 9 2 1
input = sys.stdin.readline


def get_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def move():
    global answer

    new_people = []
    for person in people:
        new_person = [person[0], person[1]]
        distance = get_distance(door, person)

        for di, dj in delta:
            ni, nj = person[0] + di, person[1] + dj
            if 0 <= ni < n and 0 <= nj < n and not maze[ni][nj]:
                if get_distance(door, [ni, nj]) < distance:
                    new_person = [ni, nj]
                    distance = get_distance(door, [ni, nj])

        if new_person != door:
            new_people.append(new_person)

        if new_person != person:
            answer += 1

    return new_people


def get_start_point(person, length):
    return [max(max(person[0], door[0]) - length, 0), max(max(person[1], door[1]) - length, 0)]


def find_square():
    length = 10
    for person in people:
        now_length = max(abs(person[0] - door[0]), abs(person[1] - door[1]))
        if now_length < length:
            length = now_length
            start_point = get_start_point(person, length)
        elif now_length == length:
            now_start_point = get_start_point(person, length)
            if now_start_point < start_point:
                start_point = now_start_point
    
    return start_point, length


def rotate(start_point, length):
    x, y = start_point

    new_maze = copy.deepcopy(maze)
    for i in range(length + 1):
        for j in range(length + 1):
            new_maze[x + j][y + length - i] = max(maze[x + i][y + j] - 1, 0)

    new_people = []
    for person in people:
        if x <= person[0] < x + length + 1 and y <= person[1] < y + length + 1:
            person = [x - y + person[1], x + y + length - person[0]]
        new_people.append(person)

    new_door = [x - y + door[1], x + y + length - door[0]]

    return new_maze, new_people, new_door


n, m, k = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
people = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
door = list(map(lambda x: int(x) - 1, input().split()))
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
answer = 0

for _ in range(k):
    people = move()
    if not people: break
    start_point, length = find_square()
    maze, people, door = rotate(start_point, length)

print(answer)
print(door[0] + 1, door[1] + 1)
