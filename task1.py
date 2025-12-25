def task1():
    n, m = map(int, input().split())
    
    # Создаем таблицу DP
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Базовые случаи: (0,0) - проигрышная позиция
    dp[0][0] = 0
    
    # Заполняем таблицу
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            
            # Проверяем все возможные ходы
            can_move_to_losing = False
            
            # 1. Взять один камень из первого набора
            if i >= 1 and dp[i-1][j] == 0:
                can_move_to_losing = True
            # 2. Взять один камень из второго набора
            if j >= 1 and dp[i][j-1] == 0:
                can_move_to_losing = True
            # 3. Взять по одному камню из обоих наборов
            if i >= 1 and j >= 1 and dp[i-1][j-1] == 0:
                can_move_to_losing = True
            
            dp[i][j] = 1 if can_move_to_losing else 0
    
    # Выводим результат для начальной позиции
    result = "Win" if dp[n][m] == 1 else "Lose"
    print(result)
    
    # Выводим таблицу DP
    for i in range(n + 1):
        for j in range(m + 1):
            print(dp[i][j], end=' ')
        print()

if __name__ == "__main__":
    task1()
