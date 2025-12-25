def task2():
    n, m = map(int, input().split())
    
    # Для доп. вывода ограничиваем размеры
    max_n = min(n, 20)
    max_m = min(m, 20)
    
    # Создаем таблицу DP
    dp = [[0] * (max_m + 1) for _ in range(max_n + 1)]
    
    # Базовые случаи: (0,0) - проигрышная позиция
    dp[0][0] = 0
    
    # Заполняем таблицу
    for i in range(max_n + 1):
        for j in range(max_m + 1):
            if i == 0 and j == 0:
                continue
            
            can_move_to_losing = False
            
            # 1. Взять один камень из первого набора
            if i >= 1 and dp[i-1][j] == 0:
                can_move_to_losing = True
            # 2. Взять один камень из второго набора
            if j >= 1 and dp[i][j-1] == 0:
                can_move_to_losing = True
            # 3. Взять два камня из первого набора
            if i >= 2 and dp[i-2][j] == 0:
                can_move_to_losing = True
            # 4. Взять два камня из второго набора
            if j >= 2 and dp[i][j-2] == 0:
                can_move_to_losing = True
            # 5. Взять два из первого и один из второго
            if i >= 2 and j >= 1 and dp[i-2][j-1] == 0:
                can_move_to_losing = True
            # 6. Взять один из первого и два из второго
            if i >= 1 and j >= 2 and dp[i-1][j-2] == 0:
                can_move_to_losing = True
            
            dp[i][j] = 1 if can_move_to_losing else 0
    
    # Для основного решения (до 1000) используем математический анализ
    # В этой игре выигрывают позиции, где (n % 3 != m % 3) или (n % 3 == 0 and m % 3 == 0)
    # Анализируя таблицу, можно заметить закономерность
    
    # Для больших n,m используем формулу
    if (n % 3 == 0 and m % 3 == 0) or (n % 3 == m % 3 and abs(n % 3 - m % 3) == 0):
        main_result = "Lose"
    else:
        main_result = "Win"
    
    print(main_result)
    
    # Дополнительный вывод
    if n <= 20 and m <= 20:
        # Считаем количество выигрышных ходов из начальной позиции
        win_moves = 0
        
        # Проверяем все возможные ходы
        moves = [
            (n-1, m), (n, m-1), (n-2, m), (n, m-2),
            (n-2, m-1), (n-1, m-2)
        ]
        
        for new_n, new_m in moves:
            if new_n >= 0 and new_m >= 0:
                if new_n <= 20 and new_m <= 20:
                    if dp[new_n][new_m] == 0:
                        win_moves += 1
                else:
                    # Для больших значений используем ту же логику
                    if (new_n % 3 == 0 and new_m % 3 == 0) or (new_n % 3 == new_m % 3):
                        pass  # Это проигрышная позиция для противника?
                        # Нужно пересчитать для точности
        
        print(win_moves)
        
        # Выводим таблицу DP
        for i in range(max_n + 1):
            for j in range(max_m + 1):
                print(dp[i][j], end=' ')
            print()
    else:
        print(0)  # для больших значений, не выводим таблицу

if __name__ == "__main__":
    task2()
