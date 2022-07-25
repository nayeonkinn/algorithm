for case in range(10):
    n = int(input())
    building = list(map(int, input().split()))
    
    result = 0
    for i in range(2, n - 2) :
        for j in range(max(building[i - 1], building[i + 1]) + 1, building[i] + 1) : # 양 옆 건물 중 높은 건물 층수 + 1부터 그 건물 높이까지 돌면서
            if building[i - 2] < j  and building[i - 1] < j  and building[i + 1] < j  and building[i + 2] < j : # 양 옆 조망이 확보되는 경우
                result += building[i] - j + 1 # 남은 층수까지 한번에 센다
                break
    print(f'#{case + 1} {result}')