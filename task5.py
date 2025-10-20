def minimum_total(triangle):
    # Копируем данные, чтобы не менять оригинал
    cost = [row[:] for row in triangle]
    shortest_path = cost
    parents = {} #словарь координат родителей
    parents[(0, 0)] = None # Исправлено: храним значения, а не индексы
    costs = dict() # словарь стоимостей для каждой вершины
    costs[(0, 0)] = triangle[0][0]
    
    
    #находим количество строк в треугольнике
    n = len(cost)
    
    # Проходим треугольник сверху вниз
    for i in range(1, n):
        line = triangle[i]
        for j in range(len(line)):
            parent1, parent2 = None, None
            if j == 0:
                parent1 = (i - 1, j)
            elif j == len(line) - 1:
                parent1 = (i - 1, j - 1)
            else:
                parent1, parent2 = (i - 1, j), (i - 1, j - 1)

            best_parent = None
            best_cost = None

            if parent2:
                if costs[parent1] > costs[parent2]:
                    best_parent = parent2
                    best_cost = costs[parent2] + line[j]
                else:
                    best_parent = parent1
                    best_cost = costs[parent1] + line[j]

            else:
                best_parent = parent1
                best_cost = costs[parent1] + line[j]
            
            parents[(i, j)] = best_parent
            costs[(i, j)] = best_cost

            #print(parents)
            #print(costs)
    
    return parents, costs

def find_shortest_path(parents, costs, triangle):
    # Находим конечную точку с минимальной стоимостью
    end_points = [p for p in costs.keys() if p[0] == max(i for i, j in costs.keys())]
    end_point = min(end_points, key=lambda p: costs[p])
    
    # Восстанавливаем путь
    path = []
    current = end_point
    while current:
        #получаем координаты нужной нам точки пути
        a, b = current
        #преобразуем координаты в точку исходного треугольника
        path.append(triangle[a][b])
        current = parents[current]
    return costs[end_point], path[::-1]

# Использование
triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
parent_dict, cost_dict = minimum_total(triangle1)
min_cost, path = find_shortest_path(parent_dict, cost_dict, triangle1)
print(f"Минимальный путь: {' → '.join(map(str, path))}")
print(f"Результат: {min_cost}")

triangle2 = [[-1],[2,3],[1,-1,-3],[4,2,1,3]]
parent_dict, cost_dict = minimum_total(triangle2)
min_cost, path = find_shortest_path(parent_dict, cost_dict, triangle2)
print(f"Минимальный путь: {' → '.join(map(str, path))}")
print(f"Результат: {min_cost}")
