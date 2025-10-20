def minimum_total(triangle):
    # Копируем данные, чтобы не менять оригинал
    cost = [row[:] for row in triangle]
    shortest_path = cost
    parents = {} #словарь для хранения кратчайшего пути до точки
    parents['00'] = [triangle[0][0]]  # Исправлено: храним значения, а не индексы
    
    #находим количество строк в треугольнике
    n = len(cost)
    
    # Проходим треугольник сверху вниз
    for i in range(1, n):
        for j in range(i + 1):  # Исправлено: j <= i
            # max(j-1, 0) гарантирует, что индекс не будет отрицательным
            best_option = min(shortest_path[i-1][max(j-1,0)], shortest_path[i-1][j])
            shortest_path[i][j] = best_option + cost[i][j]
            
            # Определяем, от какого родителя пришли
            if shortest_path[i-1][max(j-1,0)] <= shortest_path[i-1][j]:
                # Пришли из левого родителя
                parent_key = str(i-1) + str(max(j-1,0))
            else:
                # Пришли из правого родителя  
                parent_key = str(i-1) + str(j)
            
            # Копируем путь от родителя и добавляем текущее значение
            parents[str(i) + str(j)] = parents[parent_key] + [triangle[i][j]]
    
    # Находим минимальный путь в последней строке
    min_sum = min(shortest_path[-1])
    min_index = shortest_path[-1].index(min_sum)
    min_path_key = str(n-1) + str(min_index)
    min_path = parents[min_path_key]
    
    return min_sum, min_path, parents

# Тестируем код
triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
min_sum1, path1, parents1 = minimum_total(triangle1)

triangle2 = [[-1],[2,3],[1,-1,-3],[4,2,1,3]]
min_sum2, path2, parents2 = minimum_total(triangle2)

print("Треугольник 1:")
print(f"Минимальная сумма: {min_sum1}")
print(f"Путь: {' → '.join(map(str, path1))}")
print(f"Значения пути: {path1}")

print("\nТреугольник 2:")
print(f"Минимальная сумма: {min_sum2}")
print(f"Путь: {' → '.join(map(str, path2))}")
print(f"Значения пути: {path2}")

# Покажем несколько записей из словаря parents
print("\nСловарь parents для треугольника 1:")
for key in sorted(parents1.keys()):
    print(f"Вершина {key}: {parents1[key]}")