import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Ініціалізуємо загальні витрати
    total_cost = 0
    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(cable_lengths)
    
    # Поки в купі більше одного елемента
    while len(cable_lengths) > 1:
        # Вибираємо два кабелі з найменшою довжиною
        first_min = heapq.heappop(cable_lengths)
        second_min = heapq.heappop(cable_lengths)
        
        # Обчислюємо вартість з'єднання цих двох кабелів
        cost = first_min + second_min
        
        # Додаємо сумарну довжину новоствореного кабелю нsазад в купу
        heapq.heappush(cable_lengths, cost)
        
        # Додаємо вартість цього з'єднання до загальних витрат
        total_cost += cost
    
    # Повертаємо загальні витрати
    return total_cost

# Приклад використання:
cable_lengths = [5, 4, 2, 8]
print(min_cost_to_connect_cables(cable_lengths))
