def task3():
    import sys
    
    input_data = sys.stdin.read().strip().split()
    N = int(input_data[0])
    K = int(input_data[1])
    positions = list(map(int, input_data[2:2+N]))
    
    # Сортируем позиции
    positions.sort()
    
    # DP: dp[i] - минимальная стоимость подключения первых i+1 компьютеров
    dp = [0] * N
    dp[0] = K  # Первый компьютер можно подключить только к потолку
    
    for i in range(1, N):
        # Вариант 1: подключить i-й компьютер к потолку
        cost1 = dp[i-1] + K
        
        # Вариант 2: подключить i-й компьютер к (i-1)-му
        distance = positions[i] - positions[i-1]
        cost2 = dp[i-1] + distance * distance
        
        dp[i] = min(cost1, cost2)
    
    print(dp[N-1])

if __name__ == "__main__":
    task3()
