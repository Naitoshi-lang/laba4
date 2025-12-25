def task4_efficient():
    MOD = 1000000007
    
    N = int(input())
    
    if N == 1:
        print(3)
        return
    
    # Используем DP с двумя предыдущими печеньками
    # dp[a][b] - количество последовательностей, заканчивающихся на ab
    dp = [[1] * 3 for _ in range(3)]  # для длины 2
    
    for _ in range(2, N):
        new_dp = [[0] * 3 for _ in range(3)]
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    if a != c:  # условие: первая и третья в тройке не совпадают
                        new_dp[b][c] = (new_dp[b][c] + dp[a][b]) % MOD
        dp = new_dp
    
    # Суммируем все варианты
    result = 0
    for i in range(3):
        for j in range(3):
            result = (result + dp[i][j]) % MOD
    
    print(result)
