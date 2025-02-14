import numpy as np
import matplotlib.pyplot as plt

def dls(graph, current, target, visited, path, current_distance, depth, max_depth, result):
    """Рекурсивный поиск в глубину с ограничением"""
    if depth > max_depth:
        return False  # Достигнут лимит глубины
    
    visited.add(current)
    path.append(current)
    
    if current == target:
        if current_distance < result["min_distance"]:
            result["min_distance"] = current_distance
            result["min_path"] = path.copy()
            result["found_depth"] = depth
        visited.remove(current)
        path.pop()
        return True
    
    for neighbor, distance in graph[current]:
        if neighbor not in visited:
            if dls(graph, neighbor, target, visited, path, current_distance + distance, depth + 1, max_depth, result):
                return True
    
    visited.remove(current)
    path.pop()
    return False

def find_shortest_path_dls(graph, start, end, max_depth):
    """Функция для поиска кратчайшего пути с ограничением глубины"""
    result = {"min_distance": float('inf'), "min_path": [], "found_depth": -1}
    
    for depth in range(max_depth + 1):
        if dls(graph, start, end, set(), [], 0, 0, depth, result):
            return result["min_path"], result["min_distance"], result["found_depth"]
    
    return [], float('inf'), -1  # Если путь не найден

# Определяем граф (города и расстояния)
graph = {
    'Город A': [('Город B', 15), ('Город J', 14)],
    'Город B': [('Город A', 15), ('Город D', 12), ('Город H', 25)],
    'Город C': [('Город A', 10), ('Город D', 8), ('Город E', 20)],
    'Город D': [('Город C', 8), ('Город B', 12), ('Город E', 5), ('Город F', 5), ('Город G', 22)],
    'Город E': [('Город C', 20), ('Город D', 5), ('Город F', 18)],
    'Город F': [('Город E', 18), ('Город D', 5), ('Город G', 7)],
    'Город G': [('Город D', 22), ('Город F', 7), ('Город H', 10)],
    'Город H': [('Город G', 10), ('Город B', 25), ('Город I', 6)],
    'Город I': [('Город H', 6), ('Город J', 8)],
    'Город J': [('Город I', 8), ('Город A', 14)]
}

start_city = 'Город E'
end_city = 'Город I'
max_depth = 10  # Ограничение глубины поиска

shortest_path, shortest_distance, found_depth = find_shortest_path_dls(graph, start_city, end_city, max_depth)

if shortest_path:
    print(f'🔹 Кратчайший путь из {start_city} в {end_city}: {" -> ".join(shortest_path)}')
    print(f'🔹 Общая длина пути: {shortest_distance} км')
    print(f'🔹 Решение найдено на глубине {found_depth}')
else:
    print(f'❌ Путь из {start_city} в {end_city} не найден при глубине {max_depth}')
