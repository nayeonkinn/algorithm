red_end = None
blue_end = None

red_visited = None
blue_visited = None

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

answer = 1e9

def check(maze, visited, i, j):
    if 0 <= i < len(maze) and 0 <= j < len(maze[0]) and not visited[i][j] and maze[i][j] != 5:
        return True
    return False

def dfs(maze, red_now, blue_now, cnt):
    global answer, red_end, blue_end

    if cnt > answer:
        return
    
    red_done = red_now == red_end
    blue_done = blue_now == blue_end

    if red_done and blue_done:
        answer = min(answer, cnt)
        return
    
    red_delta = ((0, 0), ) if red_done else delta
    blue_delta = ((0, 0), ) if blue_done else delta

    for red_di, red_dj in red_delta:
        red_ni, red_nj = red_now[0] + red_di, red_now[1] + red_dj
        if not (red_done or check(maze, red_visited, red_ni, red_nj)):
            continue

        for blue_di, blue_dj in blue_delta:
            blue_ni, blue_nj = blue_now[0] + blue_di, blue_now[1] + blue_dj

            if not (blue_done or check(maze, blue_visited, blue_ni, blue_nj)):
                continue
            
            if (red_ni, red_nj) == (blue_ni, blue_nj) or ((red_ni, red_nj) == blue_now and (blue_ni, blue_nj) == red_now) or ((red_ni, red_nj) == red_now and (blue_ni, blue_nj) == blue_now):
                continue
            
            red_visited[red_ni][red_nj] = True
            blue_visited[blue_ni][blue_nj] = True
            dfs(maze, (red_ni, red_nj), (blue_ni, blue_nj), cnt + 1)
            red_visited[red_ni][red_nj] = False
            blue_visited[blue_ni][blue_nj] = False

def solution(maze):
    global answer, red_end, blue_end, red_visited, blue_visited

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_end = (i, j)
            elif maze[i][j] == 4:
                blue_end = (i, j)

    red_visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    blue_visited = [[False] * len(maze[0]) for _ in range(len(maze))]

    red_visited[red_start[0]][red_start[1]] = True
    blue_visited[blue_start[0]][blue_start[1]] = True

    dfs(maze, red_start, blue_start, 0)

    if answer == 1e9:
        answer = 0
    
    return answer