50%
Test: 41 / lesson 41 (29.12). Сложность алгоритмов. Big O / 41
Student: strchik (str-top)

---
Рассмотрим следующий код для работы с большими данными:

```python
from collections import defaultdict
import sys

def process_large_dataset(data):
    # Группировка данных по категориям
    groups = defaultdict(list)
    for category, value in data:
        groups[category].append(value)
    
    # Вычисление статистики
    stats = {}
    for category, values in groups.items():
        stats[category] = {
            'count': len(values),
            'sum': sum(values),
            'avg': sum(values) / len(values),
            'max': max(values),
            'min': min(values)
        }
    
    return stats

# Данные: 1 миллион записей
data = [(i % 100, i * 2) for i in range(1_000_000)]
result = process_large_dataset(data)
```

Какова общая временная сложность алгоритма и сколько памяти он потребляет?

Selected: [5] | Points: 1.0 | Correct: [3]
---
Какой из следующих кодов наиболее эффективно создаёт словарь из списка кортежей, где первый элемент - ключ, второй - значение?

```python
pairs = [('a', 1), ('b', 2), ('c', 3)]

# Вариант А
dict_a = {}
for k, v in pairs:
    dict_a[k] = v

# Вариант Б
dict_b = dict(pairs)

# Вариант В
dict_c = {k: v for k, v in pairs}
```

Какова временная сложность каждого варианта?

Selected: [1] | Points: 0.0 | Correct: [1]
